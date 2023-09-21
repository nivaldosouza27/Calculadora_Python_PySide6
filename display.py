from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MININUM_WIDTH
from PySide6.QtCore import Qt


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setPlaceholderText('Digite a sua operação')
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MININUM_WIDTH)
        self.setTextMargins(TEXT_MARGIN, TEXT_MARGIN, TEXT_MARGIN, TEXT_MARGIN)
