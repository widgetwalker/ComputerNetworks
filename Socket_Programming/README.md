# 🔌 Socket Programming

A collection of client-server architectures demonstrating fundamental network communication using Python's `socket` library.

---

## 🗂️ Categories

### 🔹 Basic TCP/UDP
- `tcpclient.py` & `tcpserver.py`: Connection-oriented reliable stream.
- `udpclient.py` & `udpserver.py`: Connectionless datagram service.

### 🔹 Duplex Communication
- `full_duplex_server.py` & `full_duplex_client.py`: Simultaneous two-way communication.
- `half_duplex_server.py` & `half_duplex_client.py`: Alternating communication (like walkie-talkies).

### 🔹 Exam Preparation
- `exam server.py` & `exam client.py`: Consolidated implementations for quick reference.

### 🔹 Integrated Lab Experiments
- [**ex1_single_thread**](./ex1_single_thread): Interactive single-threaded server/client.
- [**ex2_multi_thread**](./ex2_multi_thread): Multi-threaded server handling concurrent clients.
- [**ex3_cache_memory**](./ex3_cache_memory): Server-side caching simulation (Hit/Miss logic).
- [**ex4_hashing_sharding**](./ex4_hashing_sharding): Distributed data storing via hash-based sharding.
- [**ex5_http_requests**](./ex5_http_requests): REST API interaction using the `requests` library.
- [**01_socket_basics**](./01_socket_basics): Detailed TCP/UDP starting examples.
- [**02_duplex_chat**](./02_duplex_chat): Enhanced half/full duplex implementations.

---

## 📡 Architecture
![Socket Flow](https://www.testingdocs.com/questions/wp-content/uploads/Socket-Programming-in-Java.png)

---

## 🏃 Quick Start
```bash
# Terminal 1
python tcpserver.py

# Terminal 2
python tcpclient.py
```
