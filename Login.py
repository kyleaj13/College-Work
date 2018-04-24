import ctypes
import time
username = ""
password = ""

while username != "KYLE":
    username = input("Username: ").upper()
    if username != "KYLE":
        print("Username incorrect")
    else:
        while password != "password":
            password = input("Password: ")
            if password != "password":
                print("Password incorrect")
            else:
                print("Access granted")

