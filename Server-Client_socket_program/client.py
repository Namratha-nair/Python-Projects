import socket


host = socket.gethostname()
port = 5555

mysocket = socket.socket()
mysocket.connect((host, port))

s_message = input("> ")
while s_message.lower().strip() != "bye":
    mysocket.send(s_message.encode())
    r_message = mysocket.recv(1024).decode()
    print("Received message: " + str(r_message))
    s_message = input("> ")
mysocket.close()
