import socket

HOST = '127.0.0.1'
PORT = 65432

def start_half_duplex_client_input():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print(f"Connected to server on {HOST}:{PORT}")

            # --- 1. CLIENT SENDS FIRST (User Input) ---
            message = input("Client, your turn to send. Enter message: ")
            s.sendall(message.encode())
            print(f"Client sent: {message}")

            # --- 2. CLIENT RECEIVES RESPONSE ---
            data = s.recv(1024)
            if data:
                print(f"\n<< Server replied: {data.decode()}")

            # --- 3. Communication cycle ends ---
            print("\nClient finished.")

    except ConnectionRefusedError:
        print("Connection refused. Ensure the server is running first.")

if __name__ == '__main__':
    start_half_duplex_client_input()