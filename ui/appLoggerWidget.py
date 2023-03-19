import sys
from PyQt6 import QtWidgets
import logging

# Uncomment below for terminal log messages
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s')


class QTextEditLogger(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = QtWidgets.QPlainTextEdit(parent)
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)


class LoggerWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        logTextBox = QTextEditLogger(self)
        # You can format what is printed to text box
        logTextBox.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(logTextBox)
        # You can control the logging level
        logging.getLogger().setLevel(logging.DEBUG)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(logTextBox.widget)
        self.setLayout(layout)

        # self.test()

    def info(self, msg: str):
        logging.info(msg)

    def warning(self, msg: str):
        logging.warning(msg)

    def error(self, msg: str):
        logging.error(msg)

    def test(self):
        logging.debug('damn, a bug')
        logging.info('something to remember')
        logging.warning('that\'s not right')
        logging.error('foobar')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    mw = QtWidgets.QMainWindow()
    lw = LoggerWidget()
    mw.setCentralWidget(lw)
    mw.show()
    lw.test()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')
