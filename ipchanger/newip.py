import os
import time 
from os import system
import colorama
from colorama import Fore, Style
colorama.init()
print(Fore.RED + """
██████╗  ██████╗ ███████╗██╗  ██╗██╗   ██╗██████╗ ████████╗████████╗███████╗ █████╗ ███╗   ███╗
██╔══██╗██╔═══██╗╚══███╔╝██║ ██╔╝██║   ██║██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
██████╔╝██║   ██║  ███╔╝ █████╔╝ ██║   ██║██████╔╝   ██║      ██║   █████╗  ███████║██╔████╔██║
██╔══██╗██║   ██║ ███╔╝  ██╔═██╗ ██║   ██║██╔══██╗   ██║      ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
██████╔╝╚██████╔╝███████╗██║  ██╗╚██████╔╝██║  ██║   ██║      ██║   ███████╗██║  ██║██║ ╚═╝ ██║
╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
""""""
 ██████╗ ██████╗ ██████╗ ███████╗██████╗     ██████╗ ██╗   ██╗     █████╗ ███████╗██████╗  █████╗ ██╗██╗     
██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗    ██╔══██╗╚██╗ ██╔╝    ██╔══██╗╚══███╔╝██╔══██╗██╔══██╗██║██║     
██║     ██║   ██║██║  ██║█████╗  ██████╔╝    ██████╔╝ ╚████╔╝     ███████║  ███╔╝ ██████╔╝███████║██║██║     
██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗    ██╔══██╗  ╚██╔╝      ██╔══██║ ███╔╝  ██╔══██╗██╔══██║██║██║     
╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║    ██████╔╝   ██║       ██║  ██║███████╗██║  ██║██║  ██║██║███████╗
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═════╝    ╚═╝       ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
""")
print(Style.RESET_ALL)
print("command(komutlar) [1 = ip adresi deiştirme(ip changer)],[2 = mac adresi deiştirme(mac changer)],[3 = ip ve mac deiştirme(ip and mac changer)]")
command = int(input("bir veri girin(enter a data) : "))


if command == 1:
    seccont = int(input("kaç saniye'de değişsin(How many seconds do you change), tavsiye saniye 20,(recommed second(20)) : "))
    while True:
            os.system("service tor start")
            os.system("anonsurf start")
            os.system("anonsurf myip")
            time.sleep(seccont)
            os.system("anonsurf stop")

if command == 2:
    seccont = int(input("kaç saniye'de değişsin(How many seconds do you change), tavsiye saniye 20,(recommed second(20)) : "))
    os.system("ifconfig")
    servics=input(("hangi servis olduğunu seçin örn eth0 wlan1(wich service e.g(eth0,wlan1)"))
    while True:
        os.system("macchanger -r "+servics)
        time.sleep(seccont)
        os.system("macchanger -e "+servics)

if command == 3:
    seccont = int(input("kaç saniye'de değişsin(How many seconds do you change), tavsiye saniye 30,(recommed second(30)) : "))
    os.system("ifconfig")
    servics=input(("hangi servis olduğunu seçin örn eth0 wlan1(wich service e.g(eth0,wlan1)"))
    while True:
        os.system("service tor start")
        os.system("anonsurf start")
        os.system("anonsurf myip")
        os.system("macchanger -r "+servics)
        time.sleep(seccont)
        os.system("anonsurf stop")
        os.system("macchanger -e "+servics)
