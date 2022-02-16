import socket                                           # Socket module provides socket operations and some related functions.


def get_IP():                                           #define a function to get the IP address
    host = input("Enter the website address(URL):")     #take the host name - url as input
    try:                                                #test a for errors
        print(f"Hostname: {host}")                      #print the host name
        print(f"IP: {socket.gethostbyname(host)}")      #print the IP address of the host
    except socket.gaierror as error:                    #store the getaddrinfo error thrown, in the variable, error
        print(f"Invalid Hostname! Error is {error}")    #print the error


choice = "y"                                             #set choice to y initially
while choice == "y":
    get_IP()
    choice = input("\nEnter y to continue finding IP address or Press any key to exit!: ")
