import socket                                           # Socket module provides socket operations and some related functions.


def get_IP():                                           #define a function to get the IP address
    hname = input("Enter the website address(URL):")    #take the host name - url as input
    try:                                                #test a for errors
        print(f"Hostname: {hname}")                     #print the host name
        print(f"IP: {socket.gethostbyname(hname)}")     #print the IP address of the host
    except socket.gaierror as error:                    #store the getaddrinfo error thrown, in the variable, error
        print(f"Invalid Hostname! Error is {error}")    #print the error


get_IP()
