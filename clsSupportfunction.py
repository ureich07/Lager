import sys, os
import datetime #import datetime

import mariadb
import configparser
from PySide6.QtWidgets import QMessageBox

#################################### Ini-Datei Funktionen ##################################################################
class IniFile():
    def fcOpenIniFile(sFile):
        config = configparser.ConfigParser()
        config.read(sFile)
        try:
            config.add_section("SETTINGS")
        except configparser.DuplicateSectionError:
            pass

        return config

    def prWriteConfig(config, Entry, Value):
        config.set("SETTINGS", Entry, Value)

    def prSaveIniFile(config, sFile):
        with open(sFile, "w") as config_file:
            config.write(config_file)

    def fcReadConfig(config, key):
        try:
            value = config.get("SETTINGS", key)
        except configparser.DuplicateSectionError:
            value = ''
        return value

#################################### Datenbank Funktionen ##################################################################
class DataBase():
    def fcConnectDb(user1, password1, host1 , port1, database1):
        """ Connect to MariaDB Platform """
        try:
            conn = mariadb.connect(
                user=user1,
                password=password1,
                host=host1,
                port=int(port1),
                database=database1
            )
        
        except mariadb.Error as e:
            Support.error_file('connect_db', e)
            
        return conn

    def fcCheckServerStatus(user1, password1, host1 , port1, database1):
        try:
            mariadb.connect(user=user1, password=password1,	host=host1,	port=int(port1), database=database1)
            status = True
        except:
            status = False
        return status  
    
    def get_number_of_row(cur, sql):
        cur.execute(sql)
        row = cur.fetchall()
        return (len(row))
    
    def insert_command(cur, table, fields, value):
        #print(table, fields, value)
        status = False
        try:
            if len(fields) == len(value):
                s_fields = ','.join(fields)
                s_value ='?'
                for i in range (0, len(fields)-1):
                    s_value = s_value + ',?'
                sql = "INSERT INTO " + table + " (" + s_fields + ") VALUES (" + s_value + ")"
                #print(sql)
                cur.execute(sql, value )
                status = True
            else:
                Support.error_file('insert_command','Array fields und value sind unterschiedlich lang => ' + str(len(fields)) + ', ' + str(len(value)))
        except Exception as e:
            Support.error_file('insert_command', str(e))
        return status
    
    def update_command(cur, table, fields, value, id):
        """
        Update Tabelle
        1. Wert in der Tabelle ist die 'id' """
        #print(table, fields, value)
        status = False
        try:
            if len(fields) == len(value):
                ar_value = []
                """id nicht mit einbeziehen, start bei 1 und nicht bei 0"""
                for i in range (1, len(fields)):
                    ar_value.append(fields[i] + " = '" + value[i] + "'")
                s_value = ','.join(ar_value)
                sql = "UPDATE " + table + " SET " + s_value + " WHERE id = '" + id + "'"
                #print(sql)
                cur.execute(sql, value )
                status = True
            else:
                Support.error_file('insert_command','Array fields und value sind unterschiedlich lang => ' + str(len(fields)) + ', ' + str(len(value)))
        except Exception as e:
            Support.error_file('update_command', str(e))
        return status
    
    
    
#################################### Table Funktionen ##################################################################
class TableBase():  
    """Funktionen für die Tabellen"""  
    def remove_rows_tabelle(model):
        """Alle Einträge aus der Tabelle löschen"""
        for row in reversed(range(model.rowCount())):
            model.removeRow(row)        

    
#################################### Hilfs Funktionen ##################################################################
class Support():
    
    def msgbox_ok(titel, info, icon):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(info)
        msg.setWindowTitle(titel)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def msgbox_ok_cancel(titel, info, icon):
        button ='Cancel'
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(info)
        msg.setWindowTitle(titel)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
        if retval == 1024:
            button ='OK'
        return button
    
    def is_element_in_dictionary(Dict, sElement):
        try:
            lFound = True
            Found = str(Dict).find("('" + sElement + "'")
            if Found == -1: lFound = False
        except Exception:
            lFound = False
        return lFound

    def get_time_id():
        """eindeueutigen Schlüssel erzeugen als Datensatzzeiger"""
        stime = datetime.datetime.now()
        return stime.strftime("%Y%m%d%H%M%S")
        
    def convert_datum(dateString):
        """Datumsumwandlung, 01.09.2008 > 20080901) und (20080901 > 01.09.2008)"""
        if '.' in dateString or  '/' in dateString:
            if '.' in dateString:
                dateTimeObj = datetime.datetime.strptime(dateString, "%d.%m.%Y")
            if '/' in dateString:
                dateTimeObj = datetime.datetime.strptime(dateString, "%d/%m/%Y")
            return dateTimeObj.strftime("%Y%m%d")
        else:
            return dateString[6:8] + '.' + dateString[4:6] + '.' + dateString[0:4]
        
    def get_time_stamp():
        stime = datetime.datetime.now()
        return stime.strftime("%Y%m%d-%H%M%S")
    
    def checkDate(sdate):
        try:
            dateTimeObj = datetime.datetime.strptime(sdate, "%d.%m.%Y")
            datetime.date(dateTimeObj.year,dateTimeObj.month,dateTimeObj.day)
            return True
        except ValueError:
            return False
    
    def get_time_diff(end_day):
        """ 
        Ermittelt die Differenz zwischen übergebenen Datum und aktuellen Datum in Tage
        
        :param end_day: Datum
        :return:        Tage
        """
        stime = Support.convert_datum(end_day)
        end_day = Support.convert_datum(stime)
        t = str(end_day).split('.')
        end_day = t[0] + "." + t[1] + "." + t[2]
        
        present_day = datetime.datetime.now()
        stime = str(present_day).split(' ')
        t = str(stime[0]).split('-')
        present_day = t[2] + "." + t[1] + "." + t[0]
        
        a = datetime.datetime.strptime(present_day, '%d.%m.%Y')
        b = datetime.datetime.strptime(end_day, '%d.%m.%Y')
        return (a-b).days   
    
    def error_file(sModule, sError):
        """

        :param sModule:
        :param sError:
        :return:
        """
        sFile = os.path.abspath(os.getcwd()) + '/ErrorLog.txt'
        sTime = Support.get_time_stamp()
        f = open(sFile, 'a')
        f.write(sTime + ': ' + sModule + ' =>  - %s' % sError + '\n')
        f.close()
    
    def save_file(sFile, sValue, sAtt):
        """

        :param sModule:
        :param sError:
        :return:
        """
        sFile = os.path.abspath(os.getcwd()) + '/' + sFile
        f = open(sFile, sAtt)
        f.write(sValue)
        f.close()