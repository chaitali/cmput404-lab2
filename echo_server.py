#!/usr/bin/env python3

import socket

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
  # create socket
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   # s.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1) # make socket listen
    #listen forever
    while True:
      conn, addr = s.accept() #accept incoming connections
      full_data = b"" #create byte str
      while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
          break
        full_data += data
    # print(full_data)
        #send data back as a response
        conn.sendall(full_data)
    #q 1 limits response time to one ms

if __name__ == "__main__":
  main()
