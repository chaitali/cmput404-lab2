#!/usr/bin/env python3

import socket

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

addr_info = socket.getaddrinfo("www.google.com", 80, proto=socket.SOL_TCP)
(family, socketype, proto, cannoname, sockaddr) = addr_info[0]


def main():
  # create socket
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   # s.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1) # make socket listen
    #listen forever
    while True:
      conn, addr = s.accept() #accept incoming connections
      print(conn)
      with conn:
        with socket.socket(family, socketype) as proxy_end:
	  #connect
          proxy_end.connect(sockaddr)
          print("connected") 
          full_data = b"" #create byte str
          while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
              break
            full_data += data
          proxy_end.sendall(full_data)
          full_data_from_google = b""
          while True:
            data = proxy_end.recv(BUFFER_SIZE)
            if not data:
              break
            full_data_from_google += data
    # print(full_data)
        #send data back as a response
        conn.sendall(full_data)
    #q 1 limits response time to one ms

if __name__ == "__main__":
  main()
