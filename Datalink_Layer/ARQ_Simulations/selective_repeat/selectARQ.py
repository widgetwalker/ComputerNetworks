import socket

HOST = 'localhost'
PORT = 5001
BUFFER_SIZE = 1024
WINDOW_SIZE = 4

received_frames = {}
expected_base = 0
drop_count = {}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
print(f"🖥️ Server is listening on {HOST}:{PORT}...")

while True:
    data, addr = server_socket.recvfrom(BUFFER_SIZE)
    seq_num = int(data[:1])
    message = data[1:].decode()

    # Simulate error: drop frame 2 the first 3 times
    if seq_num == 2 and drop_count.get(seq_num, 0) < 3:
        drop_count[seq_num] = drop_count.get(seq_num, 0) + 1
        print(f"❌ Simulated error: dropping frame {seq_num} (attempt {drop_count[seq_num]})")
        continue

    if seq_num not in received_frames:
        received_frames[seq_num] = message
        print(f"✅ Received frame {seq_num}: {message}")
    else:
        print(f"🔁 Duplicate frame {seq_num} ignored")

    # Send ACK for the received frame
    ack = str(seq_num).encode()
    server_socket.sendto(ack, addr)

    # Deliver in-order frames
    while expected_base in received_frames:
        print(f"📦 Delivered frame {expected_base}: {received_frames[expected_base]}")
        del received_frames[expected_base]
        expected_base += 1
