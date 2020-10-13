# IP HUNTER 
An objective was given to us, it was to be able to create an IP Hunter that was able to detect and analyze any IP given and get as many information as possible about that IP.

IP HUNTER is an opensource program for soc analyst, it helps with collect data from a specifi IP address

### More tools:


IP Hunter has

- whois tool (via api)
- IP abuse tool (vai api)
- IP geolocalization (via api with personal key)
- SSL scan
- Management Database

## Installation
Per l'installazione di "Ip Hunter" è necessario installare Python 3.3.x o successive.
Si consiglia la creazione di un virtual enviroment (abbrev. venv) per fare tutti i test del prodotto ed eventuale sviluppo.

Le versioni di Python più recenti (dalla 3.3 in poi) hanno un modulo venv nella libreria standard che permette appunto di creare i venv. 
Il procedimento è molto semplice, ad esempio in ambiente windows, aprite un prompt dei comandi, oppure dall'ambiente di sviluppo un "terminale".
Create ad es. una directory "Envs" nel vostro disco C:\ che conterrà tutti i vostri "virtual enviroments" ad esempio C:\Envs
Attivate l'ambiente di sviluppo o semplicemente shell di Python e portatevi nella directory C:\Envs, ed invocate il modulo venv per creare il nuovo venv:

C:\ > cd C:\Envs
C:\Envs > python -m venv iphunter 

L'opzione -m vuol dire che non ci interessa invocare la shell di Python, ma vogliamo invece che Python esegua un modulo in particolare: 
in questo caso, il modulo venv con l'argomento ulteriore iphunter che è semplicemente il nome che vogliamo dare al venv che stiamo creando.

Con questo abbiamo creato un nuovo venv di nome iphunter. 
Concretamente, questo significa che adesso esiste una directory C:\Envs\iphunter dentro i file necessari a eseguire Python 3.x e la sua libreria standard
(controllate pure!).

Per "usare" un venv bisogna prima "attivarlo". Per questo scopo esiste un batch script activate.bat o activate.ps1 
che viene sempre copiato nel processo di creazione del venv: 
Dalla finestra terminale, dell'ambiente di sviluppo dalla sheel di Python potete usarlo in questo modo:

C:\Envs\iphunter\Scripts\activate.ps1

Il prompt della shell cambierà in questo modo


(iphunter) ...

Da una directory di lavoro qualsiasi, in questo modo avete attivato il venv. 
Notate che adesso il prompt indica la stessa directory di prima, ma preceduta dal nome del venv (iphunter nel nostro caso): 
questo vuol dire che adesso state lavorando "dentro" il venv. 

Una volta attivato il venv, andare nella cartella iphunter e dare il comando di installazione:

python -m pip install -r requirements.txt


# estratto del file requirements.txt 

- python_nmap==0.6.1
- pandas==1.1.2
- ipwhois==1.2.0
- requests==2.24.0
- getmac==0.8.2
- ipinfo==3.0.0
- netaddr==0.8.0
- passlib==1.7.2
- PyQt5==5.15.1

## Possibile Errore di nmap
potresti riscontrare il problema del PortScanner non presente
In caso di errori su nmap port verificare che non siano stati installati contemporaneamente nmap e python-nmap...
Disinstallare tutti i package nmap,procedere come segue:
1. python -m pip uninstall nmap
2. python -m pip uninstall python-nmap
3. python -m pip install python-nmap
4. uscire e rientrare da visual studio

## Usage
IP Hunter GUI is userfriendly

There is a home page with a IP general search with all the IP Hunter tools and after that ips are stored in database.

thr other tools are placed in the left menu, it appears when the menu button is clicked



![HomePage](https://github.com/Andrxid/IP-Hunter/blob/main/img/2020-10-13%2012_57_07-.png)

## Tools

### Whois
- Insert a valid Ip address it will display the Whois API results

![HomePage](https://github.com/Andrxid/IP-Hunter/blob/main/img/2020-10-12%2020_55_37-.png)

### Abuse
- Insert a valid Ip address it will display the Abuse API results

![HomePage](https://github.com/Andrxid/IP-Hunter/blob/main/img/2020-10-12%2020_55_39-.png)

### Radar
- Insert a valid Ip address it will display the Geolocalization API results


![HomePage](https://github.com/Andrxid/IP-Hunter/blob/main/img/2020-10-12%2020_55_42-.png)

### SSL Scan
##### Warning this is an incomplete Task!!!!!
- Insert a valid Ip address it will display the ssl results

![HomePage](https://github.com/Andrxid/IP-Hunter/blob/main/img/2020-10-12%2020_55_45-.png)

### Database
- Search a specific private or public IP address

![HomePage](https://github.com/Andrxid/IP-Hunter/blob/main/img/2020-10-12%2020_55_48-.png)
![HomePage](https://github.com/Andrxid/IP-Hunter/blob/main/img/2020-10-12%2020_55_51-.png)
![HomePage](https://github.com/Andrxid/IP-Hunter/blob/main/img/2020-10-12%2020_56_03-.png)



