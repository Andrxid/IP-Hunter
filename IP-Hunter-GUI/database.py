import sqlite3
import netaddr
from netaddr import *
#from ipaddress import IPv4Address, IPv6Address, IPv4Network, IPv6Network, ip_address

#--------------FUNZIONE PER RIEMPIRE LA TABELA PRIVATE IP CON QUERY SQL---------------------------
def database_private_ip(self):
    from definitico import Ui_IPSEARCH_window, QtWidgets
    connection = sqlite3.connect('IpHunter.db')
    query = '''
            SELECT
            ip.ip_address    
            , nmap.port       
            , nmap.name       
            , nmap.protocol   
            , nmap.state            
            , nmap.product    
            , ip.mac_address  
            , ip.vendor       
            , nmap.extrainfo  
            , nmap.reason     
            , nmap.version    
            , nmap.conf       
            , nmap.cpe        
            , ip.scan_data    
            , ip.scan_username 
            FROM
            private_ip ip
            
            CROSS JOIN
            
            nmap_output nmap
            ON
            ip.ip_address = nmap.host
            
    '''
    result = connection.execute(query)
    self.tableWidget_private_ip.setRowCount(0)
    for row_number,result in enumerate (result):
            self.tableWidget_private_ip.insertRow(row_number)
            for collum_number,data in enumerate (result):
                    cell= QtWidgets.QTableWidgetItem(str(data))
                    self.tableWidget_private_ip.setItem(row_number,collum_number,cell)

#--------------FUNZIONE PER RIEMPIRE LA TABELA PUBLIC IP CON QUERY SQL---------------------------

def database_public_ip(self):
    from definitico import Ui_IPSEARCH_window, QtWidgets
    connection = sqlite3.connect('IpHunter.db')
    query = """
            SELECT
            ip.ip_address    
            , nmap.port       
            , nmap.name       
            , nmap.protocol   
            , nmap.state            
            , nmap.product          
            , nmap.extrainfo  
            , nmap.reason     
            , nmap.version    
            , nmap.conf       
            , nmap.cpe        
            , ip.scan_data    
            , ip.scan_username
            FROM
            public_ip ip
            
            CROSS JOIN
            
            nmap_output nmap
            ON
            ip.ip_address = nmap.host
            
    
    """
    result = connection.execute(query)
    self.tableWidget_public_ip.setRowCount(0)
    for row_number,result in enumerate (result):
            self.tableWidget_public_ip.insertRow(row_number)
            for collum_number,data in enumerate (result):
                    cell= QtWidgets.QTableWidgetItem(str(data))
                    self.tableWidget_public_ip.setItem(row_number,collum_number,cell)

#--------------FUNZIONE DI RICERC IP PER RIEMPIRE LA TABELA CON RISULTATI IP SELEZIONATI CON QUERY SQL---------------------------

def search_db_tool(self):
    from definitico import Ui_IPSEARCH_window, QtWidgets
    try:
        
        getvar = self.Search_bar.text()
        if IPAddress(getvar).is_private():

            with sqlite3.connect("IpHunter.db") as db:
                c = db.cursor()
            ## find_ip = ("SELECT * FROM private_ip WHERE ip_address = ?")
            find_ip = ('''
                SELECT
                ip.ip_address    
            , nmap.port       
            , nmap.name       
            , nmap.protocol   
            , nmap.state            
            , nmap.product    
            , ip.mac_address  
            , ip.vendor       
            , nmap.extrainfo  
            , nmap.reason     
            , nmap.version    
            , nmap.conf       
            , nmap.cpe        
            , ip.scan_data    
            , ip.scan_username 
            FROM
            private_ip ip
            
            CROSS JOIN
            
            nmap_output nmap
            ON
            ip.ip_address = nmap.host
            WHERE ip_address = ?
            ''')              
            c.execute(find_ip, [(getvar)])
            results = c.fetchall()
            self.tableWidget_private_ip.setRowCount(0)
            for row_number,result in enumerate (results):
                    self.tableWidget_private_ip.insertRow(row_number)
                    for collum_number,data in enumerate (result):
                            cell= QtWidgets.QTableWidgetItem(str(data))
                            self.tableWidget_private_ip.setItem(row_number,collum_number,cell)
            self.stackedWidget.setCurrentWidget(self.PAGE_DATABASE_private_IP)
        else:

            with sqlite3.connect("IpHunter.db") as db:
                c = db.cursor()
            ## find_ip = ("SELECT * FROM private_ip WHERE ip_address = ?")
            find_ip = ('''
            SELECT
            ip.ip_address    
        , nmap.port       
        , nmap.name       
        , nmap.protocol   
        , nmap.state            
        , nmap.product          
        , nmap.extrainfo  
        , nmap.reason     
        , nmap.version    
        , nmap.conf       
        , nmap.cpe        
        , ip.scan_data    
        , ip.scan_username
        FROM
        public_ip ip
        
        CROSS JOIN
        
        nmap_output nmap
        ON
        ip.ip_address = nmap.host
        WHERE ip_address = ?
            ''')              
            c.execute(find_ip, [(getvar)])
            results = c.fetchall()
            self.tableWidget_public_ip.setRowCount(0)
            for row_number,result in enumerate (results):
                    self.tableWidget_public_ip.insertRow(row_number)
                    for collum_number,data in enumerate (result):
                            cell= QtWidgets.QTableWidgetItem(str(data))
                            self.tableWidget_public_ip.setItem(row_number,collum_number,cell)
            self.stackedWidget.setCurrentWidget(self.PAGE_DATABASE_Public_IP)
            
    except netaddr.core.AddrFormatError:
            pass
            
#--------------CREAZIONE DEL DATABASE IP HUNTER------------------------------------
def IP_DB():
    with sqlite3.connect("IpHunter.db") as db:                # creazione di un database                                                         
        c = db.cursor()                                         # username, password, email, data di registrazione e data ultimo accesso
    c.execute("""
    CREATE TABLE IF NOT EXISTS private_ip(
    ip_address TEXT PRIMARY KEY NOT NULL, 
    client TEXT , 
    mac_address TEXT , 
    vendor TEXT, 
    scan_data DATETIME DEFAULT CURRENT_TIMESTAMP, 
    scan_username TEXT, 
    UNIQUE(ip_address) ON CONFLICT REPLACE);
    """)
    c.execute("""
    CREATE TABLE IF NOT EXISTS public_ip(
    ip_address TEXT PRIMARY KEY NOT NULL, 
    scan_data DATETIME DEFAULT CURRENT_TIMESTAMP, 
    scan_username TEXT, 
    UNIQUE(ip_address) ON CONFLICT REPLACE);
    """)
    c.execute("""
    CREATE TABLE IF NOT EXISTS nmap_output(
    host TEXT, 
    port INTEGER, 
    name TEXT, 
    hostname TEXT, 
    hostname_type TEXT, 
    protocol TEXT, 
    state TEXT, 
    product TEXT, 
    extrainfo REAL, 
    reason TEXT, 
    version REAL, 
    conf INTEGER, 
    cpe TEXT, 
    scan_data DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY(host, port, name) ON CONFLICT REPLACE);
    """)
    c.execute("""
    CREATE TABLE IF NOT EXISTS user_cred(
    username TEXT NOT NULL, 
    email TEXT PRIMARY KEY NOT NULL, 
    password VARCHAR(20) NOT NULL, 
    reg_data DATETIME DEFAULT CURRENT_TIMESTAMP, 
    last_access TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    settings TEXT)  
    """)
    
    db.commit()