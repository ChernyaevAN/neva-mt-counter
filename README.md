# Исходные коды (origin code)

# Библиотека для связи со счетчиками электроэнергии Нева МТ3хх
Origin code is on link
https://github.com/vika-sonne/NevaMt3xx
It is for Python 2.x

I only updated for Python 3.x Serial Port part 

1 Change serial.write(str)  and serial.read(s) with
serial.write(ss.encode()) and serial.read(s.decode())

2. So, added one test (myneva.py) for get Current, Voltage, Power, etc from device
Many thanks for original code !

# Средства отладки библиотеки

# Имитатор счетчика

# Original README.md

# NevaMt3xx
Serial interface access library of electric power consumption counter of "Neva MT 3xx" type by Taipit (Saint-Petersburg) manufacturing

# Нева МТ 3xx
Работа со счётчиком потребления электроэнергии типа Нева МТ 3xx производства Тайпит (Санкт-Петербург). Работа с прибором учёта происходит согласно МЭК 61107 и [OBIS](http://www.dlms.com/documentation/listofstandardobiscodesandmaintenanceproces/index.html) кодам (кроме байта контрольной суммы пакета, он не соответствует МЭК 61107 (ISO 1155)). Использует [python 2](https://www.python.org/downloads/). Работа согласно протоколу МЕК 61107 реализована библиотекой, которая может быть использована для работы с другими типами приборов.

Требует установки пакетов:
1. [pySerial](https://pypi.org/project/pyserial/).
Установить можно используя [pip](https://pypi.org/project/pip/) в одну строку командного интерпритатора: `pip install pyserial`. При этом проконтролировать, что используется pip необходимой версии python (для Windows - запуск pip.exe из необходимой папки).

2. [argparse](https://pypi.org/project/argparse/).
Установка аналогично: `pip install argparse`.

## test_serial.py
Утилита командной строки для работы со счётчиком. Производит считывание/запись значений OBIS параметров. Содержит алгоритм считывания архива получасовых показаний с разбором по 4-м тарифам согласно тарифному расписанию.
Пример считывания версии счётчика:
```
> python test_serial.py -p ttyUSB0 --obis 60.01.04*FF
000V0201
```
[Примеры запуска и работы утилиты](test_serial.log).

Вывод справки: `python test_serial.py -?`.

## meter_imitator.py
Утилита командной строки - имитатор работы счётчика (считывание/запись параметров OBIS) для отладки и технологических прогонов сервисного п/о работы с этими счётчиками. Имитатор представляет сервер, ожидающий подключений по TCP порту. [Пример запуска имитатора](meter_imitator.sh) со списком значений для OBIS параметров, например: `-o 60.01.04*FF:000V020`. Значения даты и времени можно не задавать, тогда возвращаются текущие показания:
- `00.09.02*FF`: дата, ГГММДД
- `00.09.01*FF`: время, ЧЧММСС

Вывод справки: `python meter_imitator.py -?`.
