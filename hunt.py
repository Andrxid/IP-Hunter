

#-----IMPORT NECESSARI
from csv import Dialect

from pprint import pp
from netaddr import *

from ipaddress import IPv4Address, IPv6Address, IPv4Network, IPv6Network, ip_address
import json
from pandas import test
import requests
from ipwhois import IPWhois

import socket
from getmac import get_mac_address
import sqlite3
import urllib.request as urllib2
import codecs
import nmap
import csv
import pandas as pd
import os
from os import path





#-------------FUNZIONE PER LO SCAN DI NMAP------------------------------
def scan(self):
    import definitico
     
    getvar = self.Type_an_IP_AddressIPHUNTER.text()
    nm = nmap.PortScanner()
    
    self.info = nm.scan(getvar, '80-443')
    
    global datcsv
    datcsv = nm.csv()
    self.formattedinfo = json.dumps(self.info, indent=2)
    self.label_5.setText(self.formattedinfo)

    save_csv_data(datcsv)
    print(datcsv)
    f = open("Temporary/results.txt", "a")
    f.write("\n************************** NMAP SCAN *******************************")
    f.write(str(self.formattedinfo))    

#-------------FUNZIONE PER INSERIMENTO DATI IP PUBBLICO----------------
def insert_publicdata(self):
    import sign_in
    import definitico
    getvar = self.Type_an_IP_AddressIPHUNTER.text()

    with sqlite3.connect("IpHunter.db") as db:                # creazione di un database                                                         
        c = db.cursor() 
    add_data = ('INSERT INTO public_ip(ip_address,  scan_data, scan_username ) VALUES (?,  datetime(), ?)')    
    data = [(getvar), (sign_in.mail)]
    c.execute(add_data, data) 
    db.commit()
    
    conn = sqlite3.connect('IpHunter.db')
    c = conn.cursor()
     
    users = pd.read_csv('output2.csv')
    users.to_sql('nmap_output', conn, if_exists='append', index = False, chunksize = 10000)
                
    conn.commit()

#-------------FUNZIONE PER SALVARE L'OUTPUT DI NMAP SU CSV-------------
def save_csv_data(datcsv, path='.'):  # FUNZIONE PER PASSARE IL CSV DI NMAP AL MIO CSV
    with open(path + '/output.csv', 'w') as output:
        
        output.write(datcsv)
    reader = csv.reader(open("output.csv", "rU"), delimiter=';')
    writer = csv.writer(open("output2.csv", 'w'), delimiter=',')
    writer.writerows(reader)

#-------------TOOL PER LA RACCOLTA INFO WHOIS--------------------------
def whois_hunt(self):
    file = path.exists('Temporary/results.txt')
    if file == True:
        os.remove('Temporary/results.txt')
    else:
        pass   
    import definitico                               # fare error handling                  
    getvar = self.Type_an_IP_AddressIPHUNTER.text()     
    obj = IPWhois(getvar)  # DATI
    self.res = obj.lookup_whois()  # INFORMAZIONI
    self.formattedres = json.dumps(self.res, indent=2)

    self.label_7.setText(self.formattedres)
    
    f = open("Temporary/results.txt", "a")
    f.write("\n************************** NMAP SCAN *******************************")

    f.write(str(self.formattedres))

#-------------TOOL PER LA RACCOLTA INFO IP ABUSE-----------------------    
def IPabuse_hunt(self):
    import definitico                                                                                  # fare error handling
    url = 'https://api.abuseipdb.com/api/v2/check'
    getvar = self.Type_an_IP_AddressIPHUNTER.text() 
    
    querystring = {'ipAddress': getvar, 'maxAgeInDays': '90'}

    headers = {
            'Accept': 'application/json',
            'Key': '1470cb5c931b223895e357af37d02340ad10eef6ed710907b44a26c855573f183f3df52ac6839509'
    }

    self.response = requests.request(method = 'GET', url = url, headers = headers, params = querystring)

    # Formatted output
    self.decodedResponse = json.loads(self.response.text)
    self.formatteddecoded = json.dumps(self.decodedResponse, sort_keys = True, indent = 4)
    
    self.label_6.setText(self.formatteddecoded)
    f = open("Temporary/results.txt", "a")
    f.write("\n**************************ABUSE*******************************")
    f.write(str(self.formatteddecoded))

