import socket
import ssl

def run_server(host='0.0.0.0', port=5000):
    # Create the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    # Configure SSL Context
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")
    
    print(f"Server started on {host}:{port} (Single-threaded)")
    print("Waiting for connections...")
    
    try:
        while True:
            # Accept a connection
            client_conn, addr = server_socket.accept()
            print(f"Connected by: {addr}")
            
            # Wrap the socket with SSL
            secure_conn = context.wrap_socket(client_conn, server_side=True)
            
            try:
                # Receive data
                data = secure_conn.recv(1024).decode()
                if not data:
                    continue
                print(f"Received from client: {data}")
                
                # Send response
                response = f"Echo from Single-threaded Server: {data}"
                secure_conn.send(response.encode())
            except Exception as e:
                print(f"Error handling client: {e}")
            finally:
                secure_conn.shutdown(socket.SHUT_RDWR)
                secure_conn.close()
                print(f"Connection with {addr} closed.")
                
    except KeyboardInterrupt:
        print("\nServer stopping...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    run_server()
