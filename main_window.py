# import PySide6.QtCore
from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QWidget)
from PySide6.QtGui import QIcon
from variables import WINDOWS_ICON_PATH


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # Configurando o Layout Basico
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # Titulo da janela
        self.setWindowTitle('Calculadora')

        # Definir o Icone da Janela
        icon = QIcon(str(WINDOWS_ICON_PATH))
        self.setWindowIcon(icon)

    # Ultima Tarefa

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
