#!/usr/
import configparser
import mariadb
import os
from pathlib import Path
from clsSupportfunction import Support as clsSu

class Function():
    
    def fcSaveIni_MariaDb(sIniFile, ip, port, user, pw, db):
        import configparser
        path = Path(__file__)
        ROOT_DIR = path.parent.absolute()
        config_path = os.path.join(ROOT_DIR, sIniFile)

        config = configparser.ConfigParser()
        config.read(config_path)
        config.set('mariadb', 'ip', str(ip))
        config.set('mariadb', 'port', str(port))
        config.set('mariadb', 'user', str(user))
        config.set('mariadb', 'pw', str(pw))
        config.set('mariadb', 'db', str(db))
        with open(config_path, 'w') as configfile:
            config.write(configfile)
    
    def fcReadIni(sIniFile):
   
        a = dict()
        try:
            import configparser
            path = Path(__file__)
            ROOT_DIR = path.parent.absolute()
            config_path = os.path.join(ROOT_DIR, sIniFile)
            print(config_path)
            config = configparser.ConfigParser()
            config.read(config_path)
            
            a['ip'] = config.get('mariadb', 'ip')
            a['port'] = config.get('mariadb', 'port')
            a['user'] = config.get('mariadb', 'user')
            a['pw'] = config.get('mariadb', 'pw')
            a['db'] = config.get('mariadb', 'db')

        except Exception as e:
            clsSu.error_file('fcReadIni', e)
        return a
    
    def strucktur_lager_marke_h_kategorie():
        fields = ['id',  'name']
        return fields
    
    def strucktur_u_kategorie():
        fields = ['id',  'kategorie', 'name']
        return fields
    
    def strucktur_artikel():
        fields =  ['id', 'name', 'h_kategorie', 'u_kategorie', 'marke', 'barcode', 'anzahl', 'soll', 'gewicht', 
                   'einheit', 'brennwert', 'kalorien', 'protein', 'kohlehydrate', 'zucker', 'fett', 'preis']
        return fields

    def strucktur_buchung():
        fields =  ['id', 'barcode', 'lager', 'datum', 'name', 'preis', 'anzahl']
        return fields

    def strucktur_history():
        fields =  ['id', 'barcode', 'name', 'datum', 'preis', 'anzahl']
        return fields
    
    
    def save_tabelle(pd, sql, conn, tabelle):
        df = pd.read_sql_query(sql, conn)
        values = '<' + tabelle + '>\n'
        for row_number in df.index:
            count = df.iloc[row_number].count() 
            values += "'"
            value = ''
            for i in range(0, count):
                wert = df.iloc[row_number][i]
                value = value +  str(wert) + "';'"
            values = values + value + '\n'
        values += '<End>\n'
        return values
    
    
    def collect_value_lager_marke_h_kategorie(id, eintrag):
        value =  [id, eintrag]    
        return value
    
    def collect_value_u_kategorie(id, haupt, unter):
        value =  [id, haupt, unter]    
        return value


