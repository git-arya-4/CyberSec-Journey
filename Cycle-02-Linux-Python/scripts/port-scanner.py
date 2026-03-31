import socket
import sys
from datetime import datetime

target = input("Enter Target IP: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

print("-" * 50)
print(f"Scanning Target: {target_ip}")
print("-" * 50)

t1 = datetime.now()

try:
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port}: Open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.error:
    print("Could not connect to server.")
    sys.exit()

t2 = datetime.now()
total = t2 - t1

print("-" * 50)
print(f"Scanning Completed in: {total}")
print("-" * 50)
