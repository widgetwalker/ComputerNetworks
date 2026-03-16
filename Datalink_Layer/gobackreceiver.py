import socket

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
print(f"Receiver listening on {HOST}:{PORT}...")

received_frames = {}
total_frames = None
cumulative_ack = -1
sender_addr = None

while True:
    data, addr = server_socket.recvfrom(BUFFER_SIZE)
    msg = data.decode()
    sender_addr = addr

    if msg == "END":
        if total_frames is None:
            total_frames = len(received_frames)
            print("\nAll frames received. Now provide ACKs:")
        base = cumulative_ack + 1
        if base >= total_frames:
            server_socket.sendto(b"COMPLETE", sender_addr)
            print("All frames acknowledged. Transmission complete.")
            received_frames = {}
            total_frames = None
            cumulative_ack = -1
            continue

        print(f"\nProvide ACKs for pending frames starting from {base}:")
        new_cumulative = cumulative_ack
        for i in range(base, total_frames):
            choice = input(f"Send ACK for frame {i}? (y/n): ").strip().lower()
            if choice == "y":
                server_socket.sendto(str(i).encode(), sender_addr)
                print(f"ACK {i} sent")
                if i == new_cumulative + 1:
                    new_cumulative += 1
            else:
                print(f"No ACK for frame {i}")
                break
        cumulative_ack = new_cumulative

        if cumulative_ack >= total_frames - 1:
            server_socket.sendto(b"COMPLETE", sender_addr)
            print("All frames acknowledged. Transmission complete.")
            received_frames = {}
            total_frames = None
            cumulative_ack = -1
        else:
            server_socket.sendto(b"ACKROUND_DONE", sender_addr)
            print("Waiting for retransmissions...")
        continue

    seq_num, payload = msg.split(":", 1)
    seq = int(seq_num)
    received_frames[seq] = payload
    print(f"Received frame {seq}: {payload}")