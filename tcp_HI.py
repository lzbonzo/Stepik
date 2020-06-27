import socket
req = 'TCP HI!'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('0.0.0.0', 2222))
s.send(req.encode())
rsp = s.recv(1024)
s.close()
print('hi')