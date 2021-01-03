from constants import PRINTER_MODE_HEADER, PRINTER_MODE_INFO, PRINTER_MODE_WARNING, VARIABLES, UNITS


def printer(message: str, mode: int = 0) -> None:
    """
    Format and print the message.
    :param message: the message to print and format
    :param mode: how to format the message
    :return: None
    """
    if is_in(mode, PRINTER_MODE_HEADER):
        print(20 * "=")

    if is_in(mode, PRINTER_MODE_INFO):
        print("[+]", end=" ")
    elif is_in(mode, PRINTER_MODE_WARNING):
        print("[!]", end=" ")

    print(message)

    if is_in(mode, PRINTER_MODE_HEADER):
        print(20 * "=")


def is_in(settings: int, constants: int) -> bool:
    """
    If the bit(s) "constants" is/are on in "settings".
    :param settings: the holder of bits to test
    :param constants: the bit(s) to test
    :return: if the bit(s) is/are "settings"
    """
    return settings & constants == constants


def replace_variables(text: str) -> str:
    """
    Replace variables of a text defined by constants.py#VARIABLES.
    :param text: the text that hold or not variables
    :return: the text replaced
    """
    for v in VARIABLES:
        text = text.replace(v, VARIABLES[v])

    return text


def get_size(size: str) -> tuple:
    """
    Get what represent in bytes a string like 1Gb...
    :param size: the size with units
    :return: the size without units and the string unit
    """
    size = size.lower()
    for u in UNITS:
        if size.endswith(u):
            try:
                v = int(size[:-len(u)] if len(u) > 0 else size)
                return v * UNITS[u], size[-len(u):] if len(u) > 0 else size
            except ValueError:
                pass

    raise ValueError(f"Can't understand the unit: {size}")
