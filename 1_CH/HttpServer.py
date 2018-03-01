'''
Author: Tayloc Cochran
Project: NATS
Goal:
  Rework the TCP server into an http server
'''

import socket



def to_bytes(bytes_or_str):
  '''
  Accepts a 8-bit or string and returns an 8-bit
  '''
  if isinstance(bytes_or_str, str):
    value = bytes_or_str.encode('utf-8')
  else:
    value = bytes_or_str
  return value


# host = socket.gethostbyname(socket.gethostname())
host = ''
port = 8888

http_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
http_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
http_socket.bind((host, port))
http_socket.listen(1)
print("[*] Serving HTTP on %s:%d" % (host, port))

while True:
  client_connection, client_address = http_socket.accept()
  request = client_connection.recv(1024)
  print("[*][*] Request - Start[*][*]")
  print("%s" % request)
  print("[*][*] Request - End [*][*]")

  http_response = '''\
HTTP/1.1 200 OK

Hello World!
  '''
  http_response = to_bytes(http_response)

  client_connection.sendall(http_response)
  client_connection.close()


