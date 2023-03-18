import sys, logging
from Applogger import LoggerWidget

from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QMainWindow,
    QApplication,
    QTableWidget,
    QGridLayout,
    QCheckBox,
    QVBoxLayout,
    QPushButton,
    QSizePolicy
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
        self.resize(1200, 600)

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
        mySpacer = QWidget()
        mySpacer.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        GridCB.addWidget(mySpacer)

        vLayout = QVBoxLayout()

        hLayoutMain = QHBoxLayout()
        hLayoutFooter = QHBoxLayout()

        #  main h layout
        hLayoutMain.addLayout(GridCB)
        # hLayoutMain.addLayout(FeaturLayout) todo
        self.loggerWidget = LoggerWidget()
        hLayoutMain.addWidget(self.loggerWidget)


        vLayout.addLayout(hLayoutMain)

        #  footer h layout
        self.parseBtn = QPushButton('Start parsing')
        hLayoutFooter.addWidget(self.parseBtn)
        vLayout.addLayout(hLayoutFooter)

        #  window layout
        self.setLayout(vLayout)
        # central_widget = QWidget()
        # self.setCentralWidget(central_widget)
        # central_widget = vLayout

        # actions
        self._createAction()

    def _createAction(self):
        self.parseBtn.clicked.connect(self._startParsing)

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

    def checkboxChanged(self):
        self.labelResult.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
