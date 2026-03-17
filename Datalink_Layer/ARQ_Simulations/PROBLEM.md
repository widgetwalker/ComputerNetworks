## Problem: Reliable data transfer over unreliable channels

### Definition

Simulate **Automatic Repeat reQuest (ARQ)** protocols to achieve reliable delivery over an
unreliable channel:

- **Stop-and-Wait**
- **Go-Back-N**
- **Selective Repeat**

### Assumptions

- Underlying transport uses UDP or TCP on localhost.
- Packets or ACKs may be **lost** or **delayed** (simulated).
- Data is a small sequence of characters or frames.

### Example questions

- How many retransmissions occur when some ACKs are dropped?
- How does window size affect throughput in Go-Back-N and Selective Repeat?

See each subfolder’s `PROBLEM.md` for details and pseudocode.

