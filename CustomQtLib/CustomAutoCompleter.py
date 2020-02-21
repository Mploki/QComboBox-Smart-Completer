from PySide2.QtWidgets import QCompleter
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtCore import Qt, QModelIndex
from . import InnerProxyModel

### Set and display the autocomplete list with matching elements containing the string.
#   This list is sorted by elements starting with the string first, and then element containing the string
### Author : Florian HUCKEL (Tours, France) v.1.0 (21/02/2020)
class CustomAutoCompleter(QCompleter):

    def __init__(self, parent=None):
        super(CustomAutoCompleter, self).__init__(parent)
        self.global_completion_prefix = ""
        self.source_model = QStandardItemModel()
        self.setCompletionMode(QCompleter.PopupCompletion)

    def setModel(self, model):
        self.source_model = model
        super(CustomAutoCompleter, self).setModel(self.source_model)

    def updateModel(self):
        # Create and Sort Item in a local AutoCompletion list
        self.local_completion_prefix = self.global_completion_prefix
        local_model = QStandardItemModel()
        sorting_model_list = self.source_model.findItems(self.local_completion_prefix, Qt.MatchStartsWith)
        i = 0
            # This is not the cleanest idea, there should be a way to do this with a better optimization
            # But in python, who really care about opti'? ;)
        for mod in sorting_model_list:
            item = QStandardItem(mod)
            local_model.setItem(i, 0, item)
            i += 1
        for mod in self.source_model.findItems(self.local_completion_prefix, Qt.MatchContains):
            if len(local_model.findItems(mod.text())) == 0:
                item = QStandardItem(mod)
                local_model.setItem(i, 0, item)
                i += 1
        proxy_model = InnerProxyModel.InnerProxyModel(self)
        proxy_model.setSourceModel(local_model)
           
        super(CustomAutoCompleter, self).setModel(proxy_model)

    def splitPath(self, path):
        self.global_completion_prefix = path
        self.updateModel()
        return ""