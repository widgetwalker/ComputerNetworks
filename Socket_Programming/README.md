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
