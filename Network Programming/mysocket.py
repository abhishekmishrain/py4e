import socket

cmd = 'GET HTTP://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('data.pr4e.org', 80))
sock.send(cmd)

while True:
    data = sock.recv(512)
    if len(data) > 0:
        print(data.decode(), end="")
    else:
        break

sock.close()
