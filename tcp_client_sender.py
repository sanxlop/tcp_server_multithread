#!/usr/bin/python3

# -*- coding: utf-8 -*-
# TCP Client for sending messages
# to substitute netcat command: nc [server-ip-address] [port]

# IMPORTS
import socket
import time

# CONSTANTS AND VARIABLES
HOST = "::" # socket.AF_INET6
#HOST = "0.0.0.0" # socket.AF_INET
PORT = 33333
data = 'Mensaje enviado con fecha en ms: ' + str(time.time())

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

print("Sent: {}".format(data))
