import socket


host = socket.gethostname()
port = 5555

mysocket = socket.socket()
mysocket.bind((host, port))

mysocket.listen(5)
conn, address = mysocket.accept()
print("Connection from: " + str(address))
while True:
    r_message = conn.recv(1024).decode()
    if not r_message:
        break
    print("Message received: " + str(r_message))
    s_message = input("> ")
    conn.send(s_message.encode())
conn.close()
