# 🌐 Computer Networks Lab

Welcome to the comprehensive repository for **Computer Networks** laboratory programs and simulations. This repository is organized by network layer and functionality, covering everything from Data Link Layer protocols to Application Layer services and Network Security.

---

## 📂 Repository Structure

| Category | Description |
| :--- | :--- |
| [**🛠️ Datalink Layer**](./Datalink_Layer) | Flow control and error control protocols (Stop & Wait, GBN, Selective Repeat, ARQ Simulations). |
| [**🔌 Socket Programming**](./Socket_Programming) | Core networking using TCP/UDP, Full/Half Duplex communication, and basic socket patterns. |
| [**✉️ Application Layer**](./Application_Layer) | Implementation of high-level protocols like SMTP and FTP. |
| [**⚡ Cisco Packet Tracer**](./Cisco_Packet_Tracer) | Network topology simulations and routing configurations (including extra lab topologies). |
| [**🔐 Security & TLS**](./Security_TLS) | Encrypted communication using SSL/TLS and certificate management. |
| [**🧠 Memcache Simulation**](./Memcache_Simulation) | Advanced simulation of distributed memory caching systems. |
| [**📄 Docs**](./Docs) | Comparative study of protocols and roadmap. |
| [**🧪 net_lab.py**](./net_lab.py) | Consolidated utility for laboratory network simulations. |

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.x**: Most programs are written in Python.
- **Cisco Packet Tracer**: Required to open `.pkt` files.
- **Libraries**: Some simulations might require additional packages.
  ```bash
  pip install -r Memcache_Simulation/requirements.txt
  ```

### How to Run
1.  **Clone the Repo**:
    ```bash
    git clone https://github.com/widgetwalker/ComputerNetworks.git
    cd ComputerNetworks
    ```
2.  **Run a Program**:
    Navigate to the specific folder and run the server/client scripts:
    ```bash
    # Example: Running a simple TCP Server
    cd Socket_Programming
    python tcpserver.py
    ```

---

## 🛠️ Technologies Used
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Cisco](https://img.shields.io/badge/cisco-049fd9?style=for-the-badge&logo=cisco&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

---

## 📊 Project Highlights
- **Layer-wise Organization**: Easy to navigate based on the OSI model.
- **Interactive Simulations**: Real-time visualization of data flow in Datalink protocols.
- **Secure Communication**: Hands-on examples of TLS handshake and encrypted data transfer.

---

<p align="center">
  <i>Created with ❤️ by <a href="https://github.com/widgetwalker">WidgetWalker</a></i>
</p>
