# 🔐 Security & TLS

Encrypted socket communication implementing the TLS (Transport Layer Security) handshake and secure data transfer.

---

## 🛡️ Security Features
- **Asymmetric Encryption**: RSA keys for handshake.
- **Symmetric Encryption**: Session keys for data transfer.
- **Integrity**: MAC codes to prevent tampering.

---

## 📜 Components
- `generate_certs.py`: Script to generate self-signed SSL/TLS certificates.
- `server.crt` & `server.key`: Example certificate and private key.
- `server_single.py` & `server_multi.py`: Secure servers handling single and multiple clients.
- `client.py`: TLS-enabled client.

---

## 🔑 Certificate Setup
Before running the server, generate the credentials:
```bash
python generate_certs.py
```
This produces `server.crt` and `server.key` required for the handshake.
