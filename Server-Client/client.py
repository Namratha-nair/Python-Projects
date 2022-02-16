import socket

port = 5550
host = '172.30.226.200'  # client

server = ('172.30.226.205', 5555)
mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mysocket.bind((host, port))

s_message = input("-> ")
while s_message.lower().strip() != "bye":
    mysocket.sendto(s_message.encode('utf-8'), server)
    r_message, addr = mysocket.recvfrom(1024)
    r_message = r_message.decode('utf-8')
    print("You have a message: " + str(r_message))
    s_message = input("-> ")
mysocket.close()
