from socket import *

def local_ip():
	s = socket(AF_INET, SOCK_DGRAM)
	s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
	local_ip_address = s.getsockname()[0]
	return local_ip_address

def broadcast(txt):
	s = socket(AF_INET, SOCK_DGRAM)
	s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
	s.sendto(txt.encode("utf8"),('',12345))

broadcast(local_ip())

