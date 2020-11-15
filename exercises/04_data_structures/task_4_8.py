# -*- coding: utf-8 -*-
"""
Задание 4.8
Преобразовать IP-адрес в переменной ip в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения
Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате надо добавить два пробела между столбцами)
Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = "192.168.3.1"
ip = ip.split('.')
print(ip[0])
print(bin(int(ip[0])))
print("{:10}{:10}{:10}{:10}".format(ip[0],ip[1],ip[2],ip[3]))
print("{:08b}  {:08b}  {:08b}  {:08b}".format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3])))