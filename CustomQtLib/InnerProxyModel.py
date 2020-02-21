from PySide2.QtCore import QSortFilterProxyModel

class InnerProxyModel(QSortFilterProxyModel):

    def filterAcceptsRow(self, sourceRow, sourceParent):
        index0 = self.sourceModel().index(sourceRow, 0, sourceParent)
        return self.parent().local_completion_prefix.lower() in self.sourceModel().data(index0).lower()