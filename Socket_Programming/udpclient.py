import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 2222)
print("UDP Client is running... (type 'exit' to quit)")

try:
    while True:
        # Get user input
        msg = input("Client: ")
        client_socket.sendto(msg.encode(), server_address)

        # Exit condition
        if msg.lower() == "exit":
            print("Client shutting down.")
            break

        # Receive reply from server
        data, _ = client_socket.recvfrom(1024)
        print("Server:", data.decode())

finally:
    client_socket.close()
