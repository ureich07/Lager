# This Python file uses the following encoding: utf-8
import sys, os, datetime, locale, time

import pandas as pd
import webbrowser

from clsFunction import Function as clsFu
from clsSupportfunction import DataBase as clsDb
from clsSupportfunction import Support as clsSu
from clsSupportfunction import TableBase as clsTb

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QAbstractItemView
from PySide6.QtGui import  QValidator, QIcon, Qt#, QDoubleValidator, QIntValidator, QMouseEvent


from PySide6 import  QtCore, QtWidgets, QtGui

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from Lager_ui import Ui_MainWindow
from ConfigSqlConnection_ui import Ui_ConfigSQLConnection
from ArtikelErfassen_ui import Ui_ArtikelErfassen
from Kategorie_ui import Ui_Kategorie
import warnings

warnings.filterwarnings('ignore')


arIni = clsFu.fcReadIni("Lager.ini")
locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
sDate = datetime.date.today()
l_new = False
l_edit = False
l_delete = False
l_start = False
l_pwd = False
n_id = 0
n_anzahl = 0
s_password =""

conn = clsDb.fcConnectDb(arIni['user'],arIni['pw'], arIni['ip'], arIni['port'], arIni['db'])
cur = conn.cursor()
basedir = os.path.dirname(__file__)
#################################### Globale Funktionen ##################################################################
def prSetAgliment(value):
    item = QtWidgets.QTableWidgetItem(value) 
    item.setTextAlignment(Qt.AlignCenter)
    return item

#################################### Hilfs Funktionen ##################################################################                
class ConfigSQLConnection(QDialog, Ui_ConfigSQLConnection):
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__()
        self.setupUi(self)
        self.initConfigWindow()

    def initConfigWindow(self):
        a = clsFu.fcReadIni("Lager.ini")
        self.tbSqlIp.setText(a['ip'])
        self.tbSqlPort.setText(a['port'])
        self.tbSqlUser.setText(a['user'])
        self.tbSqlPw.setText(a['pw'])
        self.tbSqlDb.setText(a['db'])
        self.btCheck.pressed.connect(self.checkconnect)
        self.btClose.pressed.connect(self.close)
        self.btSave.pressed.connect(self.saveconfig)

    def saveconfig(self):
        clsFu.fcSaveIni_MariaDb("Lager.ini", self.tbSqlIp.text(), self.tbSqlPort.text(), self.tbSqlUser.text(), self.tbSqlPw.text(), self.tbSqlDb.text())

    def checkconnect(self):

        if clsDb.fcCheckServerStatus(self.tbSqlUser.text(),self.tbSqlPw.text(), self.tbSqlIp.text(), self.tbSqlPort.text(), self.tbSqlDb.text()):
            self.btCheck.setStyleSheet('background-color:green;color:#000000;')
        else:
            self.btCheck.setStyleSheet('background-color:red;color:#000000;')

