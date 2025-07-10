import socket

# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# define host and port
host = '127.0.0.1'
port = 9000

# setup socket bind
s.bind((host, port))

# listen for connection
s.listen()
conn, addr = s.accept()

# upon connection
print(f'Connection received from {addr}')
print(conn)