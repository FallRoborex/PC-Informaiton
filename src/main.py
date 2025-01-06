import os
import psutil
import socket
import platform


def get_hostname_login():
    return os.getlogin(), socket.gethostname()


def get_os():
    operating_system = f"{platform.system()} {platform.release()} Version: {platform.version()}"
    return operating_system


def get_system_info():
    user_name, hostname = get_hostname_login()
    print(f"{user_name}@{hostname}")
    print(f"OS: {get_os()}")


get_system_info()