class Kategorie(QDialog, Ui_Kategorie):
      
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__()
        self.setupUi(self)
        self.initConfigWindow()
        
    def initConfigWindow(self):
        self.twHaupt.currentCellChanged.connect(self.set_tbHaupt2)
        self.btAddHaupt.pressed.connect(self.prAddHaupt)
        self.btAddUnter.pressed.connect(self.prAddUnter)
        self.btAddLager.pressed.connect(self.prAddLager)
        self.btAddMarke.pressed.connect(self.prAddMarke)
        self.fill_table(conn, self.twHaupt, 'h_kategorie')
        self.fill_table(conn, self.twUnter, 'u_kategorie')
        self.fill_table(conn, self.twLager, 'lager')
        self.fill_table(conn, self.twMarke, 'marke')
    
    def set_tbHaupt2(self):
        index = self.twHaupt.currentIndex()
        if index.row()>=0:
            item = self.twHaupt.item(index.row(),0)
            name = item.data(QtCore.Qt.DisplayRole)
            self.tbHaupt2.setText(name)
            self.fill_table(conn, self.twUnter, 'u_kategorie')

    def prAddLager(self):
        if self.tbLager.text().strip() == '': return
        id = clsSu.get_time_id()
        fields = clsFu.strucktur_lager_marke_h_kategorie()
        value = clsFu.collect_value_lager_marke_h_kategorie(id, self.tbLager.text())
        try:
            if clsDb.insert_command(cur, 'lager', fields, value):
                conn.commit()
                self.fill_table(conn, self.twLager, 'lager')
                self.tbLager.setText('')
        except Exception as e:
            clsSu.error_file('save_lager', str(e))

    def prAddHaupt(self):
        if self.tbHaupt.text().strip() == '': return
        id = clsSu.get_time_id()
        fields = clsFu.strucktur_lager_marke_h_kategorie()
        value = clsFu.collect_value_lager_marke_h_kategorie(id, self.tbHaupt.text())
        try:
            if clsDb.insert_command(cur, 'h_kategorie', fields, value):
                conn.commit()
                self.fill_table(conn, self.twHaupt, 'h_kategorie')
                self.tbHaupt.setText('')
        except Exception as e:
            clsSu.error_file('save_h_kategorie', str(e))
    
    def prAddUnter(self):
        if self.tbHaupt2.text().strip() == '' or self.tbUnter.text().strip() == '': return
        id = clsSu.get_time_id()
        fields = clsFu.strucktur_u_kategorie()
        value = clsFu.collect_value_u_kategorie(id, self.tbHaupt2.text(), self.tbUnter.text())
        try:
            if clsDb.insert_command(cur, 'u_kategorie', fields, value):
                conn.commit()
                self.fill_table(conn, self.twUnter, 'u_kategorie')
                self.tbUnter.setText('')
        except Exception as e:
            clsSu.error_file('save_u_kategorie', str(e))

    def prAddMarke(self):
        if self.tbMarke.text().strip() == '': return
        id = clsSu.get_time_id()
        fields = clsFu.strucktur_lager_marke_h_kategorie()
        value = clsFu.collect_value_lager_marke_h_kategorie(id, self.tbMarke.text())
        try:
            if clsDb.insert_command(cur, 'marke', fields, value):
                conn.commit()
                self.fill_table(conn, self.twMarke, 'marke')
                self.tbMarke.setText('')
        except Exception as e:
            clsSu.error_file('save_marke', str(e))
    
    def fill_table(self, conn, model, table):
        """Tabelle Artikel füllen"""
        clsTb.remove_rows_tabelle(model)
        sql = "SELECT name, id FROM " + table + " Order by name asc"
        if table == 'u_kategorie':
            sql = "SELECT name, id FROM " + table + " Where kategorie='" + self.tbHaupt2.text() + "' Order by name asc"
        df = pd.read_sql_query(sql, conn)
        for row_number in df.index:
            model.insertRow(row_number)
            for i in range(0, 1):
                value= df.iloc[row_number][i]
                model.setItem(row_number,i, QtWidgets.QTableWidgetItem(value)) 
                       
        model.setColumnWidth(0,190)
        model.hideColumn(1)
        model.sortItems(0, QtCore.Qt.AscendingOrder)
        model.selectRow(0)

