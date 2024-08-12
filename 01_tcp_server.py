#server:
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8000


server_socket.bind((host, port))

server_socket.listen(5)
print("Server listening on port :")
print(port)

while True:
    client_socket, addr = server_socket.accept()
    print("Got a connection from:")
    print(addr)

    client_socket.send(b"Thank you for connecting")

    data = client_socket.recv(1024).decode('utf-8')
    print("Received from client:" + data)

    data_upper = data.upper()

    client_socket.send(data_upper.encode('utf-8'))
    
    client_socket.close()
