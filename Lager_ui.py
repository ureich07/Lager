# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Lager.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QHeaderView, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(849, 706)
        icon = QIcon()
        icon.addFile(u"Resources/UrSecuri.ICO", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.btErfassen = QAction(MainWindow)
        self.btErfassen.setObjectName(u"btErfassen")
        icon1 = QIcon()
        icon1.addFile(u"Resources/Edit.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btErfassen.setIcon(icon1)
        self.btBearbeiten = QAction(MainWindow)
        self.btBearbeiten.setObjectName(u"btBearbeiten")
        icon2 = QIcon()
        icon2.addFile(u"Resources/Bearbeiten.ICO", QSize(), QIcon.Normal, QIcon.Off)
        self.btBearbeiten.setIcon(icon2)
        self.btConfig = QAction(MainWindow)
        self.btConfig.setObjectName(u"btConfig")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 0, 2, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout.addWidget(self.comboBox_3, 0, 4, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.twArtikel = QTableWidget(self.centralwidget)
        if (self.twArtikel.columnCount() < 6):
            self.twArtikel.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.twArtikel.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.twArtikel.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.twArtikel.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.twArtikel.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.twArtikel.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.twArtikel.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.twArtikel.setObjectName(u"twArtikel")
        self.twArtikel.setMinimumSize(QSize(320, 0))
        self.twArtikel.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.twArtikel.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.twArtikel.verticalHeader().setDefaultSectionSize(20)

        self.gridLayout_2.addWidget(self.twArtikel, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 849, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setEnabled(True)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addSeparator()
        self.toolBar.addAction(self.btErfassen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.btBearbeiten)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.btConfig)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Artikeldatenbank", None))
        self.btErfassen.setText(QCoreApplication.translate("MainWindow", u"Erfassen", None))
#if QT_CONFIG(tooltip)
        self.btErfassen.setToolTip(QCoreApplication.translate("MainWindow", u"Artikel erfassen", None))
#endif // QT_CONFIG(tooltip)
        self.btBearbeiten.setText(QCoreApplication.translate("MainWindow", u"Bearbeiten", None))
        self.btConfig.setText(QCoreApplication.translate("MainWindow", u"Config", None))
#if QT_CONFIG(tooltip)
        self.btConfig.setToolTip(QCoreApplication.translate("MainWindow", u"SQL Verbindung bearbeiten", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Kategorie", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Lagerort", None))
        ___qtablewidgetitem = self.twArtikel.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.twArtikel.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Marke", None));
        ___qtablewidgetitem2 = self.twArtikel.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Anzahl", None));
        ___qtablewidgetitem3 = self.twArtikel.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Datum", None));
        ___qtablewidgetitem4 = self.twArtikel.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Lagerort", None));
        ___qtablewidgetitem5 = self.twArtikel.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi
