import socket,base64,os #importing 'socket' for connectivity, 'base64' for encoding and 'os' for generating key
from Crypto.Cipher import AES #imported AES from pyCrpto library

pad = lambda z: z + (32 - len(z) % 32) * '$' #creating padding for AES with block 32 and $ character
AES_Encode = lambda x, z: base64.b64encode(x.encrypt(pad(z))) #Encoder
AES_Decode = lambda x, e: x.decrypt(base64.b64decode(e)).rstrip('$') #Decoder
key = os.urandom(16) #generating a random 16bit key (different than other clients)
AES_Encrypt = AES.new(key) #applying AES encryption to that key

HOST = 'localhost' #Entering my ip because here the server is my computer
PORT = 8001 #Entering same port as the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP socket creation
s.connect((HOST, PORT)) #connecting to host and port
print ("Connected to Secure Server.") #showing that client is connected
#only if connection happens then while loop
while True:#execute if connection happens
    plain_data = raw_input("[YouUnencrypted]: ") #input from the user
    encrypt = AES_Encode(AES_Encrypt,plain_data) #once the user sends text encrypting the input
    data = plain_data #storing encrypted data into another variable
    s.send(data) #seding message to the server
    s.recv(1024) #receiving the data
    print ('Message received from', encrypt) #displaying the un-decrypted message