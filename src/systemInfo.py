import psutil
import os
import platform
import socket


class SystemInfo:
    def __init__(self):
        self.info = {}

    def get_cpu_info(self) -> dict:
        try:
            return {"Model": platform.processor(),
                    "Percentage": psutil.cpu_percent(),
                    "Cores": {"Physical": psutil.cpu_count(logical=False), "Logical": psutil.cpu_count(logical=True)},
                    "Clock": {"Current": psutil.cpu_freq().current, "Min": psutil.cpu_freq().min, "Max": psutil.cpu_freq().max},}
        except Exception as e:
            return {"Error": str(e)}


    def get_ram_info(self):
        try:
            memory = psutil.virtual_memory()
            return {"Total": memory.total, "Used": memory.used, "Available": memory.available, "Percentage": memory.percent}
        except Exception as e:
            return {"Error": str(e)}

    def collect_all_info(self):
        self.info["CPU"] = self.get_cpu_info()
        self.info["RAM"] = self.get_ram_info()
        return self.info
