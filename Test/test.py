import sys
import qdarkstyle
from PySide2.QtWidgets import QWidget
from ...CustomQtLib import ExtendedCombo, CustomAutoCompleter

class MainWindow(QWidget):

    def scriptsList(self, layout):
        self.search_list = ExtendedCombo.ExtendedCombo(self)

        self.completer = CustomAutoCompleter.CustomAutoCompleter(self.search_list)

        model = QStandardItemModel()

        for i,word in enumerate( ['', 'hola', 'adios', 'hello', 'good bye', 'chien', 'chat', 'pomme', 'banane', 'chaise', 'table', 'palindrome', 'lapalissade', 'truc', 'machin', 'comptabilité', 'informatique', 'cool', 'nul', 'Absence', 'inspiration', 'MaJuscuLes', 'VOILA'] ):
            item = QStandardItem(word)
            model.setItem(i, 0, item)

    
        self.search_list.setModel(model)
        self.completer.setModel(self.search_list.model())
        self.search_list.setCompleter(self.completer)

        layout.addWidget(self.search_list)

    def __init__(self, parent=None):
        super().__init__()
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)
        self.scriptsList(grid_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())