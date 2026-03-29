import socket
import json

# Setup shards (simulated storage units)
NUM_SHARDS = 3
shards = [{"shard_id": i, "data": {}} for i in range(NUM_SHARDS)]

def get_shard_index(key):
    # Hash function to distribute keys
    return sum(ord(c) for c in key) % NUM_SHARDS

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5003))
server.listen(1)

print("[SHARDING SERVER] Cluster online on port 5003...")
conn, addr = server.accept()
print(f"[SHARDING SERVER] Master connected to client: {addr}")

while True:
    try:
        raw_data = conn.recv(1024).decode()
        if not raw_data or raw_data.lower() == 'exit': break
        
        # Expecting "COMMAND:KEY:VALUE"
        parts = raw_data.split(":")
        cmd = parts[0].upper()
        key = parts[1]
        
        shard_idx = get_shard_index(key)
        
        if cmd == "PUT":
            val = parts[2]
            shards[shard_idx]["data"][key] = val
            msg = f"STORED:{key} in Shard {shard_idx}"
        elif cmd == "GET":
            val = shards[shard_idx]["data"].get(key, "NOT_FOUND")
            msg = f"RETRIEVED:{val} from Shard {shard_idx}"
        else:
            msg = "ERROR:Invalid Command"
            
        print(f"[SHARDING SERVER] {cmd} {key} -> Shard {shard_idx}")
        conn.send(msg.encode())
    except Exception as e:
        print(f"Error: {e}")
        break

conn.close()
server.close()
print("[SHARDING SERVER] Cluster shut down.")
