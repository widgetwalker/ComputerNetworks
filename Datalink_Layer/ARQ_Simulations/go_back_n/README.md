## Go-Back-N ARQ

### Table of contents

- [Programs](#programs)
- [How to run](#how-to-run)

### Programs

- **`gobacksender.py` / `gobackreceiver.py`**: UDP Go-Back-N style demo with a fixed window and timeout
- **`go_back_n_sender_udp.py` / `go_back_n_receiver_udp.py`**: UDP Go-Back-N demo that can manually drop ACKs

### How to run

Run **receiver first**, then **sender**:

```bash
python gobackreceiver.py
python gobacksender.py
```

Or:

```bash
python go_back_n_receiver_udp.py
python go_back_n_sender_udp.py
```

