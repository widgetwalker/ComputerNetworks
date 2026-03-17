## Lab 2 – ARQ comparison (Stop-and-Wait, Go-Back-N, Selective Repeat)

### Goals

- Compare three ARQ protocols for reliable data transfer.
- Observe retransmissions and ACK patterns.

### Pre-lab

- Read:
  - `python/03_reliable_data_transfer/PROBLEM.md`
  - Each ARQ subfolder `README.md` and `PROBLEM.md`.

### Tasks

1. **Run Stop-and-Wait**

   - Use the UDP version (`stop_and_wait_sender_udp.py` / `stop_and_wait_receiver_udp.py`).
   - Trigger a few losses if the program supports it.

2. **Run Go-Back-N**

   - Use the UDP sender/receiver pair.
   - Observe what happens when one packet or ACK is lost.

3. **Run Selective Repeat**

   - Use the UDP sender/receiver pair.
   - Observe how only missing frames are retransmitted.

4. **Optional visualization**

   - Inspect `examples/arq_example_sequence.json`.
   - Run:

     ```bash
     python python/03_reliable_data_transfer/tools/plot_ascii_timeline.py --from examples/arq_example_sequence.json
     ```

   - Sketch a similar timeline for one of your own runs.

### Questions

- Which protocol sends the fewest **retransmissions** for the same loss pattern?
- How does the **window size** influence utilization in Go-Back-N vs Selective Repeat?

