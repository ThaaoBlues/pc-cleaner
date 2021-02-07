import os
import optparse
import config
from utils import printer, PRINTER_MODE_HEADER, PRINTER_MODE_WARNING, PRINTER_MODE_INFO, get_size

try:
    from pyfiglet import figlet_format
except ImportError:  # if not downloaded don't crash (because it is just style)
    printer("Figlet isn't install but it is optional.", PRINTER_MODE_WARNING)


    def figlet_format(message):
        return message


class Cleaner:
    def __init__(self, parser):
        self.weight_limit, self.weight_unit = get_size(config.WEIGHT_NOTIFY_LIMIT)

        self.dry = parser.dry
        self.do_temp = parser.temp
        self.do_weight = parser.check_weight

    def clean(self):
        if self.do_temp:
            self.temp()
        if self.do_weight:
            self.weight()

    def weight(self):
        printer(f"Listing files weighting over {config.WEIGHT_NOTIFY_LIMIT} :", PRINTER_MODE_HEADER | PRINTER_MODE_INFO)
        for path in config.SEARCH_PATHS:
            printer(f"Listing files weighting over {config.WEIGHT_NOTIFY_LIMIT} in {path}:",
                    PRINTER_MODE_HEADER | PRINTER_MODE_INFO)
            self.check_weight_directory(path)
        printer(f"To make your PC run faster, try to check the app running in background parameters.",
                PRINTER_MODE_HEADER | PRINTER_MODE_WARNING)

    def temp(self):
        for path in config.TEMP_DIRS:
            printer(f"Checking {path}", PRINTER_MODE_HEADER | PRINTER_MODE_INFO)
            if os.path.exists(path):
                for ele in os.listdir(path):
                    if self.dry:
                        printer(f"Dry removing : {ele}")
                    else:
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
    parser = optparse.OptionParser(usage="pc-cleaner.py [options]")
    parser.add_option("-D", "--dry", action="store_true", default=False, dest='dry',
                      help="do not remove any file, just show the file that will be removed")

    group = optparse.OptionGroup(parser, "Actions Options", "List of features which can be do, by default all")
    group.add_option("-A", "--all", action="store_true", default=None, dest="all",
                     help="do all actions below")
    group.add_option("-T", "--temp", action="store_true", default=None, dest="temp",
                     help="remove temp file")
    group.add_option("-W", "--check-weight", action="store_true", default=None, dest="check_weight",
                     help="check the weight of files and warn if it is above the limit")

    parser.add_option_group(group)

    options, args = parser.parse_args()
    if options.all is True or (
            options.all is None and options.temp is None and options.check_weight is None):
        options.temp = True
        options.check_weight = True

    printer(figlet_format("PC-CLEANER"))
    cleaner = Cleaner(options)
    cleaner.clean()


if __name__ == "__main__":
    main()
