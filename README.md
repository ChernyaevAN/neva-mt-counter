# Библиотека для связи со счетчиками Нева МТ
The library to connect Neva MT power counters<br>
Библиотека для связи со счетчиками электроэнергии Нева МТ (ООО "Тайпит - ИП")<br>

Исходный код библиотеки взят [отсюда](https://github.com/vika-sonne/NevaMt3xx/) и [отсюда](https://github.com/AlexObukhoff/neva-py3/).<br>
Original code is on [this](https://github.com/vika-sonne/NevaMt3xx/) and [this](https://github.com/AlexObukhoff/neva-py3/) links.<br>

Для связи со счетчиками Нева МТ существует еще одна [библиотека](https://github.com/nnemirovsky/pyneva/).<br>

Исходный код проверялся на Python 3.10.7 под операционной системой Ubuntu 22.10.<br>

## Основные изменение (general changes)
Исправлены все ошибки и предупреждения при исполнении исходного кода.
All warnings and errors are fixed.

Добавлена возможность подключения через TCP/IP сокет при схеме подключения счетчика, указанной ниже.
TCP/IP connection ability added.

Проверена возможность подключения через виртуальный последовательный порт на базе [socat](http://www.dest-unreach.org/socat/doc/socat.html).
[Socat](http://www.dest-unreach.org/socat/doc/socat.html) virtual serial port connection ability checked.

### Создание виртуального последовательного порта
Для создания виртуального последовательного порта можно использовать [socat](http://www.dest-unreach.org/socat/doc/socat.html).<br>
`sudo socat  pty,link=/dev/virtualcomX,raw  tcp:192.168.XXX.XXX:XXXXX`<br>
При этом конвертер интерфейсов должен работать в режиме сервера. После IP адреса указывается порт подключения. В указанном примере создается последовательный порт /dev/virtualcomX, где X - номер порта.

### Недостатки использования виртуальных последовательных портов
В исходном [коде](https://github.com/AlexObukhoff/neva-py3/) используется библиотека [pyserial](https://pypi.org/project/pyserial/). Не удается многократно использовать порт в связи со следующей [ошибкой](https://github.com/pyserial/pyserial/issues/196).
