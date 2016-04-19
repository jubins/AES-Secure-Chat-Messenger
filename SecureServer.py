import sys,socket,select #importing 'sys' for read, write & error functions, 'socket' for creating TCP connection, 'select' for taking I/O calls

HOST = 'localhost' #Entering ip because here the server is my computer
PORT = 8001 #Giving any random port here
SOCK_LIST = [] #sockets

def Secure_chatServer(): #creating a Server function
    s =socket.socket(socket.AF_INET, socket.SOCK_STREAM) #object s for TCP server socket connection
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #associating connection with object s
    s.bind((HOST, PORT)) #binding the host and the port
    s.listen(5) #associating 5 connections

    SOCK_LIST.append(s) #adding socket to readable connections

    print "Chat server is up on " +HOST,PORT #Once the socket is created display the server status

    while True: #Creating a while loop
        ready_to_read,ready_to_write,in_error = select.select(SOCK_LIST,[],[],0) #getting list of sockets which are ready

        for sock in ready_to_read: #Once ready, check if readable
            if sock == s: #if yes, take value into temporary variable 'sock'
                sockfd, addr = s.accept() #accept the connection(s)
                SOCK_LIST.append(sockfd) #adding another socket as well as there will bemultiple connections
                print "User from IP: %s, %s joined the secure chat" %addr #Displaying host,port of joining user

            else: #if socket not readable, then the socket must be connected
                data = sock.recv(1024) #receive message and store in data
                if data: #if data is entered
                    broadcast(s, sock, '' + str(sock.getpeername()) + ': ' + data) #broadcasting it to all users
                else: #if data is not entered
                    if sock in SOCK_LIST: #check if the readable socket are there
                        SOCK_LIST.remove(sock) #if there then remove
    s.close() #closing the socket connection when loop ends

def broadcast (server_socket, sock, message): #Creating the broadcast function we used above, to send message to all cleints
    for socket in SOCK_LIST: #For all sockets in the list
        if socket != server_socket and socket != sock : #check if socket is from connected ones
            try : #if yes, using try
                socket.send(message) #send the message from socket
            except : #if no, using except
                socket.close() #if code is here then socket connection is broken
                if socket in SOCK_LIST: #if broken connection in list
                    SOCK_LIST.remove(socket) #remove that connection

if __name__ == "__main__": #if file being imported from another computer interpreter will set it to modules name
    sys.exit(Secure_chatServer()) #exit the chat server