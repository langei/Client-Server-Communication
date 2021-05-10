import socket   #Imports socket library

clientSocket = socket.socket()  #Declares a socket object
host = '192.168.2.16'           #Server ID (IP of PC/server)
port = 12345                    #Port number


def decodeText(message):                        #Function to decode message from server
    decodedMessage = message.decode('utf-8')    #Decodes the encoded message
    return decodedMessage                       #Returns the decoded message

def encodeText(message):                        #Function to encode text
    encodedMessage = bytes(message, 'utf-8')    #Encodes the text
    return encodedMessage                       #Returns the encoded text

def clientReceive():                            #Function for client to loop and receive commands from server
    try:                                        
        while True:                                     #Loop runs until code is terminated               
            clientSocket.sendall(encodeText('0'))       #Confirmation message sent to server
            encodedMessage = clientSocket.recv(1024)    #Message received from server
            message = decodeText(encodedMessage)        #Message is decoded
            print('received: ' + str(message))          #Prints the message
    except ConnectionResetError:                        #Exception handling
        print('Host server has disconnected')
    except:
        print('Unknown error has occured')

def main():
    print('Waiting for connection')
    try:
        clientSocket.connect((host, port))      #Connects to the server
    except socket.error as e:                   #Excepts any errors           
        print(str(e))

    greeting = clientSocket.recv(1024)      #Recieves the server greeting message
    print(decodeText(greeting))             #Decodes the message

    clientReceive()                         #Runs the clientReceive function
    clientSocket.close()                    #Closes the socket

main()
