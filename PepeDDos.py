#!/usr/bin/env python

#⣿⣿⣿⣿⣿⡿⠛⠋⠁⠀⠀⠀⠀⠙⠛⠿⠟⠋⠉⠁⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿
#⣿⣿⣿⡿⠋⠀⠸⠄⢀⣀⠠⠤⠤⣀⡀⠐⡄⠀⠀⠀⠀⠀⠾⠂⠈⠻⣿⣿⣿⣿
#⣿⣿⡟⠀⠀⠀⠠⠋⠁⠀⠀⠀⠀⠀⠉⠙⠻⠒⠚⠛⠛⠛⠛⠒⠒⠦⠘⢿⣿⣿
#⣿⠟⠀⠀⡆⠀⠀⠀⠀⢀⣤⣴⣶⣶⣶⣶⣶⣧⣄⢀⣠⣤⣤⣶⣶⣶⣤⣤⣙⢿
#⠁⢸⠀⠸⠅⠀⠀⣴⣾⣿⣿⣿⣿⣿⡏⡉⠙⣿⣿⣼⣿⣿⣿⣿⣿⢋⡉⢻⣿⡆
#⣀⠀⠀⠀⠀⠀⠀⠀⢉⠛⠿⢿⣿⣿⣷⣧⣶⡿⠟⠸⠿⠿⣿⡿⠿⠶⠬⠾⠿⢃
#⠓⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠤⠤⠬⠭⠁⣤⠤⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠔⠊⠁⠀⠀⠀⠑⠢⡄⠒⠒⠂⠰⣿⣿⣿  coded with <3 by Pepe-Devs
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿
#⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡈⣿
#⠀⠀⠀⠀⠀⠀⣼⣿⣧⣭⣭⣍⣛⣛⣛⡶⠶⠶⢦⣤⣤⣤⣤⣤⣴⣶⠿⠛⣡⣿
#⠀⠀⠀⠀⠰⢄⠈⠉⠉⠉⠉⠉⠉⠙⠛⠛⠿⠿⠿⠷⠶⠶⣶⣶⣶⡶⢟⣸⣿⣿
#⣄⣀⡀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿
#⠀⠀⠈⠉⠓⠒⠢⠤⠤⠤⠤⣤⣤⣤⣤⠤⠄⠀⠀⠀⢴⣶⣿⣿⣿⣿⣿⣿⣿⣿
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⠀⠀



# ИМПОРТИРУЕМ ВСЯКУЮ ФИГНЮ
import sys
import time
import socket
import struct
import threading
from random import randint
from optparse import OptionParser
from pinject import IP, UDP
from termcolor import colored

# ЛОГО (ПРОФИ ЗОВУТ ЕГО БАННЕР)
def banner():
    system("cls" if name == "nt" else "clear")
    print(colored( '''
⣿⣿⣿⣿⣿⡿⠛⠋⠁⠀⠀⠀⠀⠙⠛⠿⠟⠋⠉⠁⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⠋⠀⠸⠄⢀⣀⠠⠤⠤⣀⡀⠐⡄⠀⠀⠀⠀⠀⠾⠂⠈⠻⣿⣿⣿⣿
⣿⣿⡟⠀⠀⠀⠠⠋⠁⠀⠀⠀⠀⠀⠉⠙⠻⠒⠚⠛⠛⠛⠛⠒⠒⠦⠘⢿⣿⣿
⣿⠟⠀⠀⡆⠀⠀⠀⠀⢀⣤⣴⣶⣶⣶⣶⣶⣧⣄⢀⣠⣤⣤⣶⣶⣶⣤⣤⣙⢿
⠁⢸⠀⠸⠅⠀⠀⣴⣾⣿⣿⣿⣿⣿⡏⡉⠙⣿⣿⣼⣿⣿⣿⣿⣿⢋⡉⢻⣿⡆
⣀⠀⠀⠀⠀⠀⠀⠀⢉⠛⠿⢿⣿⣿⣷⣧⣶⡿⠟⠸⠿⠿⣿⡿⠿⠶⠬⠾⠿⢃
⠓⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠤⠤⠬⠭⠁⣤⠤⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠔⠊⠁⠀⠀⠀⠑⠢⡄⠒⠒⠂⠰⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿
⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡈⣿
⠀⠀⠀⠀⠀⠀⣼⣿⣧⣭⣭⣍⣛⣛⣛⡶⠶⠶⢦⣤⣤⣤⣤⣤⣴⣶⠿⠛⣡⣿
⠀⠀⠀⠀⠰⢄⠈⠉⠉⠉⠉⠉⠉⠙⠛⠛⠿⠿⠿⠷⠶⠶⣶⣶⣶⡶⢟⣸⣿⣿
⣄⣀⡀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿
⠀⠀⠈⠉⠓⠒⠢⠤⠤⠤⠤⣤⣤⣤⣤⠤⠄⠀⠀⠀⢴⣶⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''','magenta'))

def help():
    ()
    
def option():
    ()

#АНАНАСЫ АТАКУЮТ!!!    
def attack():
    
        '  Отправлено!  '
	'|    Траффик   '
	'|    Пакет(ы)  '
	'|     Бит(ы)   '
	'\n{}').format('-'*63)
	
# ТУТ ВВОДИМ ПОРТ	
def port():  

	'dns': 53,
	'ntp': 123,
	'snmp': 161,
	'ssdp': 1900 
