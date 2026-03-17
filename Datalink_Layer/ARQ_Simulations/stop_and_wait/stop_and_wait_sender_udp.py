import socket
import time

HOST = '127.0.0.1'
PORT = 5050
TIMEOUT = 3

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender.settimeout(TIMEOUT)

# User input
items = input("Enter messages separated by commas: ")
messages = [x.strip() for x in items.split(",") if x.strip()]

seq = 0

for msg in messages:
    ack_received = False

    while not ack_received:
        packet = f"{seq}:{msg}"
        sender.sendto(packet.encode(), (HOST, PORT))
        print(f"Sent: {packet}")

        try:
            data, _ = sender.recvfrom(1024)
            ack = data.decode()

            if ack == f"ACK{seq}":
                print(f"ACK{seq} received")
                ack_received = True
                seq = 1 - seq
            else:
                print(f"Wrong ACK: {ack}, resending")

        except socket.timeout:
            print("Timeout, resending")

        time.sleep(1)

print("All messages sent.")
sender.close()
