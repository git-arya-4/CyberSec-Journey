import platform
import socket
import os
import psutil

print("--- System Information ---")
print(f"OS Type: {platform.system()}")
print(f"OS Version: {platform.release()}")

hostname = socket.gethostname()
print(f"IP Address: {socket.gethostbyname(hostname)}")

print(f"Username: {os.getlogin()}")

processes = len(psutil.pids())
print(f"Running Processes: {processes}")

disk = psutil.disk_usage('/')
print(f"Disk Usage: {disk.percent}% used of {disk.total // (2**30)}GB")

interfaces = list(psutil.net_if_addrs().keys())
print(f"Network Interfaces: {', '.join(interfaces)}")
print("-" * 26)
