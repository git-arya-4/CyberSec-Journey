import random
import string
import sys
import subprocess

length = int(input("Enter password length: "))
count = int(input("Enter number of passwords to generate: "))

chars = string.ascii_letters + string.digits + string.punctuation
passwords = []

for _ in range(count):
    pwd = "".join(random.choices(chars, k=length))
    passwords.append(pwd)
    print(pwd)

copy_choice = input("Copy the first password to clipboard? (y/n): ").lower()
if copy_choice == 'y':
    try:
        if sys.platform == "win32":
            subprocess.run("clip", input=passwords[0], text=True, check=True)
        elif sys.platform == "darwin":
            subprocess.run("pbcopy", input=passwords[0], text=True, check=True)
        else:
            subprocess.run(["xclip", "-selection", "clipboard"], input=passwords[0], text=True, check=True)
        print("Copied successfully.")
    except Exception:
        print("Clipboard error (Check if xclip is installed on Linux).")
