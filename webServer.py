# import socket module
from socket import *
# In order to terminate the program
import sys



def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)   # creates the socket
  
  #Prepare a server socket
  serverSocket.bind(("", port))   # binds socket to specific host and port
  
  #Fill in start
  serverSocket.listen(1)  # listens for a connection (socket is now in a listening state)
  #Fill in end

  while True:
    #Establish the connection
    
#    print('Ready to serve...')

    # accepts incoming connections 
    connectionSocket, addr = serverSocket.accept()                            #                     Fill in start -are you accepting connections?     #Fill in end


    try:
      # receive/store client's request 
      message = connectionSocket.recv(1024)                                   #                     Fill in start -a client is sending you a message   #Fill in end    (.recv is a method that receives the data from client)
      filename = message.split()[1]    # parses 'message' into a list of words-- [1] is used b/c the first word is usually like GET, and the second is the requested link/filename
      
                                                                              #opens the client requested file. 
                                                                              #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], "r") #fill in start #fill in end)   # 'open(...)' takes the parameters of what file to open and how to read it ("r" means only read the file)
      # ADD CONTENT = F.READ()?????????
                                                                              #fill in end
      

                                                                              #                     This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
                                                                              #                     Fill in start                                                                                                                                           
                                                                              #                    Content-Type is an example on how to send a header as bytes. There are more!
      outputdata = b"HTTP 1.1 200 OK\r\n"    # changed outputdata to the header of 200 ok
                                
                                                                              #                     Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
 
                                                                              #                      Fill in end
             
        # 
        # 
        # FIGURE OUT WHAT THE FOR AND SEND \R\N LINES MEAN!!!!!!!!
      appendedFile = ""     # initialize appendedFile as empty string
      for i in f: #for line in file 
                                                                              #Fill in start - append your html file contents #Fill in end 
        #connectionSocket.send(outputdata[i].encode())                           # changed outputdata to 'f'
        appendedFile += i   # appending each line of the file to variable appendedFile
        
        
      #Send the content of the requested file to the client (don't forget the headers you created)!
      # Fill in start
      connectionSocket.send(outputdata)
      connectionSocket.send(appendedFile.encode())
      connectionSocket.send("\r\n".encode())                            

      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    



    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      outputdataError = b"HTTP/1.1 404 Not Found\r\n" 
      #connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode('utf-8'))
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