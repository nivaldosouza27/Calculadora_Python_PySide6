import sys
from main_window import MainWindow
from display import Display
from PySide6.QtWidgets import QApplication


if __name__ == '__main__':

    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Display
    display = Display()
    window.addToVLayout(display)

    # Executando a aplicação Completa
    window.adjustFixedSize()
    window.show()
    app.exec()
