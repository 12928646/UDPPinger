import time
from socket import *

# Sequence number of the ping message
elapsedList = [] # Create an empty list
packetLossCount = 0
pings = 0
# Ping for 10 times
while pings < 10:
    pings +=1 # increment ping
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1) # wait up to 1 second for reply
    message = "Ping"
    address = ("127.0.0.1", 12000)

    start = time.time() # Sent time
    clientSocket.sendto(message, address) # Send the UDP packet with the ping message

    # If data is received back from server, print
    try:
        # Receive the server response
        data, server = clientSocket.recvfrom(1024) # buffer size is 1024 bytes
        end = time.time() # Received time
        elapsed = end - start
        elapsedList.append(elapsed)
        # Display the server response as an output
        print "Reply from " + address[0] + ":" , data, pings # Format the message to be sent
        print "RTT: " + str(end - start)  # Round trip time is the difference between sent and received time

    except timeout:
        # Server does not response
        # Assume the packet is lost
        packetLossCount = packetLossCount + 1
        print 'Request timed out for', 'PING', pings

print ("minimum:", min(elapsedList))
print ("maximum:", max(elapsedList))
print ("average RTTs:", sum(elapsedList)/len(elapsedList))
print ("Packet loss rate", (packetLossCount * 1.0/10 * 1.0)* 100.0, "%")



