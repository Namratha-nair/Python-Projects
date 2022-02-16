import socket                                               # Socket module provides socket operations and some related functions.

host = socket.gethostname()                                 #get the host name
port = 5555                                                 #initaiate to any port number above 1024 

mysocket = socket.socket()                                  #create an instance
mysocket.connect((host, port))                              #connect to the server

s_message = input("> ")                                     #take input
while s_message.lower().strip() != "bye":
    mysocket.send(s_message.encode())                       #send data
    r_message = mysocket.recv(1024).decode()                #receive data
    print("Received message: " + str(r_message))            #display the message in the terminal
    s_message = input("> ")                                 #take input again
mysocket.close()                                            #close connection
