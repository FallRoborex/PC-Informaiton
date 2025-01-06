import psutil
import os
import platform
import socket
import cpuinfo


class SystemInfo:
    def __init__(self):
        self.os_info = None
        self.cpu_info = None
        self.disk_info = None
        self.ram_info = None

    def collect_cpu_info(self):
        cpu_physical_core = psutil.cpu_count(logical=False)
        cpu_logical_core = psutil.cpu_count(logical=True)
        cpu_percent = psutil.cpu_percent(interval=1)
        info = platform.processor()

        self.cpu_info = f"CPU Name: {info}\nCPU cores: Physical {cpu_physical_core} and Logical {cpu_logical_core}\nCPU percent: {cpu_percent}%"

    def collect_ram_info(self):
        # self.ram_info = psutil.virtual_memory()
        pass

    #
    def collect_all_info(self):
        self.collect_cpu_info()

    def __str__(self):
        self.collect_cpu_info()
        return f"{self.cpu_info}"


x = SystemInfo()

print(x)
