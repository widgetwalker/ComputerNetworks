import socket
import threading
import time

SERVER_ADDR = ("127.0.0.1", 9999)
WINDOW_SIZE = 4
TIMEOUT = 10

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(TIMEOUT)

base = 0
next_seq_num = 0
lock = threading.Lock()
messages = []  # user-provided messages

def resend_packets():
    global base, next_seq_num
    while True:
        time.sleep(TIMEOUT)
        with lock:
            if base < next_seq_num:
                print("Timeout! Resending window...")
                for i in range(base, next_seq_num):
                    sock.sendto(f"{i}:{messages[i]}".encode(), SERVER_ADDR)

def sender():
    global base, next_seq_num
    threading.Thread(target=resend_packets, daemon=True).start()

    while True:
        msg = input("Enter message (or 'quit'): ")
        if msg.lower() == "quit":
            break
        messages.append(msg)

        with lock:
            while next_seq_num < base + WINDOW_SIZE and next_seq_num < len(messages):
                packet = f"{next_seq_num}:{messages[next_seq_num]}"
                print(f"Sending: {packet}")
                sock.sendto(packet.encode(), SERVER_ADDR)
                next_seq_num += 1

        try:
            data, _ = sock.recvfrom(1024)
            ack = int(data.decode())
            print(f"Received ACK: {ack}")
            with lock:
                base = ack + 1
        except socket.timeout:
            continue

if __name__ == "__main__":
    sender()
