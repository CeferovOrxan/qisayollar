#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Port Axtarma")
print (""" 
Hello Guys!!! :)

1) Tez axtarma
2) Servis ve versiya melumati
3) Emeliyyat sistemi melumati

""")

sayino = input("Sayini Daxil Edin: ")

if(sayino=="1"):
         hedefIP = input("Hedef IP daxil edin: ")
         os.system("nmap " + hedefIP)
elif(sayino=="2"):
         hedefIP = input("Hedef IP daxil edin: ")
         os.system("nmap -sS -sV " + hedefIP)
elif(sayino=="3"):
         hedefIP = input("Hedef IP daxil edin: ")
         os.system("nmap -0 " + HedefIP)
else: 
         print("bu reqemi gorusen orda???")  
