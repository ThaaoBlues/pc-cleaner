from getpass import getuser

PRINTER_MODE_HEADER = 1 << 1
PRINTER_MODE_INFO = 1 << 2
PRINTER_MODE_WARNING = 1 << 3

VARIABLES = {
    '$(USERNAME)': getuser()
}

UNITS = {
    "e": 10 ** 17,
    "eb": 10 ** 17,
    "p": 10 ** 15,
    "pb": 10 ** 15,
    "t": 10 ** 12,
    "tb": 10 ** 12,
    "g": 10 ** 9,
    "gb": 10 ** 9,
    "m": 10 ** 6,
    "mb": 10 ** 6,
    "k": 10 ** 3,
    "kb": 10 ** 3,
    "b": 1,
    "": 1
}
