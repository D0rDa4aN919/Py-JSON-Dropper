from platform import system
import ctypes

color = {
    "RED": '\033[31m',
    "GREEN": '\033[32m',
    "BLUE": '\033[34m',
    "MAGENTA": '\033[35m',
    "CYAN": '\033[36m',
    "BOLD": '\033[1m',
    "RESET": '\033[0m'
}

LIN = False
WIN = False
OS = system()
if OS == "Windows":
    WIN = True
elif OS == "Linux":
    LIN = True
else:
    print(f"{color['RED']}Not supported on this OS system...{color['RESET']}")
    exit(1)


def win_admin() -> bool:
    """
    Check if the user is administrator or regular user (Windows system only)
    :return: True/False
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except ctypes.WinError:
        return False


def lin_user(num: int = 0) -> bool:
    """
    Check if the user is root or regular user (Linux system only)
    :param num: integer number for control process
    :return: True/False.
    """
    from getpass import getuser
    if num == 1:
        if getuser() == "root":
            return False
        else:
            return True
    elif num == 0:
        if getuser() == "root":
            return True
        else:
            return False
