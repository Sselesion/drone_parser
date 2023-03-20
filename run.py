import sys

from PyQt6.QtWidgets import QApplication

from ui.mainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
