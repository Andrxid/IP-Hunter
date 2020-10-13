

from ipwhois import IPWhois
import json
import os
from os import path


def whois_ip(self):
    import definitico
    file = path.exists('Temporary/results.txt')
    if file == True:
        os.remove('Temporary/results.txt')
    else:
        pass                               # fare error handling                  

    
    try:
        getvar = self.Type_an_IP_Address_WHOIS.text()        
        obj = IPWhois(getvar)  # DATI
        self.res = obj.lookup_whois()  # INFORMAZIONI
        self.formattedres = json.dumps(self.res, indent=2)

        self.output_whois.setText(self.formattedres)
        
        f = open("Temporary/results.txt", "a")
        f.write(str(self.formattedres))
    except ValueError:
        self.output_whois.setText("Value error: Please try again") 