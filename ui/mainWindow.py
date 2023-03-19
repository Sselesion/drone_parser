from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QCheckBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

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
        self.setFixedSize(400, 600)

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

        VLayoutHead = QVBoxLayout()
        hLayoutMain = QHBoxLayout()
        hLayoutFooter = QHBoxLayout()

        #  title
        header_label = QLabel("Поиск комплектующих для БПЛА")
        header_label.setFont(QFont("Arial", 18))
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #  descr
        description_label = QTextEdit(
            "Данная программа осуществляет поиск комплектующих для БпЛА. Необходимо выбрать сайты, в которых будет осуществляться поиск.\
            Нажатие на кнопку \"ЗАПУСТИТЬ ПОИСК\" осуществлит поиск комплектующих.\
            Нажатие на кнопку \"ВЫГРУЗИТЬ EXCEL файл\" осуществлит выгрузку комплектующих в Excel."
        )
        description_label.setFont(QFont("Tahoma", 12))
        description_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        description_label.setReadOnly(True)
        # header layout
        VLayoutHead.addWidget(header_label)
        VLayoutHead.addWidget(description_label)

        vLayout.addLayout(VLayoutHead)

        #  main h layout
        hLayoutMain.addLayout(GridCB)

        vLayout.addLayout(hLayoutMain)

        #  footer h layout
        hLayoutFooter.addWidget(hSpacer)

        self.parseBtn = QPushButton("ЗАПУСТИТЬ ПОИСК")
        hLayoutFooter.addWidget(self.parseBtn)

        self.saveBtn = QPushButton("Выгрузить EXCEL файл")
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
            self.ShowDialog("Перед выгрузкой данных необходимо запустить их поиск")
        else:
            get_excel.make(self.parsed_data)
            self.ShowDialog("Данные выгружены в excel таблицу!")

    def ShowDialog(self, text: str):
        """
        Shows some msg to user
        """
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Сообщение")
        dlg.setText(text)
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok )
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Yes:
            pass
        else:
            pass

    def _startParsing(self):
        parsing_sites_ids = []
        for i, v in enumerate(self.listCheckBox):
            if v.isChecked():
                parsing_sites_ids.append(i)

        if len(parsing_sites_ids) == 0:
            self.ShowDialog("Не выбран ни один сайт для поиска!")
        else:
            self.ShowDialog(
                "Получение информации по комплекутющим может занять продолжительное время!"
            )
            self.parsed_data = pars.parse(parsing_sites_ids)
