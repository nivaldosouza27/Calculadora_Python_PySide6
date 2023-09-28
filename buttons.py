from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from functions import isNumOrDot, isEmpty


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_Style()

    def config_Style(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        self.setCheckable(True)


class ButtonsGrid(QGridLayout):
    def __init__(self, display, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

        self.display = display
        self._makeGrid()

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, buttton_text in enumerate(row):
                button = Button(buttton_text)

                if not isNumOrDot(buttton_text) and not isEmpty(buttton_text):
                    button.setProperty('cssClass', 'specialButton')

                self.addWidget(button, i, j)
                buttonSlot = self._makeButtonTextDisplaySlot(
                    self._insertButtonTextToDisplay,
                    button,
                )
                button.clicked.connect(buttonSlot)

    def _makeButtonTextDisplaySlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(checked):
            func(checked, *args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self, checked, button):
        button_text = button.text()
        self.display.insert(button_text)
        print(button_text)
