## Problem: Selective Repeat ARQ

### Definition

Implement **Selective Repeat ARQ**, where:

- Sender keeps a window of unacknowledged frames.
- Each frame has its **own timer**.
- Only the missing frames are retransmitted when their timers expire.

### Assumptions

- Window size is less than half the sequence number space.
- Frames and ACKs can be dropped (simulated).
- Receiver buffers out-of-order frames and delivers in order to the application.

### Sample sequence

| Time | Event                 | Seq | Notes                         |
|------|-----------------------|-----|-------------------------------|
| t0   | Send 0,1,2,3          |     | window size = 4               |
| t1   | 0,1,3 received        |     | 2 lost, 3 buffered            |
| t2   | ACKs for 0,1,3 sent   |     | receiver waits for 2          |
| t3   | Timer for 2 expires   | 2   | sender retransmits frame 2    |
| t4   | Receiver gets 2       | 2   | now delivers 2,3 in sequence  |

### Pseudocode (sender, simplified)

```text
for each frame in window:
    if new:
        send frame
        start timer[seq]

if ack for seq arrives:
    mark frame seq as acknowledged
    stop timer[seq]

if timer[seq] expires:
    resend frame seq
    restart timer[seq]
```

