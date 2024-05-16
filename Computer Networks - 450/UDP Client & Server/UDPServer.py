##############################
# Assignment 3, UDPserver with ping message
# Frankie Cook, Jan. 8, 2024
# Python 3.8.10
##############################
from socket import *
import random

# create server socket
server_socket = socket(AF_INET, SOCK_DGRAM)
# bind server socket to port number
server_socket.bind(('', 12000))
print("Server is ready to receive messages...\n")

# run forever loop to keep receiving messages
while (True):
    # receive the message from socket
    message, client_address = server_socket.recvfrom(2048)
    #decode_message = message.decode()
    #print(decode_message)
    #print("message received\n")
    
    # timer variables
    #time = 2.0
    #ttl = 1
    #reply_message = "Reply from {}: {} time={}ms TTL={}".format(client_address,decode_message,time,ttl)

    # random drop, 4/10 messages not sent to client
    simulated_drop = random.random()
    chance = 0.4
          
    # send message back to client
    if simulated_drop >= chance:
        server_socket.sendto(message, client_address)
        print("Message sent")
    # or drop message
    else:
        print("Message dropped")
