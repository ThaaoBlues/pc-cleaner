import os

import default
from utils import printer, PRINTER_MODE_HEADER, PRINTER_MODE_WARNING, PRINTER_MODE_INFO, get_size

try:
    from pyfiglet import figlet_format
except ImportError:  # if not downloaded don't crash (because it is just style)
    printer("Figlet isn't install but it is optional.", PRINTER_MODE_WARNING)


    def figlet_format(message):
        return message


class Cleaner:
    def __init__(self):
        self.weight_limit, self.weight_unit = get_size(default.WEIGHT_NOTIFY_LIMIT)

    def clean(self):
        for path in default.TEMP_DIRS:
            printer(f"Checking {path}", PRINTER_MODE_HEADER | PRINTER_MODE_INFO)
            if os.path.exists(path):
                for ele in os.listdir(path):
                    printer(f"Removing : {ele}")
                    try:
                        if os.path.isfile(ele):
                            os.remove(ele)
                        else:
                            os.removedirs(ele)
                    except:
                        printer(f"No right to remove {ele}, retry in admin privileges", PRINTER_MODE_WARNING)
            else:
                printer(f"File/folder not found: {path} !", PRINTER_MODE_WARNING)

        printer(f"Listing files weighting over {default.WEIGHT_NOTIFY_LIMIT} :", PRINTER_MODE_HEADER | PRINTER_MODE_INFO)

        for path in default.SEARCH_PATHS:
            printer(f"Listing files weighting over {default.WEIGHT_NOTIFY_LIMIT} in {path}:",
                    PRINTER_MODE_HEADER | PRINTER_MODE_INFO)
            self.check_weight_directory(path)

        printer(f"To make your PC run faster, try to check the app running in background parameters.",
                PRINTER_MODE_HEADER | PRINTER_MODE_WARNING)

    def check_weight_directory(self, uri):
        for root, directories, files in os.walk(uri):
            for file in files:
                f = os.sep.join((root, file))
                if os.path.isfile(f):
                    w = os.path.getsize(f)
                    if w >= self.weight_limit:
                        printer(f"{f}\n {file} weight {w}{self.weight_unit}")

            for directory in directories:
                self.check_weight_directory(os.sep.join((root, directory)))


def main():
    printer(figlet_format("PC-CLEANER"))
    cleaner = Cleaner()
    cleaner.clean()


if __name__ == "__main__":
    main()
