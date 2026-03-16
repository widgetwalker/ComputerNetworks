import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 2222))
print("UDP Server is running... (type 'exit' to stop)")

try:
    while True:
        # Receive message from client
        data, addr = server_socket.recvfrom(1024)
        message = data.decode()
        print("Client:", message)

        # Exit condition
        if message.lower() == "exit":
            print("Client requested to close the connection.")
            break

        # Send reply to client
        reply = input("Server: ")
        server_socket.sendto(reply.encode(), addr)

        # Optional: allow server to exit
        if reply.lower() == "exit":
            print("Server shutting down.")
            break

finally:
    server_socket.close()
