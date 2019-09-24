import time
import socket
import sys
print('setup server')
time.sleep(1)
#get the hostname,ip address from socket and set port
soc=socket.socket()
host_name=socket.gethostname()
ip=socket.gethostbyname(host_name)
port=1234
soc.bind((host_name,port))
print(host_name,'({})'.format(ip))
name=input('enter name: ')
soc.listen(1) #try to locate using socket
print('waiting for incoming connections...')
connection, addr = soc.accept()
print("received connection from ",addr[0],"(",addr[1],")\n")
print("connection established. connected from: {}, ({})".format(addr[0],addr[0]))
#get a connection from client side
clinet_name=connection.recv(1024)
clinet_name=clinet_name.decode()
print(clinet_name + 'has connected ')
print('press [bye] to leave the chat room')
connection.send(name.encode())
while True:
    message=input('me>')
    if message=='[bye]':
        message='chat you later'
        connection.send(message.encode())
        print("\n")
        break
    connection.send(message.encode())
    message = connection.recv(1024)
    message =  message.decode()
    print(clinet_name,'>',message)

