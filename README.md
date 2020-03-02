# TCP Server Receiver Multithreading IPv4 / IPv6 & TCP Client Sender (PYTHON3)

TCP Server Message Receiver with Multithreading IPv4 / IPv6 and TCP Client Message Sender made in python3 to substitute netcat nc commands.

## How to run server and client:

	- Keep the server running in a terminal:
		python3 tcp_server_receiver
		
	- Run client into another terminal:
		python3 tcp_client_sender
		
	- See sent message containing thread log.

## Files:

### - tcp_server_receiver.py
	TCP Server Message Receiver with Multithreading and IPv6 / IPv4 to substitute netcat: nc -l -p [port]
	
### - tcp_client_sender.py
	TCP Client Message Sender to substitute netcat command: nc [server-ip-address] [port]
	
