import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 7007

# Connect to the hostname on the specified port
s.connect((host, port))

# Receive no more than 1024 bytes
tm = s.recv(1024)
s.close()

print(f"The time received from the server is {tm.decode('ascii')}")
