import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from style import setupTheme

from buttons import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # info
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)  # type: ignore

    # Display
    display = Display()
    window.addWidgetToVLayout(display)  # type: ignore

    # define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
