## Problem: Go-Back-N ARQ

### Definition

Implement **Go-Back-N ARQ** where the sender:

- Maintains a **sliding window** of outstanding frames.
- Can send multiple frames without waiting for each ACK.
- On timeout, retransmits from the **oldest unacknowledged** frame.

### Assumptions

- Fixed window size `N`.
- Frames and ACKs can be dropped (simulated).
- Cumulative ACKs acknowledge all frames up to a sequence number.

### Sample sequence

| Time | Event                      | Seq | Notes                     |
|------|----------------------------|-----|---------------------------|
| t0   | Send frames 0,1,2          |     | window size = 3           |
| t1   | ACK for 0,1 received       |     | base moves to 2           |
| t2   | Frame 2 or its ACK lost    | 2   | timeout will fire         |
| t3   | Timeout → resend 2,3,4,... |     | go back from frame 2     |

### Pseudocode (sender, simplified)

```text
base = 0
next_seq = 0
window_size = N

while there is data to send or unacked frames:
    if next_seq < base + window_size and there is data:
        send frame(next_seq)
        if base == next_seq:
            start timer
        next_seq += 1

    if ACK arrives:
        base = ack_seq + 1
        if base == next_seq:
            stop timer
        else:
            restart timer

    if timeout:
        restart timer
        resend all frames from base to next_seq-1
```

