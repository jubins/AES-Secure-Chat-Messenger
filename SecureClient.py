import socket, base64, os #importing 'socket' for connectivity, 'base64' for encoding and 'os' for generating key
from Crypto.Cipher import AES #imported AES from pyCrpto library

pad = lambda z: z + (32 - len(z) % 32) * '$' #creating padding for AES with block 32 and $ character
AES_Encode = lambda x, z: base64.b64encode(x.encrypt(pad(z))) #Encoder
AES_Decode = lambda x, e: x.decrypt(base64.b64decode(e)).rstrip('$') #Decoder

key = os.urandom(32) #generating a random 32bytes key
AES = AES.new(key) #applying AES encryption to that key

HOST = 'localhost' #Entering my own ip because here the server is my computer
PORT = 8001 #Entering same port as the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a TCP socket
s.connect((HOST, PORT)) #connecting to host and port
print ("Connected to Secure Server.") #Display if connection took place

while True: #Once connection eastabalished
    message = raw_input("[YouSecure]: ") #take input from user
    encrypt = AES_Encode(AES, message) #Encrypting the user input
    print 'Encrypted message sent:', encrypt #Displaying the encrypted message

    s.send(message) #seding message to the server
    decrypt = AES_Decode(AES, encrypt) #decrypting message
    data = s.recv(1024) #receiving data from server
    decrypt=data
    nodecrypt = decrypt
    print ('Decrypted message received from', decrypt) #displaying decrypted message