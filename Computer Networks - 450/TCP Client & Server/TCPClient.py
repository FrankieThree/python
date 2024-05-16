##############################
# Assignment 2, TCPclient with http requests
# Frankie Cook, Jan. 2, 2024
# Python 3.8.10
##############################
from socket import *
import sys

# RETRIEVE PARAMETERS
host_ip = sys.argv[1]
port = sys.argv[2]
method = sys.argv[3]
filename = sys.argv[4]
# check if content exists
try:
    content = sys.argv[5]
except:
    content = ''
    
# establishes connection to host for http requests
def connect(host_ip, port, method, filename):
    # create client socket
    client_socket = socket(AF_INET, SOCK_STREAM)

    # set server IP address
    server_ip = host_ip
    # set server port number
    server_port = port

    # connect to server socket
    client_socket.connect((server_ip, int(server_port)))

    # generate message to send
    # request format: GET / HTTP/1.1\r\nHost:www.example.com\r\n\r\n
    url = host_ip
    if method.upper()=='GET':
        request = method.upper()+' /'+filename+' '+"HTTP/1.1\r\nHost:"+url+'\r\n\r\n'
    elif method.upper()=='POST':
        request = method.upper()+' /'+filename+' '+"HTTP/1.1\nHost:"+url+"\nData:"+f'"{content}"'
    elif method.upper()=='DELETE':
        request = method.upper()+' /'+filename+' '+"HTTP/1.1\nHost:"+url+'\n'

    # request to server
    print("HTTP request to server: \n"+request)
    # send message to server
    client_socket.send(request.encode())
    
    # receive message from server
    received_message = client_socket.recv(2048)
    print("HTTP response from server: \n{}".format(received_message.decode()))

    # close client socket
    client_socket.close()

connect(host_ip, port, method, filename)



