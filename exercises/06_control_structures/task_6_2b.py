# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

while(True):
	ip = input('Введите IP-адрес в формате 10.0.1.1: ')
	octets = ip.split('.')
	valid_ip = len(octets) == 4
	
	for oct in octets:
		valid_ip = oct.isdigit() and 0 <= int(oct) <= 255 and valid_ip

	if (valid_ip == True):
		oct = int(ip[0])
 
		if (oct >= 1 and oct <= 223):
			print('unicast')
		elif (oct >= 224 and oct <= 239):
			print('multicast')
		elif (ip_address == '255.255.255.255'):
			print('local broadcast')
		elif (ip_address == '0.0.0.0'):
			print('unassigned')
		else:
			print('unused')	
		break
	else:		
		print('Неправильный IP-адрес')

	
