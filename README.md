# Библиотека для связи со счетчиками Нева МТ
The library to connect Neva MT power counters
Библиотека для связи со счетчиками электроэнергии Нева МТ (ООО "Тайпит - ИП")

Исходный код библиотеки взят [отсюда](https://github.com/vika-sonne/NevaMt3xx/) и [отсюда](https://github.com/AlexObukhoff/neva-py3/).
Original code is on [this](https://github.com/vika-sonne/NevaMt3xx/) and [this](https://github.com/AlexObukhoff/neva-py3/) links.

Для связи со счетчиками Нева МТ существует еще одна [библиотека](https://github.com/nnemirovsky/pyneva/).

Исходный код проверялся на Python 3.10.7 под операционной системой Ubuntu 22.10.

## Основные изменение (general changes)
Исправлены все ошибки и предупреждения при исполнении исходного кода.
All warnings and errors are fixed.

Добавлена возможность подключения через TCP/IP сокет при схеме подключения счетчика, указанной ниже.
TCP/IP connection ability added.
