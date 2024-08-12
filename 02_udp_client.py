import socket
msgFromClient       = input("Enter a word: ")
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = (socket.gethostname(), 20001)
bufferSize          = 1024


UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Word from Server {}".format(msgFromServer[0])

print(msg)