class ArtikelErfassen(QDialog, Ui_ArtikelErfassen):
      
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__()
        self.setupUi(self)
        self.initConfigWindow()
        
    def initConfigWindow(self):
        self.setTableAnzahl()
        self.prRefresh()
        self.coHaupt.currentTextChanged.connect(self.fillcoUnter)
        self.btSpeichern.setEnabled(False)
        self.btSpeichern.pressed.connect(self.prSpeichern)
        self.chCodeCheck.stateChanged.connect(self.onStateChanged)
        self.tbDatum.setInputMask("99.99.9999")
        self.tbDatum.editingFinished.connect(self.prCheckDatum)
        self.tbBarcode.editingFinished.connect(self.prCheckBarcode)
        self.tbAnzahl.editingFinished.connect(self.prEnableSpeichern)
        self.tbBarcode.installEventFilter(self)
        self.tbBarcode.setFocus()
        
    def onStateChanged(self):
        if self.tbBarcode.text().strip() == '': return
        if self.chCodeCheck.isChecked():
            self.prCodeCheck()
        
    def prRefresh(self):
        self.fillCombobox(conn, self.coMarke, 'marke')
        self.fillCombobox(conn, self.coLager, 'lager')
        self.fillCombobox(conn, self.coHaupt, 'h_kategorie')
        self.fillCombobox(conn, self.coUnter, 'u_kategorie')
    
    def prEnableSpeichern(self):
        if self.tbName.text().strip() == '': return
        if self.tbBarcode.text().strip() == '': return
        if self.tbAnzahl.text().strip() == '': return
        if not self.prCheckDatum(): return
        self.btSpeichern.setEnabled(True)
        
    def prSpeichern(self):
        if self.tbName.text().strip() == '': return
        if self.tbBarcode.text().strip() == '': return
        if self.tbAnzahl.text().strip() == '': return
        self.prCheckCoBox(self.coMarke, "marke")
        self.prCheckCoBox(self.coHaupt, "h_kategorie")
        self.prCheckCoBox(self.coUnter, "u_kategorie")
        self.prCheckCoBox(self.coLager, "lager")
        if self.prCheckDatum():
            if l_new:
                self.prSaveArtikel()
            else:
                self.prUpdateArtikel()
            self.prSaveBuchung()
            self.prClearFelder()
            self.tbBarcode.setFocus()
    
    def prCheckCoBox(self, model, table):
        sql = "SELECT name, id FROM " + table + " Where name='" + model.currentText() + "'"
        if table == 'u_kategorie':
            sql = "SELECT name, id FROM " + table + " Where kategorie='" + self.coHaupt.currentText() + "' and name='" + model.currentText() + "'"
        row =clsDb.get_number_of_row(cur, sql)
        if row <= 0:
            id = clsSu.get_time_id()
            fields = clsFu.strucktur_lager_marke_h_kategorie()
            value = clsFu.collect_value_lager_marke_h_kategorie(id, model.currentText())
            if table == 'u_kategorie':
                fields = clsFu.strucktur_u_kategorie()
                value = clsFu.collect_value_u_kategorie(id, self.coHaupt.currentText(), model.currentText())
            try:
                if clsDb.insert_command(cur, table, fields, value):
                    conn.commit()
                    model.addItem(model.currentText())
            except Exception as e:
                clsSu.error_file('save_marke', str(e))
    
    def prCheckDatum(self):
        if clsSu.checkDate(self.tbDatum.text()):
            self.tbDatum.setStyleSheet("color: black;  background-color: white")
            return True
        else:
            self.tbDatum.setFocus()
            self.tbDatum.setStyleSheet("color: white;  background-color: read")
            return False
    
    def prCodeCheck(self):
        url = "https://fddb.info/db/de/suche/?udd=0&cat=site-de&search=" + self.tbBarcode.text()
        webbrowser.open(url)
       
    def prCheckBarcode(self):
        if self.chCodeCheck.isChecked(): self.prCodeCheck()
        s_barcode = self.tbBarcode.text().strip().replace("\n","")
        global l_new; l_new = True
        sql = "SELECT * FROM artikel Where barcode='" + s_barcode + "'"
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchall()
        if len(row) > 0:
            value = row[0]
            l_new = False
            self.prfillFormular(value)
            self.tbDatum.setFocus()
            self.tbDatum.setCursorPosition(0)
            self.enable_felder('Edit',True)
            self.prEnableEmptyFelder()
        else:
            global n_anzahl; n_anzahl = 0
            self.prClearFelder()
            self.tbBarcode.setText(s_barcode)
            self.tbName.setFocus()
            self.enable_felder('New',True)
        self.fill_table_anzahl(conn, self.twListe)
        global l_start; l_start = True
     
    def enable_felder(self, art, status):
        self.tbName.setReadOnly(not status)
        self.coMarke.setEnabled(status)
        self.coHaupt.setEnabled(status)
        self.coUnter.setEnabled(status)
        self.tbGroesse.setReadOnly(not status)
        self.coEinheit.setEnabled(status)
        self.coLager.setEnabled(status)
        self.tbBrennwert.setReadOnly(not status)
        self.tbKalorien.setReadOnly(not status)
        self.tbProtein.setReadOnly(not status)
        self.tbFett.setReadOnly(not status)
        self.tbKohle.setReadOnly(not status)
        self.tbZucker.setReadOnly(not status)
        
        if art == 'Edit':
            self.tbName.setReadOnly(status)
            self.coMarke.setEnabled(not status)
            self.coHaupt.setEnabled(not status)
            self.coUnter.setEnabled(not status)
            self.tbGroesse.setReadOnly(status)
            self.coEinheit.setEnabled(not status)
            self.tbBrennwert.setReadOnly(status)
            self.tbKalorien.setReadOnly(status)
            self.tbProtein.setReadOnly(status)
            self.tbFett.setReadOnly(status)
            self.tbKohle.setReadOnly(status)
            self.tbZucker.setReadOnly(status)
       
    def prfillFormular(self, value):
        global n_id; n_id = value[0]
        global n_anzahl; n_anzahl = value[6]
        self.tbName.setText(value[1])
        self.coHaupt.setCurrentText(value[2])
        self.coUnter.setCurrentText(value[3])
        self.coMarke.setCurrentText(value[4])
        self.tbAnzahl.setText('') 
        self.tbSoll.setText(value[7]) 
        self.tbGroesse.setText(value[8]) 
        self.coEinheit.setCurrentText(value[9])
        self.tbDatum.setText('') 
        self.tbBrennwert.setText(value[10]) 
        self.tbKalorien.setText(value[11]) 
        self.tbProtein.setText(value[12]) 
        self.tbFett.setText(value[13]) 
        self.tbKohle.setText(value[14]) 
        self.tbZucker.setText(value[15]) 
        self.tbPreis.setText(value[16]) 
        
        
        self.coLager.setCurrentText('')
    
    def prEnableEmptyFelder(self):
        if self.tbGroesse.text().strip() == '': self.tbGroesse.setReadOnly(False)
        if self.tbBrennwert.text().strip() == '': self.tbBrennwert.setReadOnly(False)
        if self.tbKalorien.text().strip() == '': self.tbKalorien.setReadOnly(False)
        if self.tbProtein.text().strip() == '': self.tbProtein.setReadOnly(False)
        if self.tbFett.text().strip() == '': self.tbFett.setReadOnly(False)
        if self.tbKohle.text().strip() == '': self.tbKohle.setReadOnly(False)
        if self.tbZucker.text().strip() == '': self.tbZucker.setReadOnly(False)
    
    def prClearFelder(self):
        self.tbBarcode.setText('') 
        self.tbName.setText('') 
        self.tbPreis.setText('') 
        self.tbGroesse.setText('') 
        self.tbDatum.setText('') 
        self.tbPreis.setText('') 
        self.tbAnzahl.setText('') 
        self.tbSoll.setText('') 
        self.tbBrennwert.setText('') 
        self.tbKalorien.setText('') 
        self.tbProtein.setText('') 
        self.tbFett.setText('') 
        self.tbKohle.setText('') 
        self.tbZucker.setText('') 
        self.coMarke.setCurrentIndex(0)
        self.coHaupt.setCurrentIndex(0)
        self.coUnter.setCurrentIndex(0)
        self.coLager.setCurrentIndex(0)
        self.coEinheit.setCurrentIndex(0)
        
    def prSaveArtikel(self):
        global l_start; l_start = False
        id = clsSu.get_time_id()
        fields = clsFu.strucktur_artikel()
        value = self.collect_value_artikel(id)
        try:
            if clsDb.insert_command(cur, 'artikel', fields, value):
                conn.commit()
        except Exception as e:
            clsSu.error_file('save_artikel', str(e))
    
    def prUpdateArtikel(self):
        global l_start; l_start = False
        fields = clsFu.strucktur_artikel()
        value = self.collect_value_artikel(n_id)
        try:
            if clsDb.update_command(cur, 'artikel', fields, value, n_id):
                conn.commit()
        except Exception as e:
            clsSu.error_file('save_artikel', str(e))
    
    def prSaveBuchung(self):
        time.sleep(1)
        id = clsSu.get_time_id()
        fields = clsFu.strucktur_buchung()
        value = self.collect_value_buchnung(id)
        try:
            if clsDb.insert_command(cur, 'buchung', fields, value):
                conn.commit()
        except Exception as e:
            clsSu.error_file('save_buchung', str(e))
    
    def collect_value_artikel(self, id):
        n_anz = int(n_anzahl) + int(self.tbAnzahl.text())
        value =  [id, self.tbName.text(), self.coHaupt.currentText(), self.coUnter.currentText(), self.coMarke.currentText(), self.tbBarcode.text(),
                  str(n_anz), self.tbSoll.text(), self.tbGroesse.text(), self.coEinheit.currentText(), self.tbBrennwert.text(), 
                  self.tbKalorien.text(), self.tbProtein.text(), self.tbKohle.text(), self.tbZucker.text(), self.tbFett.text(), self.tbPreis.text()]  
        return value    
        
    def collect_value_buchnung(self, id):
        value =  [id, self.tbBarcode.text(), self.coLager.currentText(), self.tbDatum.text(), self.tbName.text() ,self.tbPreis.text(),  self.tbAnzahl.text()]  
        return value
        
    def fillcoUnter(self):
        self.fillCombobox(conn, self.coUnter, 'u_kategorie')
    
    def fillCombobox(self, conn, model, table):
        """Combobox füllen"""
        model.clear()
        sql = "SELECT name, id FROM " + table + " Order by name asc"
        if table == 'u_kategorie':
            sql = "SELECT name, id FROM " + table + " Where kategorie='" + self.coHaupt.currentText() + "' Order by name asc"
        df = pd.read_sql_query(sql, conn)
        for row_number in df.index:
            for i in range(0, 1):
                value= df.iloc[row_number][i]
                model.addItem(value)
    
    def fill_table_anzahl(self, conn, model):
        """Tabelle Anzahl füllen"""
        clsTb.remove_rows_tabelle(model)
        sql = "SELECT datum, anzahl, preis, id FROM buchung Where barcode='" + self.tbBarcode.text() + "' Order by name asc"
        df = pd.read_sql_query(sql, conn)
        for row_number in df.index:
            model.insertRow(row_number)
            for i in range(0, 4):
                value= df.iloc[row_number][i]
                model.setItem(row_number,i, prSetAgliment(value))
                
               
    def setTableAnzahl(self):
        self.twListe.setColumnWidth(0,80)
        self.twListe.setColumnWidth(1,50)
        self.twListe.setColumnWidth(2,80)
        self.twListe.setColumnWidth(3,0)
        self.twListe.hideColumn(3)
        self.twListe.sortItems(0, QtCore.Qt.AscendingOrder)
        self.twListe.selectRow(0)
        
