import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(5)
conn, addr = sock.accept()

print 'connected:', addr

while True:
    data = conn.recv(1024).decode()
    if data.lower() == 'close':
        break
    if data:
        conn.send(data.upper().encode())

conn.close()