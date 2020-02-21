from PySide2.QtWidgets import QComboBox, QLineEdit
from PySide2.QtCore import Qt, QEvent

### A classical QComboBox with an AutoCompleter that handles Tab key completion.
# If Tab key is pressed with no selection, the first item of the completer will
# be set. If you use arrows then press Tab, the selected item will be set
### Author : Florian HUCKEL (Tours, France) v.1.0 (21/02/2020)
class ExtendedCombo(QComboBox):

    def __init__( self,  parent = None):
        # You need to have the parent widget which contains the completer
        super(ExtendedCombo, self ).__init__( parent )
        # Set the edition mode to be able to enter text in the ComboBox
        self.setEditable(True)
        self.setInsertPolicy(QComboBox.NoInsert)
        self.setLineEdit(QLineEdit(self))

    def event(self, event):
        # Catch if Tab is pressed
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Tab:
            # Adjust Text Item selection if manual selection
            item = self.model().findItems(self.lineEdit().text(), Qt.MatchContains)              
            if len(item) != 0:
                # Adjust Text Item selection if manual action
                self.completer().setCurrentRow(self.completer().popup().selectionModel().currentIndex().row())
                # Set completed text to ComboBox
                self.lineEdit().setText(self.completer().currentCompletion())
            else:
                # Clear text if nothing matches
                self.lineEdit().setText("")

            event.accept()
        return QComboBox.event(self,event)