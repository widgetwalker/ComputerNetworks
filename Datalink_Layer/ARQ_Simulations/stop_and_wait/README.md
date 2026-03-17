## Stop-and-Wait ARQ

### Table of contents

- [Programs](#programs)
- [How to run](#how-to-run)

### Programs

- **`stopsender.py` / `stoprecver.py`**: TCP-based stop-and-wait per character (seq 0/1)
- **`stop_and_wait_sender_udp.py` / `stop_and_wait_receiver_udp.py`**: UDP-based stop-and-wait with optional ACK dropping

### How to run

For the **TCP** version (terminal 1 then terminal 2):

```bash
python stoprecver.py
python stopsender.py
```

For the **UDP** version (terminal 1 then terminal 2):

```bash
python stop_and_wait_receiver_udp.py
python stop_and_wait_sender_udp.py
```

