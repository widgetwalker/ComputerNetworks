import socket
import time

HOST = '127.0.0.1'
PORT = 5555
TIMEOUT = 3

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender.settimeout(TIMEOUT)

try:
    # User input
    items = input("Enter messages separated by commas: ")
    messages = [x.strip() for x in items.split(",") if x.strip()]
    
    if not messages:
        print("[ERROR] No messages entered")
        sender.close()
        exit(1)

    seq = 0
    max_retries = 5

    for msg in messages:
        ack_received = False
        retries = 0

        while not ack_received and retries < max_retries:
            packet = f"{seq}:{msg}"
            sender.sendto(packet.encode(), (HOST, PORT))
            print(f"[SENT] {packet} (attempt {retries + 1})")

            try:
                data, _ = sender.recvfrom(1024)
                ack = data.decode()

                if ack == f"ACK{seq}":
                    print(f"[ACK] ACK{seq} received")
                    ack_received = True
                    seq = 1 - seq
                else:
                    print(f"[ERROR] Wrong ACK: {ack}, resending")
                    retries += 1

            except socket.timeout:
                print(f"[TIMEOUT] No ACK received, resending")
                retries += 1

            time.sleep(0.5)
        
        if not ack_received:
            print(f"[FAILED] Message failed after {max_retries} retries: {msg}")

    print("[SUCCESS] All messages sent.")

except KeyboardInterrupt:
    print("\n[INTERRUPTED] Sender stopped")
except Exception as e:
    print(f"[ERROR] {e}")
finally:
    sender.close()
