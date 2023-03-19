import logging

from PyQt6 import QtWidgets


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

        log_text_box = QTextEditLogger(self)
        log_text_box.setFormatter(logging.Formatter("[%(asctime)s] -  %(message)s"))
        logging.getLogger().addHandler(log_text_box)
        logging.getLogger().setLevel(logging.INFO)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(log_text_box.widget)
        self.setLayout(layout)

    def info(self, msg: str):
        logging.info(msg)

    def warning(self, msg: str):
        logging.warning(msg)

    def error(self, msg: str):
        logging.error(msg)
