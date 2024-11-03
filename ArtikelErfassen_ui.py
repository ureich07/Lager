# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ArtikelErfassen.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_ArtikelErfassen(object):
    def setupUi(self, ArtikelErfassen):
        if not ArtikelErfassen.objectName():
            ArtikelErfassen.setObjectName(u"ArtikelErfassen")
        ArtikelErfassen.resize(319, 531)
        self.gridLayout = QGridLayout(ArtikelErfassen)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btSpeichern = QPushButton(ArtikelErfassen)
        self.btSpeichern.setObjectName(u"btSpeichern")

        self.gridLayout.addWidget(self.btSpeichern, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(126, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 2)

        self.btCodeCheck = QPushButton(ArtikelErfassen)
        self.btCodeCheck.setObjectName(u"btCodeCheck")

        self.gridLayout.addWidget(self.btCodeCheck, 0, 3, 1, 2)

        self.label = QLabel(ArtikelErfassen)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.tbBarcode = QLineEdit(ArtikelErfassen)
        self.tbBarcode.setObjectName(u"tbBarcode")

        self.gridLayout.addWidget(self.tbBarcode, 1, 1, 1, 4)

        self.label_2 = QLabel(ArtikelErfassen)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.tbName = QLineEdit(ArtikelErfassen)
        self.tbName.setObjectName(u"tbName")
        self.tbName.setMinimumSize(QSize(211, 0))
        self.tbName.setReadOnly(False)

        self.gridLayout.addWidget(self.tbName, 2, 1, 1, 4)

        self.label_3 = QLabel(ArtikelErfassen)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.coMarke = QComboBox(ArtikelErfassen)
        self.coMarke.setObjectName(u"coMarke")
        self.coMarke.setMinimumSize(QSize(211, 0))

        self.gridLayout.addWidget(self.coMarke, 3, 1, 1, 4)

        self.label_4 = QLabel(ArtikelErfassen)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.coHaupt = QComboBox(ArtikelErfassen)
        self.coHaupt.setObjectName(u"coHaupt")
        self.coHaupt.setMinimumSize(QSize(211, 0))

        self.gridLayout.addWidget(self.coHaupt, 4, 1, 1, 4)

        self.label_5 = QLabel(ArtikelErfassen)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.coUnter = QComboBox(ArtikelErfassen)
        self.coUnter.setObjectName(u"coUnter")
        self.coUnter.setMinimumSize(QSize(211, 0))

        self.gridLayout.addWidget(self.coUnter, 5, 1, 1, 4)

        self.label_7 = QLabel(ArtikelErfassen)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.tbGroesse = QLineEdit(ArtikelErfassen)
        self.tbGroesse.setObjectName(u"tbGroesse")
        self.tbGroesse.setMinimumSize(QSize(61, 0))

        self.gridLayout.addWidget(self.tbGroesse, 6, 1, 1, 1)

        self.label_21 = QLabel(ArtikelErfassen)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 6, 2, 1, 1)

        self.coEinheit = QComboBox(ArtikelErfassen)
        self.coEinheit.addItem("")
        self.coEinheit.addItem("")
        self.coEinheit.addItem("")
        self.coEinheit.addItem("")
        self.coEinheit.setObjectName(u"coEinheit")
        self.coEinheit.setMinimumSize(QSize(75, 0))

        self.gridLayout.addWidget(self.coEinheit, 6, 3, 1, 2)

        self.label_8 = QLabel(ArtikelErfassen)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.tbDatum = QLineEdit(ArtikelErfassen)
        self.tbDatum.setObjectName(u"tbDatum")
        self.tbDatum.setMinimumSize(QSize(61, 0))

        self.gridLayout.addWidget(self.tbDatum, 7, 1, 1, 1)

        self.label_22 = QLabel(ArtikelErfassen)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 7, 2, 1, 1)

        self.tbPreis = QLineEdit(ArtikelErfassen)
        self.tbPreis.setObjectName(u"tbPreis")
        self.tbPreis.setMinimumSize(QSize(56, 0))

        self.gridLayout.addWidget(self.tbPreis, 7, 3, 1, 1)

        self.label_9 = QLabel(ArtikelErfassen)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 7, 4, 1, 1)

        self.label_10 = QLabel(ArtikelErfassen)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)

        self.tbAnzahl = QLineEdit(ArtikelErfassen)
        self.tbAnzahl.setObjectName(u"tbAnzahl")
        self.tbAnzahl.setMinimumSize(QSize(61, 0))

        self.gridLayout.addWidget(self.tbAnzahl, 8, 1, 1, 1)

        self.label_23 = QLabel(ArtikelErfassen)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 8, 2, 1, 1)

        self.tbSoll = QLineEdit(ArtikelErfassen)
        self.tbSoll.setObjectName(u"tbSoll")
        self.tbSoll.setMinimumSize(QSize(75, 0))

        self.gridLayout.addWidget(self.tbSoll, 8, 3, 1, 2)

        self.label_6 = QLabel(ArtikelErfassen)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1)

        self.coLager = QComboBox(ArtikelErfassen)
        self.coLager.setObjectName(u"coLager")
        self.coLager.setMinimumSize(QSize(211, 0))

        self.gridLayout.addWidget(self.coLager, 9, 1, 1, 4)

        self.label_11 = QLabel(ArtikelErfassen)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)

        self.tbBrennwert = QLineEdit(ArtikelErfassen)
        self.tbBrennwert.setObjectName(u"tbBrennwert")
        self.tbBrennwert.setMinimumSize(QSize(61, 0))

        self.gridLayout.addWidget(self.tbBrennwert, 10, 1, 1, 1)

        self.label_12 = QLabel(ArtikelErfassen)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 10, 2, 1, 1)

        self.tbKalorien = QLineEdit(ArtikelErfassen)
        self.tbKalorien.setObjectName(u"tbKalorien")
        self.tbKalorien.setMinimumSize(QSize(56, 0))

        self.gridLayout.addWidget(self.tbKalorien, 10, 3, 1, 1)

        self.label_13 = QLabel(ArtikelErfassen)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 10, 4, 1, 1)

        self.label_15 = QLabel(ArtikelErfassen)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 11, 0, 1, 1)

        self.tbProtein = QLineEdit(ArtikelErfassen)
        self.tbProtein.setObjectName(u"tbProtein")
        self.tbProtein.setMinimumSize(QSize(61, 0))

        self.gridLayout.addWidget(self.tbProtein, 11, 1, 1, 1)

        self.label_16 = QLabel(ArtikelErfassen)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 11, 2, 1, 1)

        self.tbFett = QLineEdit(ArtikelErfassen)
        self.tbFett.setObjectName(u"tbFett")
        self.tbFett.setMinimumSize(QSize(56, 0))

        self.gridLayout.addWidget(self.tbFett, 11, 3, 1, 1)

        self.label_14 = QLabel(ArtikelErfassen)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 11, 4, 1, 1)

        self.label_18 = QLabel(ArtikelErfassen)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 12, 0, 1, 1)

        self.tbKohle = QLineEdit(ArtikelErfassen)
        self.tbKohle.setObjectName(u"tbKohle")
        self.tbKohle.setMinimumSize(QSize(61, 0))

        self.gridLayout.addWidget(self.tbKohle, 12, 1, 1, 1)

        self.label_19 = QLabel(ArtikelErfassen)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 12, 2, 1, 1)

        self.tbZucker = QLineEdit(ArtikelErfassen)
        self.tbZucker.setObjectName(u"tbZucker")
        self.tbZucker.setMinimumSize(QSize(56, 0))

        self.gridLayout.addWidget(self.tbZucker, 12, 3, 1, 1)

        self.label_17 = QLabel(ArtikelErfassen)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 12, 4, 1, 1)

        self.label_20 = QLabel(ArtikelErfassen)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.label_20, 13, 0, 1, 1)

        self.twListe = QTableWidget(ArtikelErfassen)
        if (self.twListe.columnCount() < 4):
            self.twListe.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.twListe.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.twListe.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.twListe.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.twListe.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.twListe.setObjectName(u"twListe")
        self.twListe.setMinimumSize(QSize(211, 0))

        self.gridLayout.addWidget(self.twListe, 13, 1, 1, 4)


        self.retranslateUi(ArtikelErfassen)

        QMetaObject.connectSlotsByName(ArtikelErfassen)
    # setupUi

    def retranslateUi(self, ArtikelErfassen):
        ArtikelErfassen.setWindowTitle(QCoreApplication.translate("ArtikelErfassen", u"Artikel erfassen", None))
        self.btSpeichern.setText(QCoreApplication.translate("ArtikelErfassen", u"Speichern", None))
        self.btCodeCheck.setText(QCoreApplication.translate("ArtikelErfassen", u"Check Code", None))
        self.label.setText(QCoreApplication.translate("ArtikelErfassen", u"Barcode", None))
        self.label_2.setText(QCoreApplication.translate("ArtikelErfassen", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("ArtikelErfassen", u"Marke", None))
        self.label_4.setText(QCoreApplication.translate("ArtikelErfassen", u"Hauptkat.", None))
        self.label_5.setText(QCoreApplication.translate("ArtikelErfassen", u"Unterkat.", None))
        self.label_7.setText(QCoreApplication.translate("ArtikelErfassen", u"Gewicht", None))
        self.label_21.setText(QCoreApplication.translate("ArtikelErfassen", u"       Einheit", None))
        self.coEinheit.setItemText(0, QCoreApplication.translate("ArtikelErfassen", u"g", None))
        self.coEinheit.setItemText(1, QCoreApplication.translate("ArtikelErfassen", u"ml", None))
        self.coEinheit.setItemText(2, QCoreApplication.translate("ArtikelErfassen", u"Kg", None))
        self.coEinheit.setItemText(3, QCoreApplication.translate("ArtikelErfassen", u"L", None))

        self.label_8.setText(QCoreApplication.translate("ArtikelErfassen", u"Ablaufdatum", None))
        self.tbDatum.setText("")
        self.label_22.setText(QCoreApplication.translate("ArtikelErfassen", u"       Preis", None))
        self.label_9.setText(QCoreApplication.translate("ArtikelErfassen", u"\u20ac", None))
        self.label_10.setText(QCoreApplication.translate("ArtikelErfassen", u"Anzahl ", None))
        self.label_23.setText(QCoreApplication.translate("ArtikelErfassen", u"       Soll", None))
        self.label_6.setText(QCoreApplication.translate("ArtikelErfassen", u"Lagerort", None))
        self.label_11.setText(QCoreApplication.translate("ArtikelErfassen", u"Brennwert", None))
        self.label_12.setText(QCoreApplication.translate("ArtikelErfassen", u"kJ   Kalorien", None))
        self.label_13.setText(QCoreApplication.translate("ArtikelErfassen", u"kcal", None))
        self.label_15.setText(QCoreApplication.translate("ArtikelErfassen", u"Protein", None))
        self.label_16.setText(QCoreApplication.translate("ArtikelErfassen", u"g   Fett", None))
        self.label_14.setText(QCoreApplication.translate("ArtikelErfassen", u"g", None))
        self.label_18.setText(QCoreApplication.translate("ArtikelErfassen", u"Kohlehydrate", None))
        self.label_19.setText(QCoreApplication.translate("ArtikelErfassen", u"g  Zucker", None))
        self.label_17.setText(QCoreApplication.translate("ArtikelErfassen", u"g", None))
        self.label_20.setText(QCoreApplication.translate("ArtikelErfassen", u"Liste", None))
        ___qtablewidgetitem = self.twListe.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ArtikelErfassen", u"Datum", None));
        ___qtablewidgetitem1 = self.twListe.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ArtikelErfassen", u"Anzahl", None));
        ___qtablewidgetitem2 = self.twListe.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ArtikelErfassen", u"Preis", None));
        ___qtablewidgetitem3 = self.twListe.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ArtikelErfassen", u"ID", None));
    # retranslateUi

