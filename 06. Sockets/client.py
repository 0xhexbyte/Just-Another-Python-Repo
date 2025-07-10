import socket
# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# define host and port
host = '127.0.0.1'
port = 9000

#connect
s.connect((host, port))