#-------------FUNZIONE PER RICONOSCERE LA CLASSE DI UN IP--------------
def class_def(self):
    import definitico
        
    classA = IPv4Network(("10.0.0.0", "255.0.0.0"))  # or IPv4Network("10.0.0.0/8")
    classB = IPv4Network(("172.16.0.0", "255.240.0.0"))  # or IPv4Network("172.16.0.0/12")
    classC = IPv4Network(("192.168.0.0", "255.255.0.0"))  # or IPv4Network("192.168.0.0/16")
    getvar = self.Type_an_IP_AddressIPHUNTER.text()                                                          # definizione classe Ip privato
    ip1 = IPv4Address(getvar)
    if ip1 in classA:
        self.label_class.setText('Classe A')
        f = open("Temporary/results.txt", "a")
        f.write('classe A')
    elif ip1 in classB:
        self.label_type.setText('Classe B')
        f = open("Temporary/results.txt", "a")
        f.write('classe B')    
    elif ip1 in classC:
        self.label_class.setText('Classe C')
        f = open("Temporary/results.txt", "a")
        f.write('classe C')
    else:
        self.label_class.setText('non ne ho idea')
        f = open("Temporary/results.txt", "a")
        f.write('classe non ne ho idea')
        

#-------------FUNZIONE PER RICONOSCERE HOSTNAME PRIVATO-----------------
def host_name(self):
    try:
        getvar = self.Type_an_IP_AddressIPHUNTER.text()                                                          # definizione classe Ip privato
        info_client = socket.gethostbyaddr(getvar)
        global client
        client = info_client[0]
        print('hostname = ' + client)
        self.label_hostname.setText('hostname = ' + client)
        f = open("Temporary/results.txt", "a")
        f.write('hostname = ' + client)
    except socket.herror:
        print('Socket.herror, host name not found')
        client = 'Not Found'
        pass     

#-------------FUNZIONE PER RICONOSCERE IL VENDOR DEL MAC----------------
def look_vendor(self):
    import definitico
    global mac
    file = path.exists('Temporary/results.txt')
    if file == True:
        os.remove('Temporary/results.txt')
    else:
        pass
    try:
        getvar = self.Type_an_IP_AddressIPHUNTER.text()                                                          # definizione classe Ip privato

        mac = get_mac_address(ip = getvar)
        self.label_macaddress.setText(mac)
        #API base url,you can also use https if you need
        url = "http://macvendors.co/api/"
        #Mac address to lookup vendor from

        request = urllib2.Request(url+mac, headers={'User-Agent' : "API Browser"}) 
        response = urllib2.urlopen( request )
        #Fix: json object must be str, not 'bytes'
        reader = codecs.getreader("utf-8")
        global vendor
        vendor = json.load(reader(response))
        
        #Print company name
        
        company = vendor['result']['company']
        global company2
        company2 = company
        print(company)
        f = open("Temporary/results.txt", "a")
        f.write(company)
    except KeyError:
        company2 = "Not found" 
        pass
    except TypeError:
        print("mac address not found")
        pass
    except NameError:
        company2 = "Not found" 
        pass

#-------------FUNZIONE PER INSERIRE I DATI IP PRIVATI NEL DB------------
def insert_data(self):
    import sign_in
    import definitico
    getvar = self.Type_an_IP_AddressIPHUNTER.text()                                                          # definizione classe Ip privato

    with sqlite3.connect("IpHunter.db") as db:                # creazione di un database                                                         
        c = db.cursor() 
    add_data = ('INSERT INTO private_ip(ip_address, client, mac_address, vendor, scan_data, scan_username) VALUES (?, ?, ?, ?, datetime(), ? )')

    data = [(getvar), (client), (mac), (company2), (sign_in.mail)]
    c.execute(add_data, data)
    db.commit()
    
    conn = sqlite3.connect('IpHunter.db')
    c = conn.cursor()
    users = pd.read_csv('output2.csv')
    users.to_sql('nmap_output', conn, if_exists='append', index = False, chunksize = 10000)
    ##  c.executemany("INSERT OR IGNORE INTO IP_ACTIVE_SERVICES (host, port, service, state) VALUES (?, ?, ?, ?);",
    ##                to_db)                     
    db.commit()