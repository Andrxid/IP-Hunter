
import requests
import json
import ipinfo 
import time
import os
from os import path


def message_send(self):
    import definitico
    from definitico import QMessageBox
    msg = QMessageBox()
    msg.setWindowTitle("Message sended")
    msg.setText("Checking your Ip geolocalization")

    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()




def IP_geo(self):
    import definitico 
    file = path.exists('Temporary/results.txt')
    if file == True:
        os.remove('Temporary/results.txt')
    else:
        pass         
    try:

                
        getvar = self.Type_an_IP_Address_radar.text()

     # codice per il servizio di geolocalizzazione IP
        acces_token = '1d920b86e75c6e'

        handler = ipinfo.getHandler(acces_token)  # DATI
        details = handler.getDetails(getvar)  # GEOLOCALIZZAZIONE
        self.details2 = json.dumps(details.all)
        
        self.output_radar.setText(self.details2)
        
        f = open("Temporary/results.txt", "a")
        f.write(str(self.details2))
        
        

                
                
    except requests.exceptions.HTTPError:
                
        self.output_radar.setText("requests.exceptions.HTTPError:")
        pass