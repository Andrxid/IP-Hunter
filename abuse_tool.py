
import requests
import json
import os

from os import path


def IPabuse(self):
    import definitico
    #os.remove('Temporary/results.txt')
    file = path.exists('Temporary/results.txt')
    if file == True:
        os.remove('Temporary/results.txt')
    else:
        pass                               # fare error handling                                                                                       # error handling integrato
    url = 'https://api.abuseipdb.com/api/v2/check'
    getvar = self.Type_an_IP_Address_ABUSE.text()
    
    querystring = {'ipAddress': getvar, 'maxAgeInDays': '90'}

    headers = {
            'Accept': 'application/json',
            'Key': '1470cb5c931b223895e357af37d02340ad10eef6ed710907b44a26c855573f183f3df52ac6839509'
    }

    self.response = requests.request(method = 'GET', url = url, headers = headers, params = querystring)

    # Formatted output
    self.decodedResponse = json.loads(self.response.text)
    self.formatteddecoded = json.dumps(self.decodedResponse, sort_keys = True, indent = 4)
    
    self.output_abuse.setText(self.formatteddecoded)
    f = open("Temporary/results.txt", "a")
    f.write(str(self.formatteddecoded))
    