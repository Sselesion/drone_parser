import sys, logging
from ui.appLoggerWidget import LoggerWidget

from PyQt6.QtGui import QAction, QIcon, QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QMainWindow,
    QTableWidget,
    QGridLayout,
    QCheckBox,
    QVBoxLayout,
    QPushButton,
    QSizePolicy,
    QLabel,
    QTextEdit,
    QDialogButtonBox,
    QDialog,
    QMessageBox
)


class MainWindow(QWidget):

    def __init__(self):
        """
        :param interactor: immutable object - global hotspot for entire application
        :param login:
        """
        super(MainWindow, self).__init__()

        # window properties
        self.setWindowTitle("Парсер комплектующих БПЛА")
        # self.setWindowIcon(QIcon(r'')) todo
        # self.resize(600, 600)
        self.setFixedSize(400, 600)

        # setting layouts
        #  sites check boxes:
        self.listCheckBox = ['https://aeromotus.ru',
                             'https://nelk.ru',
                             'https://dji.com/ru/dji-fpv/specs',
                             'https://geobox.ru'
                             ]
        GridCB = QGridLayout()
        for i, v in enumerate(self.listCheckBox):
            self.listCheckBox[i] = QCheckBox(v)
            GridCB.addWidget(self.listCheckBox[i], i, 0)
        # Custom spacer
        vSpacer = QWidget()
        hSpacer = QWidget()
        vSpacer.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        hSpacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

        GridCB.addWidget(vSpacer)


        vLayout = QVBoxLayout()

        VLayoutHead = QVBoxLayout()
        hLayoutMain = QHBoxLayout()
        hLayoutFooter = QHBoxLayout()

        #  title
        header_label = QLabel("Поиск комплектующих для БПЛА")
        header_label.setFont(QFont("Arial", 18))
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #  descr
        description_label = QTextEdit("Описание описание описание описание описание описание описание описание описание описание описание описание описание описание описание описание описание описание описание описание описание описание описание описание описание описание")
        description_label.setFont(QFont("Arial", 14))
        description_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        description_label.setReadOnly(True)
        # header layout
        VLayoutHead.addWidget(header_label)
        VLayoutHead.addWidget(description_label)

        vLayout.addLayout(VLayoutHead)

        #  main h layout
        hLayoutMain.addLayout(GridCB)
        # hLayoutMain.addLayout(FeaturLayout) todo
        # self.loggerWidget = LoggerWidget()
        # hLayoutMain.addWidget(self.loggerWidget)


        vLayout.addLayout(hLayoutMain)

        #  footer h layout
        hLayoutFooter.addWidget(hSpacer)

        self.parseBtn = QPushButton('Спарсить')
        hLayoutFooter.addWidget(self.parseBtn)

        self.saveBtn = QPushButton('Сохранить')
        hLayoutFooter.addWidget(self.saveBtn)

        vLayout.addLayout(hLayoutFooter)

        #  window layout
        self.setLayout(vLayout)

        # actions
        self._createAction()


    def _createAction(self): ...
        # self.parseBtn.clicked.connect(self._startParsing)
        # self.saveBtn.clicked.connect(self._save)

    def _save(self):
        self.loggerWidget.error('implement me!!')

    def ShowDialog(self, text: str):
        """
        Shows some msg to user
        """
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Сообщение")
        dlg.setText(text)
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Yes:
            print("Yes!")
        else:
            print("No!")
        # if button == QMessageBox.standardButton:
        #     print("OK!")
    def _startParsing(self):
        parsing_sites_ids = []
        parsing_sites_url = []
        for i, v in enumerate(self.listCheckBox):
            if v.isChecked():
                parsing_sites_ids.append(i)
                parsing_sites_url.append(v.text())
        if len(parsing_sites_ids) == 0:
            self.loggerWidget.error("Nothing to parse")
            return
        self.loggerWidget.info(str(parsing_sites_ids))
        # self.loggerWidget.info("parsing sites ids:" +
        #                        " ".join(str(id) for id in parsing_sites_ids) +
        #                        "\tparsing sites urls:" +
        #                        " ".join(str(url) for url in parsing_sites_url))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()