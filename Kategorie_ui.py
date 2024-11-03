# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Kategorie.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Kategorie(object):
    def setupUi(self, Kategorie):
        if not Kategorie.objectName():
            Kategorie.setObjectName(u"Kategorie")
        Kategorie.resize(697, 474)
        self.gridLayout = QGridLayout(Kategorie)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Kategorie)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.label_2 = QLabel(Kategorie)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)

        self.tbHaupt = QLineEdit(Kategorie)
        self.tbHaupt.setObjectName(u"tbHaupt")
        self.tbHaupt.setMinimumSize(QSize(141, 0))

        self.gridLayout.addWidget(self.tbHaupt, 1, 0, 1, 2)

        self.twHaupt = QTableWidget(Kategorie)
        if (self.twHaupt.columnCount() < 2):
            self.twHaupt.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.twHaupt.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.twHaupt.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.twHaupt.setObjectName(u"twHaupt")
        font = QFont()
        font.setPointSize(8)
        self.twHaupt.setFont(font)
        self.twHaupt.verticalHeader().setMinimumSectionSize(20)
        self.twHaupt.verticalHeader().setDefaultSectionSize(20)

        self.gridLayout.addWidget(self.twHaupt, 1, 2, 4, 1)

        self.tbHaupt2 = QLineEdit(Kategorie)
        self.tbHaupt2.setObjectName(u"tbHaupt2")
        self.tbHaupt2.setEnabled(False)
        self.tbHaupt2.setMinimumSize(QSize(141, 0))
        self.tbHaupt2.setFrame(True)

        self.gridLayout.addWidget(self.tbHaupt2, 1, 3, 1, 2)

        self.twUnter = QTableWidget(Kategorie)
        if (self.twUnter.columnCount() < 2):
            self.twUnter.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.twUnter.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.twUnter.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.twUnter.setObjectName(u"twUnter")
        self.twUnter.setFont(font)
        self.twUnter.verticalHeader().setMinimumSectionSize(20)
        self.twUnter.verticalHeader().setDefaultSectionSize(20)

        self.gridLayout.addWidget(self.twUnter, 1, 5, 4, 1)

        self.verticalSpacer = QSpacerItem(20, 118, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 2, 1)

        self.tbUnter = QLineEdit(Kategorie)
        self.tbUnter.setObjectName(u"tbUnter")
        self.tbUnter.setMinimumSize(QSize(141, 0))

        self.gridLayout.addWidget(self.tbUnter, 2, 3, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 118, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 4, 1, 1)

        self.btAddHaupt = QPushButton(Kategorie)
        self.btAddHaupt.setObjectName(u"btAddHaupt")

        self.gridLayout.addWidget(self.btAddHaupt, 4, 0, 1, 2)

        self.label_3 = QLabel(Kategorie)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.label_4 = QLabel(Kategorie)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 3, 1, 1)

        self.tbLager = QLineEdit(Kategorie)
        self.tbLager.setObjectName(u"tbLager")
        self.tbLager.setMinimumSize(QSize(141, 0))

        self.gridLayout.addWidget(self.tbLager, 6, 0, 1, 2)

        self.twLager = QTableWidget(Kategorie)
        if (self.twLager.columnCount() < 2):
            self.twLager.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.twLager.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.twLager.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        self.twLager.setObjectName(u"twLager")
        self.twLager.setFont(font)
        self.twLager.verticalHeader().setMinimumSectionSize(20)
        self.twLager.verticalHeader().setDefaultSectionSize(20)

        self.gridLayout.addWidget(self.twLager, 6, 2, 3, 1)

        self.tbMarke = QLineEdit(Kategorie)
        self.tbMarke.setObjectName(u"tbMarke")
        self.tbMarke.setMinimumSize(QSize(141, 0))

        self.gridLayout.addWidget(self.tbMarke, 6, 3, 1, 2)

        self.twMarke = QTableWidget(Kategorie)
        if (self.twMarke.columnCount() < 2):
            self.twMarke.setColumnCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.twMarke.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.twMarke.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        self.twMarke.setObjectName(u"twMarke")
        self.twMarke.setFont(font)
        self.twMarke.verticalHeader().setMinimumSectionSize(20)
        self.twMarke.verticalHeader().setDefaultSectionSize(20)

        self.gridLayout.addWidget(self.twMarke, 6, 5, 3, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 88, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_4, 7, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 88, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_3, 7, 4, 1, 1)

        self.btAddLager = QPushButton(Kategorie)
        self.btAddLager.setObjectName(u"btAddLager")

        self.gridLayout.addWidget(self.btAddLager, 8, 0, 1, 2)

        self.btAddUnter = QPushButton(Kategorie)
        self.btAddUnter.setObjectName(u"btAddUnter")

        self.gridLayout.addWidget(self.btAddUnter, 4, 3, 1, 2)

        self.btAddMarke = QPushButton(Kategorie)
        self.btAddMarke.setObjectName(u"btAddMarke")

        self.gridLayout.addWidget(self.btAddMarke, 8, 3, 1, 2)


        self.retranslateUi(Kategorie)

        QMetaObject.connectSlotsByName(Kategorie)
    # setupUi

    def retranslateUi(self, Kategorie):
        Kategorie.setWindowTitle(QCoreApplication.translate("Kategorie", u"Kategorie bearbeiten", None))
        self.label.setText(QCoreApplication.translate("Kategorie", u"Hauptkategorie", None))
        self.label_2.setText(QCoreApplication.translate("Kategorie", u"Unterkategorie", None))
        ___qtablewidgetitem = self.twHaupt.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Kategorie", u"Name", None));
        ___qtablewidgetitem1 = self.twHaupt.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Kategorie", u"ID", None));
        ___qtablewidgetitem2 = self.twUnter.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Kategorie", u"Name", None));
        ___qtablewidgetitem3 = self.twUnter.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Kategorie", u"ID", None));
        self.btAddHaupt.setText(QCoreApplication.translate("Kategorie", u"Hinzuf\u00fcgen", None))
        self.label_3.setText(QCoreApplication.translate("Kategorie", u"Lagerort", None))
        self.label_4.setText(QCoreApplication.translate("Kategorie", u"Marke", None))
        ___qtablewidgetitem4 = self.twLager.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Kategorie", u"Name", None));
        ___qtablewidgetitem5 = self.twLager.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Kategorie", u"ID", None));
        ___qtablewidgetitem6 = self.twMarke.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Kategorie", u"Name", None));
        ___qtablewidgetitem7 = self.twMarke.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Kategorie", u"ID", None));
        self.btAddLager.setText(QCoreApplication.translate("Kategorie", u"Hinzuf\u00fcgen", None))
        self.btAddUnter.setText(QCoreApplication.translate("Kategorie", u"Hinzuf\u00fcgen", None))
        self.btAddMarke.setText(QCoreApplication.translate("Kategorie", u"Hinzuf\u00fcgen", None))
    # retranslateUi

