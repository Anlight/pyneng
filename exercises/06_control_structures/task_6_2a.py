# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ip_address = input('Введите IP-адрес в формате 10.0.1.1: ')
correct_ip = True
ip = ip_address.split('.')

if (len(ip) != 4):
	correct_ip = False

for oct in ip:
	if not (oct.isdigit() and 0 <= int(oct) <= 255):
		correct_ip = False
        
if (correct_ip == True):	
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
else:
	print('Неправильный IP-адрес')

