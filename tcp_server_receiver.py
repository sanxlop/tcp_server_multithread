#!/usr/bin/python3

# -*- coding: utf-8 -*-
# TCP Server with Multithreading and IPv6/4
# to substitute netcat: nc -l -p [port]

# IMPORTS
import socket
import socketserver
import threading
import logging


# CONSTANTS AND VARIABLES
HOST = "::" # IPv4 and IPv6 machine
#HOST = "0.0.0.0" # IPv4 machine
PORT = 33333

# CLASS TCP SERVER MULTITHREADING
class TCPRequestHandler(socketserver.BaseRequestHandler):
    """Class for handling requests"""
    def handle(self):
        # Get data
        data = self.request.recv(4096) # Obtain data
        data_decoded = data.decode() # Decode bytes
        # Format string with data_decoded result and threads
        log_string = "{} {}\nFrom - Ip: {} Port: {}\n{}\n{}\n".format(threading.active_count(),
                                                                threading.enumerate(),
                                                                self.client_address[0],
                                                                self.client_address[1],
                                                                threading.current_thread().name,
                                                                data_decoded)
        print(log_string)

class ThreadedTCPServerIPv6(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """Class for adding multithreading and TCP server"""
    address_family = socket.AF_INET6 # Accept IPv4 and IPv6
    #address_family = socket.AF_INET # Accept just IPv4


# FUNCTIONS
def main():
    server = ThreadedTCPServerIPv6((HOST, PORT), TCPRequestHandler)
    server.serve_forever() # Activate server in main thread


# MAIN
if __name__ == "__main__":
    main()
