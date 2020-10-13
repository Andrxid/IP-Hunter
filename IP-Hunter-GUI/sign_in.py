
import sqlite3
import random
from math import log
from random import choice
import sqlite3
from getpass import getpass
#import os
import smtplib, ssl
import random

from passlib.hash import  sha256_crypt
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import os
import sign_in
from PyQt5.QtWidgets import QMessageBox








#------------------CREAZIONE DEL DB CREDENZIALI NEL CASO IN CUI NON ESISTESSE---------
def create_db():
    with sqlite3.connect("IpHunter.db") as db:                # creazione di un database                                                         
            c = db.cursor()                                         # username, password, email, data di registrazione e data ultimo accesso
    c.execute("""
    CREATE TABLE IF NOT EXISTS user_cred(                            
    username TEXT NOT NULL,
    email TEXT PRIMARY KEY NOT NULL,
    password VARCHAR(20) NOT NULL,
    Reg_data DATETIME DEFAULT CURRENT_TIMESTAMP,
    settings TEXT)
    """)
    db.commit()
    
#------------------FUNZIONE PER LA GENERAZIONE DI UN CODICE RANDOM-------------------
def code_generator(self):
    numbers = "0123456789"
    lenght = 4
    global code
    self.code = "".join(random.sample(numbers, lenght))
#------------------FUNZIONE SEND EMAIL PER LA 2FA------------------------------------------------
def sendmail(self):
    self.code_generator()   
    
    fromaddr = "iphunter.spam@gmail.com"
    toaddr = sign_in.mail
    
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    
    # storing the senders email address   
    msg['From'] = fromaddr 
    
    # storing the receivers email address  
    msg['To'] = toaddr 
    
    # storing the subject  
    msg['Subject'] = "Code Verification for 2FA"
    
    # string to store the body of the mail 
    body = "Your code verification is: " + self.code
    
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
        
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    
    # start TLS for security 
    s.starttls() 
    
    # Authentication 
    s.login(fromaddr, "TeamApassword!") 
    
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 

    # terminating the session 
    s.quit() 
    


#------------------VERIFICA DEL CODICE INVIATO-----------------------------
def verify(self):
    import definitico
    from definitico import QtCore
    code_verification = self.lineEdit_PASSWORD_3.text()
    if code_verification == self.code:
            print('\n-----------------OK, READY TO START THE HUNT?---------------')
            self.personal_color()
        
            self.ABUSE.show()
            self.DATABASE.show()
            self.Home_IP_HUNTER.show()
            self.SSL_SCAN.show()
            self.WHOIS.show()
            self.SETTINGS.show()
            self.RADAR.show()
            self.LOG_IN.hide()
            self.IP_HUNTER_tittle.setText(QtCore.QCoreApplication.translate("IPSEARCH_window", sign_in.mail))

            
            
            self.stackedWidget.setCurrentWidget(self.PAGE_IP_HUNTER)
    else:
        self.msgerror()
        self.lineEdit_PASSWORD_3.clear()
        self.stackedWidget.setCurrentWidget(self.LOG_IN_2)

        
                
        

#------------------FUNZIONE PER IL LOG IN E INVIO DELLA MAIL--------------------            
def login(self):
    import definitico
    try:
        global mail
        mail = self.lineEdit_E_MAIL_2.text()

        password = self.lineEdit_PASSWORD_2.text()
        
        with sqlite3.connect("IpHunter.db") as db:
                c = db.cursor()
        find_mail =("SELECT email FROM user_cred WHERE email = ?")
        c.execute(find_mail, [(mail)])
        mail_ver = c.fetchall()
        if mail_ver:
                find_password = ("SELECT password FROM user_cred WHERE email = ?")
                c.execute(find_password, [(mail)])
                pass_hash = c.fetchone()
                pass_verify = sha256_crypt.verify(password, pass_hash[0])
        
                if pass_verify == True:
                        self.sendmail()
                        
                        print("\nWe have send an email with the verification code, insert below")
                        self.stackedWidget.setCurrentWidget(self.PAGE_INSERT_CODE) 
                        pass
    except smtplib.SMTPRecipientsRefused:
            self.msgerror()
        
#------------------FUNZIONE PER LA CREAZIONE DI UN NUOVO UTENTE----------------
def register(self):
    import definitico
    setting = "background-image: url(images/bg_IPh.png);"
    reg_email = self.lineEdit_E_MAIL_3.text()
    with sqlite3.connect("IpHunter.db") as db:
        c = db.cursor()
    c.execute("SELECT username FROM user_cred WHERE email = ?", [(reg_email)] )
    data = c.fetchall()
    if len(data) == 0:
        reg_username =  self.lineEdit_USERNAME_2.text()
        
        reg_password = self.lineEdit_PASSWORD_5.text()
        reg_password_crypt = sha256_crypt.hash(reg_password)
        add_credential = ("INSERT INTO user_cred (username, email, password, Reg_data, settings) VALUES (?, ?, ?, datetime(), ?)")
        data2 = [(reg_username), (reg_email), (reg_password_crypt), (setting)]
        c.execute(add_credential, data2) 
        db.commit()
        self.stackedWidget.setCurrentWidget(self.LOG_IN_2)
    else:
        print("ERROR: This email is used by another account")
        self.already_exist()
        
#-----------------MESSAGGIO SE UTENTE ESISTE GIA' IN FASE DI REG--------------
def already_exist(self):
    import definitico
    msg = QMessageBox()
    msg.setWindowTitle("Already Used")
    msg.setText("ERROR: This email is used by another account")
    msg.setIcon(QMessageBox.Warning)
    msg.setStandardButtons(QMessageBox.Ok)
    

    msg.exec_()

#-----------------MESSAGGIO DI ERRORE-----------------------------------------    
def msgerror(self):
    import definitico
    msg = QMessageBox()
    msg.setWindowTitle("error")
    msg.setText("invalid input")
    msg.setIcon(QMessageBox.Warning)
    msg.setStandardButtons(QMessageBox.Ok)
    

    msg.exec_()


#-----------------INVIO DELLA MAIL CON CODICE GENERATO PER RESET DELLA PASSWORD-------------------
def sendmail_reset(self):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "iphunter.spam@gmail.com"
    receiver_email = self.lineEdit_USERNAME.text()
    password = "TeamApassword!"
    self.code_generator()                            # richiamo della funzione per il codice
    message = """\
            Subject: HI
    
    
    
            your verification code is: """ + self.code

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        
#-----------------FUNZIONE PER IL RESET DELLA PASSWORD-------------------------------
def reset_password(self):
    import definitico
    code_verification = self.lineEdit_entercode.text()
    with sqlite3.connect("IpHunter.db") as db:                # creazione di un database                                                         
        c = db.cursor()     
    mail = self.lineEdit_USERNAME.text()
    if code_verification == self.code:
            # devo fare una select dove la mail è uguale a quella inserita e modificare la password selezionata con quelle nuova
        password = self.lineEdit_new_password.text()
        new_password = self.lineEdit_conf_password.text()
        
        if password == new_password:
            reg_password_crypt = sha256_crypt.hash(new_password)            
            modify = ("UPDATE user_cred SET password = ? WHERE email = ?")            
            data = [(reg_password_crypt), (mail)]
            
            c.execute(modify, data)
            db.commit()
            self.stackedWidget.setCurrentWidget(self.LOG_IN_2)
        else:
            
            print('password non sono uguali riprova')
            

    pass
    
    
    