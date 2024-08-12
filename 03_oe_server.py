import socket

# odd/even SERVER

# client give snum
# check odd/evn
# send result back


HOST ='127.0.0.1'
PORT= 6099

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((HOST,PORT))
s.listen(1)
conn,addr = s.accept()
print("Connecttedd ",addr)


#-----------------------

while True:
	data=conn.recv(1024)
	print("[Client ENtered] : ",data.decode('utf-8'))
	
	if int(data)%2==0:
		text = "Even !!"
	else:
		text = "Odd !!"
	
	conn.sendall(bytes(text, 'utf-8'))
conn.close()


	
	
	