class MainWindow(QMainWindow, Ui_MainWindow):
    """Main window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__()
        self.setupUi(self)
        self.initMainWindow()

    def initMainWindow(self):
        self.resize(1200,700)
        self.btConfig.setIcon(QIcon(os.path.join(basedir, "Resources/sql.png")))
        self.btConfig.triggered.connect(self.settings)
        self.btErfassen.triggered.connect(self.prErfassen)
        self.btBearbeiten.triggered.connect(self.prKategorie)
        self.prRefresh()
        
     
        
        """Artikel"""
        row =clsDb.get_number_of_row(cur, "SELECT * FROM artikel")
        self.no_record(row)
        
        self.twArtikel.horizontalHeader().setStretchLastSection(True)
        self.twArtikel.setAlternatingRowColors(True)
        self.twArtikel.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.fill_table_artikel()
        self.coHaupt.currentIndexChanged.connect(self.fill_table_artikel)
        self.coHaupt.currentTextChanged.connect(self.fillcoUnter)
        self.coUnter.currentIndexChanged.connect(self.fill_table_artikel)
        self.coLager.currentIndexChanged.connect(self.fill_table_artikel)
        self.btGn.triggered.connect(self.fill_table_artikel)
        self.btGe.triggered.connect(self.fill_table_artikel)
        self.btRo.triggered.connect(self.fill_table_artikel)

    def fillcoUnter(self):
        self.fillCombobox(conn, self.coUnter, 'u_kategorie')
    
    def fillCombobox(self, conn, model, table):
        """Combobox füllen"""
        model.clear()
        sql = "SELECT name, id FROM " + table + " Order by name asc"
        if table == 'u_kategorie':
            sql = "SELECT name, id FROM " + table + " Where kategorie='" + self.coHaupt.currentText() + "' Order by name asc"
        df = pd.read_sql_query(sql, conn)
        model.addItem('Alles')
        for row_number in df.index:
            for i in range(0, 1):
                value= df.iloc[row_number][i]
                model.addItem(value)

    def prRefresh(self):
        self.fillCombobox(conn, self.coLager, 'lager')
        self.fillCombobox(conn, self.coHaupt, 'h_kategorie')
        self.fillCombobox(conn, self.coUnter, 'u_kategorie')
                    
    def fill_table_artikel(self):
        model =  self.twArtikel
        haupt = self.coHaupt.currentText()
        unter = self.coUnter.currentText()
        lager = self.coLager.currentText()
        """Tabelle Artikel füllen"""
        clsTb.remove_rows_tabelle(model)
        sql = "SELECT * FROM artikel Order by name asc"
        df = pd.read_sql_query(sql, conn)
        i = 0
        for row_number in df.index:
            s_id= df.iloc[row_number][0]
            s_name= df.iloc[row_number][1]
            s_haupt= df.iloc[row_number][2]
            s_unter= df.iloc[row_number][3]
            s_marke= df.iloc[row_number][4]
            s_barcode= df.iloc[row_number][5]
            s_anzahl= df.iloc[row_number][6]
            if (haupt == s_haupt and unter == s_unter) or (haupt == "Alles" and unter == "Alles") or (haupt == s_haupt and unter == "Alles"):
                model.insertRow(i)
                model.setItem(i,0, QtWidgets.QTableWidgetItem(s_name)) 
                model.setItem(i,1, QtWidgets.QTableWidgetItem(s_marke)) 
                model.setItem(i,2, prSetAgliment(s_anzahl)) 
                model.setItem(i,3, QtWidgets.QTableWidgetItem('')) 
                model.setItem(i,4, QtWidgets.QTableWidgetItem(''))
                model.setItem(i,5, QtWidgets.QTableWidgetItem(s_haupt)) 
                model.setItem(i,6, QtWidgets.QTableWidgetItem(s_unter)) 
                model.setItem(i,7, QtWidgets.QTableWidgetItem(s_id)) 
                model.setItem(i,8, QtWidgets.QTableWidgetItem(s_barcode)) 
                self.set_color(model, i)
                i = i + 1
                sql1 = "SELECT * FROM buchung Where barcode='" + s_barcode + "'"
                df1 = pd.read_sql_query(sql1, conn)
                for row_number1 in df1.index:
                    s_id= df1.iloc[row_number1][0]
                    s_lager= df1.iloc[row_number1][2]
                    s_datum= df1.iloc[row_number1][3]
                    s_anzahl= df1.iloc[row_number1][6]
                    days = clsSu.get_time_diff(s_datum)
                    if self.check_ampel(days):
                        if (lager == s_lager or lager == "Alles"):
                            model.insertRow(i)
                            model.setItem(i,0, QtWidgets.QTableWidgetItem('')) 
                            model.setItem(i,1, QtWidgets.QTableWidgetItem('')) 
                            model.setItem(i,2, prSetAgliment(s_anzahl))
                            model.setItem(i,3, prSetAgliment(s_datum))
                            model.setItem(i,4, QtWidgets.QTableWidgetItem(s_lager))
                            model.setItem(i,5, QtWidgets.QTableWidgetItem('')) 
                            model.setItem(i,6, QtWidgets.QTableWidgetItem('')) 
                            model.setItem(i,7, QtWidgets.QTableWidgetItem(s_id)) 
                            model.setItem(i,8, QtWidgets.QTableWidgetItem(s_barcode)) 
                            self.set_color_ablaufdatum(model, i, days)
                            i = i + 1
                        
        model.setColumnWidth(0,300)
        model.setColumnWidth(1,200)
        model.setColumnWidth(2,50)
        model.setColumnWidth(3,100)
        model.setColumnWidth(4,130)
        model.setColumnWidth(5,0)
        model.hideColumn(5)
        model.hideColumn(6)
        model.hideColumn(7)
        model.hideColumn(8)
        model.selectRow(0)

    def check_ampel(self, n_diff):
        l_display = False
        if n_diff < 0:
            if self.btRo.isChecked(): l_display = True
        elif n_diff < 30:
            if self.btGe.isChecked(): l_display = True
        else: 
            if self.btGn.isChecked(): l_display = True
        return l_display
            
    def set_color_ablaufdatum(self, model,i, n_diff):
        color = "white"
        if n_diff < 0:
            color = "red"
        elif n_diff < 30:
            color = "yellow"
        for x in range(0, 5):
            model.item(i,x).setBackground(QtGui.QColor(color))
    
    def set_color(self, model,i):
        for x in range(0, 5):
            model.item(i,x).setBackground(QtGui.QColor('skyblue'))
                        
    def no_record(self, row) :
        if row <= 0:
            self.btBearbeiten.setEnabled(False)
            self.btErfassen.setEnabled(True)
        else:
            self.btBearbeiten.setEnabled(True)
            self.btErfassen.setEnabled(True)
    
    def settings(self):
        """Dialog Konfiguration SQL Verbindung"""
        self.w = ConfigSQLConnection()
        self.w.show()
        
    def prErfassen(self):
        self.w = ArtikelErfassen()
        self.w.show()
        
    def prKategorie(self):
        self.w = Kategorie()
        self.w.show()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()

