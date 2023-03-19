import logging
import sys

from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QCheckBox,
    QGridLayout,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QTableWidget,
    QVBoxLayout,
    QWidget,
)

from ui.appLoggerWidget import LoggerWidget
import get_excel
import pars


class MainWindow(QWidget):
    def __init__(self):
        """
        :param interactor: immutable object - global hotspot for entire application
        :param login:
        """
        super(MainWindow, self).__init__()
        self.parsed_data = {}
        # window properties
        self.setWindowTitle("Поиск комплектующих для БПЛА")
        # self.setWindowIcon(QIcon(r'')) todo
        self.resize(1000, 600)

        # setting layouts
        #  sites check boxes:
        self.listCheckBox = [
            "aeromotus.ru",
            "air-hobby.ru",
            "mydrone.ru",
        ]
        GridCB = QGridLayout()
        for i, v in enumerate(self.listCheckBox):
            self.listCheckBox[i] = QCheckBox(v)
            GridCB.addWidget(self.listCheckBox[i], i, 0)
        # Custom spacer
        vSpacer = QWidget()
        hSpacer = QWidget()
        vSpacer.setSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding
        )
        hSpacer.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )

        GridCB.addWidget(vSpacer)

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
        hLayoutFooter.addWidget(hSpacer)

        self.parseBtn = QPushButton("ЗАПУСК ПОИСКА ДАННЫХ")
        hLayoutFooter.addWidget(self.parseBtn)

        self.saveBtn = QPushButton("Экспорт данных в EXCEL")
        hLayoutFooter.addWidget(self.saveBtn)

        vLayout.addLayout(hLayoutFooter)

        #  window layout
        self.setLayout(vLayout)

        # actions
        self._createAction()

    def _createAction(self):
        self.parseBtn.clicked.connect(self._startParsing)
        self.saveBtn.clicked.connect(self._save)

    def _save(self):
        if not self.parsed_data:
            self.loggerWidget.error(
                "Для начала необходимо провести поиск комплектующих. Выберите сайты, отметив их чекбоксами и нажмите на кнопку 'ЗАПУСК ПОИСКА ДАННЫХ'"
            )
        else:
            get_excel.make(self.parsed_data)

    def _startParsing(self):
        parsing_sites_ids = []
        for i, v in enumerate(self.listCheckBox):
            if v.isChecked():
                parsing_sites_ids.append(i)
        pars.parse(parsing_sites_ids)

        if len(parsing_sites_ids) == 0:
            self.loggerWidget.error("Вы не выбрали ни один из сайтов!")
            return

        self.loggerWidget.info(str(parsing_sites_ids))
