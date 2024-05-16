##############################
# Assignment 3, UDPclient with ping message
# Frankie Cook, Jan. 8, 2024
# Python 3.8.10 
##############################
# cd C:\Users\nfcoo\Documents\TMP
# python3 UDPClient.py 192.168.1.255 12000 5
from socket import *
from datetime import datetime
import sys

# Call: python UDPPingClient.py 192.168.1.6 12000 5
# n : number of pings
server_ip = sys.argv[1]
server_port = sys.argv[2]
n = int(sys.argv[3])

# variables
segments_sent = 0
segments_received = 0
segments_lost = 0
count = 1
rtt = []

# create client socket
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)
print("Pinging "+server_ip+":")

# number of pings
for ping_n in range(n):
    try:
        # generate message
        now = datetime.now()
        dt_str = now.strftime("%a %b %d %H:%M:%S %Y")
        message = "Ping "+str(count)+" "+dt_str

        # send message to server
        client_socket.sendto(message.encode(), (server_ip, int(server_port)))
        segments_sent += 1
        #print("Sent message: {}".format(message))

        # receive message from server
        recv_message, server_address = client_socket.recvfrom(2048)
        receive_time = datetime.now()
        segments_received += 1
        
        # round trip time in ms
        rtt_current = (receive_time-now).total_seconds()*1000
        rtt.append(rtt_current)

        # receive alert
        print("Reply from {}: {} time={:.1f}ms TTL={}".format(server_ip, recv_message.decode(), rtt_current, 1))
        count+=1
    except:
        segments_lost += 1
        print("Request timed out.")

# calculate ping statistics
segments_loss = 100 * segments_lost / segments_sent
if len(rtt) != 0:
    rtt_min = min(rtt)
    rtt_max = max(rtt)
    rtt_avg = sum(rtt) / len(rtt)
else:
    rtt_min = "EMPTY"
    rtt_max = "EMPTY"
    rtt_avg = "EMPTY"

# display ping statistics
print("\nPing statistics for "+server_ip+":")
segments_stats = "    Segments: Sent: {}, Received: {}, Lost: {} ({:.1f}% Loss)".format(segments_sent,segments_received,segments_lost,segments_loss)
print(segments_stats)
print("Approximate round trip times in ms:")
rtt_stats = "    Minimum = {:.1f}ms, Maximum = {:.1f}ms, Average = {:.2f}ms".format(rtt_min,rtt_max,rtt_avg)
print(rtt_stats)
    
# close client socket
client_socket.close()
