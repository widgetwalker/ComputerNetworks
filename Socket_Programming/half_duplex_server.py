import socket

HOST = '127.0.0.1'
PORT = 65432

def start_half_duplex_server_input():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"Half-Duplex Server listening on {HOST}:{PORT}")
        
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")

            # --- 1. SERVER RECEIVES FIRST ---
            data = conn.recv(1024)
            if data:
                print(f"\n<< Client said: {data.decode()}")

            # --- 2. SERVER SENDS RESPONSE (User Input) ---
            response = input("Server, your turn to send. Enter message: ")
            conn.sendall(response.encode())
            print(f"Server sent: {response}\n")

            # --- 3. Communication cycle ends ---
            print("Half-Duplex exchange complete. Closing connection.")

if __name__ == '__main__':
    start_half_duplex_server_input()