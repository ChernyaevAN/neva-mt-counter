import os
import time
# for using serial port
# import serial
from library import NevaMt3xx
# import paho.mqtt.client as mqtt
# for using TCP connection
import socket

# print('aaa')

'''
Для подключения необходимо создать последовательный порт следующей строкой:
socat  pty,link=/dev/virtualcom0,raw  tcp:192.168.100.XXX:8899
# Может возникнуть путаница из-за некорректного выставления параметров протокола,
#  непосредственно со счетчиком должны быть параметры 7Е1, в конвертере интерфейсов 8N1

port = serial.Serial(port='/dev/virtualcom0',
					 baudrate = 9600,
					 timeout = 2,
					 bytesize = serial.SEVENBITS,
					 parity = serial.PARITY_EVEN,
					 stopbits = serial.STOPBITS_ONE)

protocol = NevaMt3xx.NevaMt3xx_com(port)
'''

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 18899))
sock.listen(1)
connection, client_address = sock.accept()
protocol = NevaMt3xx.NevaMt3xx_tcp(connection)

result = {}

# connect & login
print('SEND: /?!\\r\\n')
company, device = protocol.connect()
cmd = protocol.receive()
print('RCV:' + str(cmd))
print(company, device)
if not cmd.is_command or cmd.command != 'P0':
    raise Exception('Command "P0" expected')

result['Vendor'] = company
result['Model'] = device

password = '00000000'
protocol.send(NevaMt3xx.NevaMt3xx.Command('P1', '(' + password + ')'))
cmd = protocol.receive()
print('RCV:' + str(cmd))

if not cmd.is_ack:
    raise Exception('Access denied')

obis_str = {
    'Date': '00.09.02*FF',  # Дата: ГГММДД
    'Time': '00.09.01*FF',
    'Version': '60.01.04*FF',
    'Address': '60.01.01*FF',
    'Point': '60.01.0A*FF',  # Точка учёта
}

obis_values = {
    'Voltage': '0C.07.00*FF',  # Напряжение по сумме фаз
    'Current': '0B.07.00*FF',  # Ток по сумме фаз
    'Active_Power': '10.07.00*FF',  # Активная мощность
    'Freq': '0E.07.01*FF',
    'Temp': '60.09.00*FF',
    'KPower': '0D.07.FF*FF',  # Коэффициент активной мощности
    'T': '0F.08.80*FF',  # Значение счётчиков по всем тарифам начиная с общего
}

table = str.maketrans("", "", '.*')

for key, value in obis_str.items():
    value = value.translate(table) + '()'
    print('SEND:' + key)
    protocol.send(NevaMt3xx.NevaMt3xx.Command('R1', value))
    cmd = protocol.receive()
    print('RCV:' + str(cmd))
    if not cmd.is_message:
        raise Exception('OBIS 000902FF expected')
    data = str(cmd.data[8:].strip('()'))
    result[key] = data


def ltrim_value(s: str) -> str:
    while len(s) > 2 and s[0] == '0' and s[1] != '.':
        s = s[1:]
    return s


for key, value in obis_values.items():
    value = value.translate(table) + '()'
    print('SEND:' + key)
    protocol.send(NevaMt3xx.NevaMt3xx.Command('R1', value))
    cmd = protocol.receive()
    print('RCV:' + str(cmd))
    if not cmd.is_message:
        raise Exception('OBIS 000902FF expected')
    data = ltrim_value(str(cmd.data[8:].strip('()')))
    if ',' in data:
        data = [ltrim_value(d) for d in data.split(',')]
        for i, d in enumerate(data):
            result[key + str(i)] = d
    else:
        result[key] = data


def on_log(client_instance, userdata, level, buff):
    print(buff)


'''
try:
	client = mqtt.Client("P1")  # create new instance
	# client.on_log = on_log
	client.username_pw_set(os.getenv('MQTT_LOGIN'), os.getenv('MQTT_PASSWORD'))
	client.connect('localhost')  # connect to broker
	client.loop_start()  # start the loop
	for key, value in result.items():
		client.publish(f"neva/{key}", value)
	time.sleep(4)  # wait
	client.loop_stop()  # stop the loop
except Exception as e:
	print(e, '\n\n')
	for key, value in result.items():
		print(key, ':', value)
'''

# logout
protocol.send(NevaMt3xx.NevaMt3xx.Command('B0', ''))

# try:

# except Exception as e:
# 		print (u'ERROR: '+str(e))
