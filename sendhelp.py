import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
#import os


from PyQt5.QtWidgets import QMessageBox


#-------INVIO DELLA MAIL DEL DILEMMA---------------------
def send_dilemma(self):
    
    import definitico
    fromaddr = "iphunter.spam@gmail.com"
    toaddr = "andrea.candura@outlook.it"
    
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    
    # storing the senders email address   
    msg['From'] = fromaddr 
    
    # storing the receivers email address  
    msg['To'] = toaddr 
    obj = self.Mail_object.text()
    # storing the subject  
    msg['Subject'] = obj
    
    # string to store the body of the mail 
    body = self.plainTextEdit_HELP.text()
    
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    
    # open the file to be sent  
    #filename = "results.txt"
    #attachment = open("Temporary/results.txt", "rb") 
    
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    
    # To change the payload into encoded form 
    #p.set_payload((attachment).read()) 
    
    # encode into base64 
    #encoders.encode_base64(p) 
    
    #p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    
    # attach the instance 'p' to instance 'msg' 
    #msg.attach(p) 
    
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
    #attachment.close()
    # terminating the session 
    s.quit() 
    #os.remove('Temporary/results.txt')
    
    self.message_send_help()

#--------MESSAGIO DI CONFERMA INVIO MAIL-----------------
def message_send_help(self):
    import definitico
    msg = QMessageBox()
    msg.setWindowTitle("Message sended")
    msg.setText("The E mail was send to your email-address")
    msg.setIcon(QMessageBox.Information)
    msg.setStandardButtons(QMessageBox.Ok)
    

    msg.exec_()