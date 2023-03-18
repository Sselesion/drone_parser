import sys
from PyQt6.QtWidgets import QApplication
from ui.mainWindow import MainWindow

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
