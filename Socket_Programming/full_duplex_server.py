import socket
import threading

HOST = '127.0.0.1'
PORT = 65433  # Use a different port to avoid conflicts

def receive_messages(conn):
    """Function to continuously receive messages from the client."""
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print("\nClient disconnected.")
                break
            # Use '>>' to clearly distinguish received messages
            print(f"\n<< Client: {data.decode()}", flush=True)
        except:
            break

def send_messages(conn):
    """Function to continuously send messages to the client."""
    while True:
        message = input() # Get input from the server user
        conn.sendall(message.encode())
        if message.lower() == 'bye':
            break

def start_full_duplex_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"Full-Duplex Server listening on {HOST}:{PORT}. Type 'bye' to exit.")
        
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}. Start typing...")

            # Start threads for simultaneous sending and receiving
            recv_thread = threading.Thread(target=receive_messages, args=(conn,))
            send_thread = threading.Thread(target=send_messages, args=(conn,))
            
            recv_thread.start()
            send_thread.start()
            
            # Wait for both threads to complete (e.g., when 'bye' is typed)
            send_thread.join()
            conn.close() # Close connection after send thread exits
            print("Server shutting down.")

if __name__ == '__main__':
    start_full_duplex_server()