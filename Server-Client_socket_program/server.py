import socket                                           # Socket module provides socket operations and some related functions.


host = socket.gethostname()                             #get the host name
port = 5555                                             #initiate to any port number above 1024

mysocket = socket.socket()                              #create an instance
mysocket.bind((host, port))                             #bind host and port together

mysocket.listen(5)                                      #configure the server to listen to 5 clients simultaneously
conn, address = mysocket.accept()                       #accept new connection
print("Connection from: " + str(address))
while True:                                             #provide a forever loop until an error occurs
    r_message = conn.recv(1024).decode()                #data more than 1024 bytes won't be accepted
    if not r_message:                                   #if data is not received, berak
        break
    print("Message received: " + str(r_message))        #display the received message
    s_message = input("> ")
    conn.send(s_message.encode())                       #send data to the client
conn.close()                                            #close the connection
