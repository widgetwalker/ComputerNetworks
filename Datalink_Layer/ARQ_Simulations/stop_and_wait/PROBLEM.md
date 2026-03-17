## Problem: Stop-and-Wait ARQ

### Definition

Implement **Stop-and-Wait ARQ** where the sender:

- Sends **one frame at a time**.
- Waits for an ACK with the correct sequence number (0 or 1).
- Retransmits if ACK is lost or incorrect (timeout).

### Assumptions

- Sequence numbers alternate between 0 and 1.
- Channel may randomly drop data or ACK packets (simulated).
- Receiver sends an ACK for each correctly received frame.

### Sample sequence

| Time | Event                  | Seq | Notes             |
|------|------------------------|-----|-------------------|
| t0   | Sender sends frame     | 0   | first data        |
| t1   | ACK lost               | 0   | timeout will fire |
| t2   | Sender retransmits     | 0   |                   |
| t3   | Receiver sends ACK     | 0   | received ok       |
| t4   | Sender sends next      | 1   |                   |

### Pseudocode (sender)

```text
seq = 0
for each data_chunk:
    do:
        send frame(seq, data_chunk)
        start timer
        wait for ACK or timeout
    while timeout or ack_seq != seq
    seq = 1 - seq
```

