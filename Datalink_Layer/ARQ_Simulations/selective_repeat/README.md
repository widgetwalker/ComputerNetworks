## Selective Repeat ARQ

### Table of contents

- [Programs](#programs)
- [How to run](#how-to-run)

### Programs

- **`selectARQsender.py` / `selectARQ.py`**: UDP selective-repeat style demo (receiver simulates dropping frame 2 a few times)
- **`selective_repeat_sender_udp.py` / `selective_repeat_receiver_udp.py`**: UDP selective repeat with manual ACK drop prompts

### How to run

Run **receiver first**, then **sender**:

```bash
python selectARQ.py
python selectARQsender.py
```

Or:

```bash
python selective_repeat_receiver_udp.py
python selective_repeat_sender_udp.py
```

