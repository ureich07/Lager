# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConfigSqlConnection.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_ConfigSQLConnection(object):
    def setupUi(self, ConfigSQLConnection):
        if not ConfigSQLConnection.objectName():
            ConfigSQLConnection.setObjectName(u"ConfigSQLConnection")
        ConfigSQLConnection.resize(352, 151)
        self.gridLayout_2 = QGridLayout(ConfigSQLConnection)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbSqlIp = QLabel(ConfigSQLConnection)
        self.lbSqlIp.setObjectName(u"lbSqlIp")

        self.gridLayout.addWidget(self.lbSqlIp, 0, 0, 1, 1)

        self.tbSqlIp = QLineEdit(ConfigSQLConnection)
        self.tbSqlIp.setObjectName(u"tbSqlIp")

        self.gridLayout.addWidget(self.tbSqlIp, 0, 1, 1, 1)

        self.lbSqlPort = QLabel(ConfigSQLConnection)
        self.lbSqlPort.setObjectName(u"lbSqlPort")

        self.gridLayout.addWidget(self.lbSqlPort, 1, 0, 1, 1)

        self.tbSqlPort = QLineEdit(ConfigSQLConnection)
        self.tbSqlPort.setObjectName(u"tbSqlPort")

        self.gridLayout.addWidget(self.tbSqlPort, 1, 1, 1, 1)

        self.lbSqlUser = QLabel(ConfigSQLConnection)
        self.lbSqlUser.setObjectName(u"lbSqlUser")

        self.gridLayout.addWidget(self.lbSqlUser, 2, 0, 1, 1)

        self.tbSqlUser = QLineEdit(ConfigSQLConnection)
        self.tbSqlUser.setObjectName(u"tbSqlUser")

        self.gridLayout.addWidget(self.tbSqlUser, 2, 1, 1, 1)

        self.lbSqlPw = QLabel(ConfigSQLConnection)
        self.lbSqlPw.setObjectName(u"lbSqlPw")

        self.gridLayout.addWidget(self.lbSqlPw, 3, 0, 1, 1)

        self.tbSqlPw = QLineEdit(ConfigSQLConnection)
        self.tbSqlPw.setObjectName(u"tbSqlPw")

        self.gridLayout.addWidget(self.tbSqlPw, 3, 1, 1, 1)

        self.lbSqlDb = QLabel(ConfigSQLConnection)
        self.lbSqlDb.setObjectName(u"lbSqlDb")

        self.gridLayout.addWidget(self.lbSqlDb, 4, 0, 1, 1)

        self.tbSqlDb = QLineEdit(ConfigSQLConnection)
        self.tbSqlDb.setObjectName(u"tbSqlDb")

        self.gridLayout.addWidget(self.tbSqlDb, 4, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.btSave = QPushButton(ConfigSQLConnection)
        self.btSave.setObjectName(u"btSave")
        self.btSave.setCursor(QCursor(Qt.ArrowCursor))

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.btSave)

        self.btCheck = QPushButton(ConfigSQLConnection)
        self.btCheck.setObjectName(u"btCheck")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.btCheck)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(2, QFormLayout.FieldRole, self.verticalSpacer)

        self.btClose = QPushButton(ConfigSQLConnection)
        self.btClose.setObjectName(u"btClose")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.btClose)


        self.gridLayout_2.addLayout(self.formLayout, 0, 1, 1, 1)


        self.retranslateUi(ConfigSQLConnection)

        QMetaObject.connectSlotsByName(ConfigSQLConnection)
    # setupUi

    def retranslateUi(self, ConfigSQLConnection):
        ConfigSQLConnection.setWindowTitle(QCoreApplication.translate("ConfigSQLConnection", u"Config SQL Connection", None))
        self.lbSqlIp.setText(QCoreApplication.translate("ConfigSQLConnection", u"SQL IP Adresse", None))
        self.lbSqlPort.setText(QCoreApplication.translate("ConfigSQLConnection", u"SQL Port", None))
        self.lbSqlUser.setText(QCoreApplication.translate("ConfigSQLConnection", u"SQL User", None))
        self.lbSqlPw.setText(QCoreApplication.translate("ConfigSQLConnection", u"SQL Password", None))
        self.lbSqlDb.setText(QCoreApplication.translate("ConfigSQLConnection", u"SQL Datenbank", None))
        self.btSave.setText(QCoreApplication.translate("ConfigSQLConnection", u"Save", None))
        self.btCheck.setText(QCoreApplication.translate("ConfigSQLConnection", u" Check Connection ", None))
        self.btClose.setText(QCoreApplication.translate("ConfigSQLConnection", u"Close", None))
    # retranslateUi

