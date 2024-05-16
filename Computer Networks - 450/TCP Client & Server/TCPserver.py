##############################
# Assignment 2, TCPserver with http requests
# Frankie Cook, Jan. 2, 2024
# Python 3.8.10
##############################
from socket import *
import os

# create server socket ("Welcoming Socket")
# AF_NET ~ Address
# SOCK_STREAM ~ Protocol to use
# 12000 ~ Port Number
# 1 ~ Server Socket Listen Forever
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('',12000))
server_socket.listen(1)
print("Server is ready to connect...\n")

# process get request
def get(filename):
    try:
        # try to open file in read mode (r)
        f = open(filename, 'r')
        # retrieve file contents
        content = f.read()
        f.close()

        # return success
        return "HTTP/1.1 200 OK\n\n"+content
    except:
        # err: return not found
        return 'HTTP/1.1 404 Not Found'

# process post request
def post(filename, content):
    try:
        # try to create file in create mode (x)
        f = open(filename, 'x')
        # retrieve file contents
        f.write(content)
        f.close()

        # return success
        return "HTTP/1.1 201 Created\n"+content+"\n"
    except:
        # err: return bad request
        return 'HTTP/1.1 400 Bad Request'

# process delete request
def delete(filename):
    try:
        # try to delete file
        os.remove(filename)

        # return success
        return "HTTP/1.1 204 No Content\n"
    except:
        # err: return not found
        return 'HTTP/1.1 404 Not Found'
    

# Forever Loop
while(True):
    # Accept Function Establishes Connection and Returns Address
    connection_socket, address = server_socket.accept()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("CONNECTION ESTABLISHED WITH {}\n".format(address))

    # Retrive message from socket
    # Message is in Bytes, so Decode
    incoming_request = connection_socket.recv(2048)
    print("Received Message: {}\n".format(incoming_request.decode()))

    # check parameters in request
    inputs = incoming_request.decode().split(' ')
    method = str(inputs[0])
    filepath = str(inputs[1][1:])

    # check method (GET, POST, DELETE)
    if method == 'GET':
        # call get method
        return_message = get(filepath)
    elif method == 'POST':
        # retrieve content, call post method
        content = incoming_request.decode().split('"')[1]
        return_message = post(filepath, content)
    elif method == 'DELETE':
        # call delete method
        return_message = delete(filepath)
       
    #return_message = inputs
    print(return_message)
    # Send message back to client
    connection_socket.send(return_message.encode())
    print("Message sent\n")

    # Close connection
    connection_socket.close()
