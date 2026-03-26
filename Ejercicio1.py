import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 8888))
s.listen(5)

print("Servidor escuchando en puerto 8888...")

client_socket, addr = s.accept()
print("Conexión desde:", addr)

data = client_socket.recv(1024)
print("Datos recibidos:", data.decode())

client_socket.send(b"Thank you for connecting")

client_socket.close()
s.close()