import socket
import re
import requests
h = requests.get('https://instagram.com/roman_allaberdin')
q = re.findall(r'paiste',h.text)
print(q)

req = 'Hello TCP!'
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    if not data or data == 'close': conn.close()
    conn.send(data)
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()

