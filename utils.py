from constants import PRINTER_MODE_HEADER, PRINTER_MODE_INFO, PRINTER_MODE_WARNING


def printer(message, mode=0):
    if is_in(mode, PRINTER_MODE_HEADER):
        print(20 * "=")

    if is_in(mode, PRINTER_MODE_INFO):
        print("[+]", end=" ")
    elif is_in(mode, PRINTER_MODE_WARNING):
        print("[!]", end=" ")

    print(message)

    if is_in(mode, PRINTER_MODE_HEADER):
        print(20 * "=")


def is_in(settings, constants):
    return settings & constants == constants
