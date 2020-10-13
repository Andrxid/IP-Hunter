import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import os
import sign_in
from PyQt5.QtWidgets import QMessageBox

#----------FUNZIONE PER INVIARE I RISULTATI DI WHOIS TOOL
def sendresults_whois(self):
    
    
    fromaddr = "iphunter.spam@gmail.com"
    toaddr = sign_in.mail
    
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    
    # storing the senders email address   
    msg['From'] = fromaddr 
    
    # storing the receivers email address  
    msg['To'] = toaddr 
    
    # storing the subject  
    msg['Subject'] = "Results WHois"
    
    # string to store the body of the mail 
    body = "Here are the whois results"
    
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    
    # open the file to be sent  
    filename = "results.txt"
    attachment = open("Temporary/results.txt", "rb") 
    
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    
    # encode into base64 
    encoders.encode_base64(p) 
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    
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
    attachment.close()
    # terminating the session 
    s.quit() 
    os.remove('Temporary/results.txt')
    
    self.message_send()

#----------FUNZIONE PER INVIARE I RISULTATI DEL TOOL DI ABUSE--------    
def sendresults_abuse(self):
    fromaddr = "iphunter.spam@gmail.com"
    toaddr = sign_in.mail
    
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    
    # storing the senders email address   
    msg['From'] = fromaddr 
    
    # storing the receivers email address  
    msg['To'] = toaddr 
    
    # storing the subject  
    msg['Subject'] = "Results "
    
    # string to store the body of the mail 
    body = "Here are the IP  results"
    
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    
    # open the file to be sent  
    filename = "results.txt"
    attachment = open("Temporary/results.txt", "rb") 
    
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    
    # encode into base64 
    encoders.encode_base64(p) 
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    
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
    attachment.close()
    # terminating the session 
    s.quit()
    os.remove('Temporary/results.txt')
    
    self.message_send()

#----------FUNZIONE PER INVIARE I RISULTATI DEL TOOL DI GEOLOCALIZATION-----
def sendresults_geo(self):
    fromaddr = "iphunter.spam@gmail.com"
    toaddr = sign_in.mail
    
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    
    # storing the senders email address   
    msg['From'] = fromaddr 
    
    # storing the receivers email address  
    msg['To'] = toaddr 
    
    # storing the subject  
    msg['Subject'] = "Results Geolocalization"
    
    # string to store the body of the mail 
    body = "Here are the IP Geolocalization results"
    
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    
    # open the file to be sent  
    filename = "results.txt"
    attachment = open("Temporary/results.txt", "rb") 
    
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    
    # encode into base64 
    encoders.encode_base64(p) 
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    
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
    attachment.close()
    # terminating the session 
    s.quit()
    os.remove('Temporary/results.txt')
    self.message_send()
    
#----------MESSAGIO DI CONFERMA INVIO MAIL-----------------------------
def message_send(self):
    import definitico
    msg = QMessageBox()
    msg.setWindowTitle("Message sended")
    msg.setText("The E mail was send to your email-address")
    msg.setIcon(QMessageBox.Information)
    msg.setStandardButtons(QMessageBox.Ok)
    

    msg.exec_()
    
def sendresults_hunt(self):
    fromaddr = "iphunter.spam@gmail.com"
    toaddr = sign_in.mail
    
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    
    # storing the senders email address   
    msg['From'] = fromaddr 
    
    # storing the receivers email address  
    msg['To'] = toaddr 
    
    # storing the subject  
    msg['Subject'] = "Results General scan"
    
    # string to store the body of the mail 
    body = "Here are the IP Hunter results"
    
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    
    # open the file to be sent  
    filename = "results.txt"
    attachment = open("Temporary/results.txt", "rb") 
    
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    
    # encode into base64 
    encoders.encode_base64(p) 
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    
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
    attachment.close()
    # terminating the session 
    s.quit()
    os.remove('Temporary/results.txt')
    self.message_send()