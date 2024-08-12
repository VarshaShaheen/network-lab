import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
word = " "
host = socket.gethostname()
port = 8000

client_socket.connect((host, port))
data = client_socket.recv(1024)
print(data.decode('utf-8'))

word = input("Enter a word:")
client_socket.send(word.encode('utf-8'))

data = client_socket.recv(1024).decode('utf-8')
print("Word received from server:")
print(data)

client_socket.close()

