import socket

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024

expected_seq = 0

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
print(f"🖥️ Server is listening on {HOST}:{PORT}...")

while True:
    try:
        data, addr = server_socket.recvfrom(BUFFER_SIZE)
        seq_num = int(data[:1])
        message = data[1:].decode()

        if seq_num == expected_seq:
            print(f"✅ Received frame {seq_num}: {message}")
            expected_seq += 1
        else:
            print(f"⚠️ Out-of-order frame {seq_num} (expected {expected_seq}) — discarding")

        # Send ACK for the last correctly received frame
        ack = str(expected_seq - 1).encode()
        server_socket.sendto(ack, addr)

    except Exception as e:
        print(f"❌ Error: {e}")
