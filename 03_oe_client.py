import socket

# odd/even CLIENT

# client give snum
# check odd/evn
# send result back


HOST = '127.0.0.1'
PORT = 6099
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((HOST,PORT))


while True:
	text = input("Enter a number : ")
	if text=="c":
		break
	s.sendall(bytes(text, 'utf-8'))
	data = s.recv(1024)
	print("[Server] : ",text," is ",data.decode('utf-8'))
s.close()
