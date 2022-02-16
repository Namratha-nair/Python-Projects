import socket

port = 5555
host = 'xxx.xx.xxx.xxx'  # enter server ip address

mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mysocket.bind((host, port))

while True:
    r_message, addr = mysocket.recvfrom(1024)
    r_message = r_message.decode('utf-8')
    if not r_message:
        break
    print("Message from: " + str(addr))
    print("You have a message: " + r_message)
    s_message = input("-> ")
    mysocket.sendto(s_message.encode('utf-8'), addr)
mysocket.close()
