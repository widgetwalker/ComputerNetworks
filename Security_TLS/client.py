import socket
import ssl

SERVER_HOST = "localhost"  # change to your Kaggle server address or IP
SERVER_PORT = 8443

# for self-signed certificates, disable verification or load the server cert
context = ssl.create_default_context()
# context.check_hostname = False
# context.verify_mode = ssl.CERT_NONE

with socket.create_connection((SERVER_HOST, SERVER_PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=SERVER_HOST) as tls_sock:
        print(f"connected to {SERVER_HOST}:{SERVER_PORT} over TLS")
        tls_sock.sendall(b"Hello from client!")
        response = tls_sock.recv(4096)
        print(f"server replied: {response.decode()}")
