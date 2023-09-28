import sys
from main_window import MainWindow
from display import Display
from info import Info
from styles import setupTheme
from buttons import ButtonsGrid
from PySide6.QtWidgets import QApplication


if __name__ == '__main__':

    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Setup Theme
    setupTheme()

    # Info
    info = Info('5 ^ 2 = 25')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # GridButton
    buttons_grid = ButtonsGrid(display)
    window.vLayout.addLayout(buttons_grid)

    # Executando a aplicação Completa
    window.adjustFixedSize()
    window.show()
    app.exec()
