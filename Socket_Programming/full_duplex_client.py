import socket
import threading
HOST = '127.0.0.1'
PORT = 65433

def receive_messages(s):
    """Function to continuously receive messages from the server."""
    while True:
        try:
            data = s.recv(1024)
            if not data:
                print("\nServer disconnected.")
                break
            # Use '>>' to clearly distinguish received messages
            print(f"\n<< Server: {data.decode()}", flush=True)
        except:
            break

def send_messages(s):
    """Function to continuously send messages to the server."""
    while True:
        message = input() # Get input from the client user
        s.sendall(message.encode())
        if message.lower() == 'bye':
            break

def start_full_duplex_client():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print(f"Connected to server on {HOST}:{PORT}. Type 'bye' to exit.")

            # Start threads for simultaneous sending and receiving
            recv_thread = threading.Thread(target=receive_messages, args=(s,))
            send_thread = threading.Thread(target=send_messages, args=(s,))
            
            recv_thread.start()
            send_thread.start()
            
            # Wait for the client's send thread to complete
            send_thread.join()
            s.close()
            print("Client shutting down.")

    except ConnectionRefusedError:
        print("Connection refused. Ensure the server is running.")

if __name__ == '__main__':
    start_full_duplex_client()