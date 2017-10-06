import time
from socket import *

# Sequence number of the ping message
pings = 0
#for pings in range(10):
while pings < 10:
    pings +=1
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)
    message = "Ping"
    address = ("127.0.0.1", 12000)

    start = time.time()
    clientSocket.sendto(message, address)
    try:
        data, server = clientSocket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print "Reply from " + address[0] + ":" , data, pings
        #print('%s %d %d' % (data, pings, elapsed)
        print "RTT: " + str(end - start)

    except timeout:
        print ('Request timed out')


