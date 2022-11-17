#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Firewall Tapmaq")
print (""" 
Xos geldiniz :D

""")

sayt = input("Sayt Adresini Daxil Et: ")
os.system("wafw00f " + sayt)
