from getpass import getuser
import os
from utils import printer, PRINTER_MODE_HEADER, PRINTER_MODE_WARNING, PRINTER_MODE_INFO

try:
    from pyfiglet import figlet_format
except ImportError:  # if not downloaded don't crash (because it is just style)
    printer("Figlet isn't install but it is optional.", PRINTER_MODE_WARNING)

    def figlet_format(message):
        return message


def main():
    printer(figlet_format("PC-CLEANER"))

    printer(f"Checking C:\\Users\\{getuser()}\\AppData\\Local\\Temp", PRINTER_MODE_HEADER | PRINTER_MODE_INFO)
    for ele in os.listdir(f"C:\\Users\\{getuser()}\\AppData\\Local\\Temp"):
        printer(f"Removing : {ele}")
        try:
            if os.path.isfile(ele):
                os.remove(ele)
            else:
                os.removedirs(ele)
        except:
            printer(f"No right to remove {ele}, retry in admin privileges", PRINTER_MODE_WARNING)

    printer(f"Checking C:\\Windows\\Temp\n", PRINTER_MODE_HEADER | PRINTER_MODE_INFO)
    for ele in os.listdir("C:\\Windows\\Temp"):
        printer(f"Removing : {ele}")
        try:
            if os.path.isfile(ele):
                os.remove(ele)
            else:
                os.removedirs(ele)
        except:
            printer(f"No right to remove {ele}, retry in admin privileges", PRINTER_MODE_WARNING)

    printer(f"Listing files wheighting over 1gb :", PRINTER_MODE_HEADER | PRINTER_MODE_INFO)

    walk("C:\\")
    printer(f"To make your PC run faster, try to check the app running in background parameters.",
            PRINTER_MODE_HEADER | PRINTER_MODE_WARNING)


def walk(uri):
    for root, directories, files in os.walk(uri):
        for file in files:
            if os.path.isfile(root + file):
                w = round(float(os.path.getsize(root + file) / 10 ** 9), 2)
                if w > 1:
                    print(f"{root + file}\n {file} weight {w}gb")

        for directory in directories:
            walk(str(root + "\\" + directory))


if __name__ == "__main__":
    main()
