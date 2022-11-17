#!/etc/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Zeiflik Analizi")
print (""" 
Xos Geldiniz :)

""")

hedefIP = input("Hedef IP Daxil Edin: ")
os.system("nikto -h " + hedefIP)
