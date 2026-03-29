import socket
import time

HOST = '127.0.0.1'
PORT = 5555
TIMEOUT = 10  # Stop listening after 10 seconds of no activity

receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
receiver.settimeout(TIMEOUT)
receiver.bind((HOST, PORT))

expected_seq = 0
received_messages = []

print(f"[LISTENING] Receiver ready on {HOST}:{PORT}")

try:
    while True:
        try:
            data, addr = receiver.recvfrom(1024)
            packet = data.decode()

            try:
                seq_str, msg = packet.split(":", 1)
                seq = int(seq_str)
            except ValueError:
                print("[ERROR] Corrupted packet received")
                continue

            print(f"[RECV] Packet {seq} from {addr}: {msg}")

            if seq == expected_seq:
                received_messages.append(msg)
                receiver.sendto(f"ACK{seq}".encode(), addr)
                print(f"[SENT] ACK{seq}")
                expected_seq = 1 - expected_seq

            else:
                last_ack = 1 - expected_seq
                print(f"[DUPLICATE] Packet {seq}, resending ACK{last_ack}")
                receiver.sendto(f"ACK{last_ack}".encode(), addr)
                print(f"[SENT] ACK{last_ack}")

            time.sleep(0.3)
        
        except socket.timeout:
            print("[TIMEOUT] No data received, closing receiver")
            break

except KeyboardInterrupt:
    print("\n[INTERRUPTED] Receiver stopped")
except Exception as e:
    print(f"[ERROR] {e}")
finally:
    print(f"[RECEIVED] Messages: {received_messages}")
    receiver.close()
