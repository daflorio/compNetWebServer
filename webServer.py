# import socket module
from socket import *
# In order to terminate the program
import sys

# NOTE: edited out a lot of prof's comments (like the 'fill in start/fill in end' comments) and added personal notes, including regular comments on how the code works/flows

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)   # creates the socket
  
  #Prepare a server socket
  serverSocket.bind(("", port))   # binds socket to specific host and port
  
  #Fill in start
  serverSocket.listen(1)  # listens for a connection (socket is now in a listening state)
  #Fill in end

  while True:
    #Establish the connection
    # accepts incoming connections 
    connectionSocket, addr = serverSocket.accept()                        

    try:
      # receive/store client's request 
      message = connectionSocket.recv(1024)     # (.recv is a method that receives the data from client)
      filename = message.split()[1]    # parses 'message' into a list of words-- [1] is used b/c the first word is usually like GET, and the second is the requested link/filename
             
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], "r")   # 'open(...)' takes the parameters of what file to open and how to read it ("r" means only read the file)

      # This variable can store the headers you want to send for any valid or invalid request.  
      # Fill in start    
      # outputdata stores the headers for a valid request (has the status line, content-type, server, and connection headers)                   
          # the 'b' means the string is represented as bytes                                                                                                                                                          
      outputdata = b"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\nServer: Apache/2.4.1 (Unix)\r\nConnection: keep-alive\r\n\r\n"
      # Fill in end

      bodyMessage = ""     # initialize bodyMessage as empty string (used for storing the body message of the html file)
      for i in f: #for line in file
          # appending each line in the file to the 'bodyMessage' variable
          bodyMessage += i      #Fill in start - append your html file contents #Fill in end 

      # send the content of the requested file to the client (don't forget the headers you created)!                                                                     
      finalMessage = outputdata + bodyMessage.encode()    # new variable finalMessage contains the headers and appends the contents of bodyMessage to add the body message of the html file to the headers to be sent out together as one message (.encode() encodes the bodyMessage string as bytes)
      connectionSocket.send(finalMessage)   # .send() sends data from one socket to another
        
      connectionSocket.close() #closing the connection socket
    
    # if the server can't find the file, then send 404 not found
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!

      #Fill in start
      # put 404 not found in outputdataError b/c that's the header used for invalid requests
      outputdataError = b"HTTP/1.1 404 Not Found\r\n" 
      connectionSocket.send(outputdataError)
      #Fill in end

      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

  #Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)