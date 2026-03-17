## Roadmap

Ideas for future improvements and contributions.

### Python experiments

- Socket basics:
  - Add IPv6 variants.
  - Add examples with non-blocking sockets or `select`.
- Duplex chat:
  - Add multi-client chat server (broadcast).
- Reliable data transfer:
  - Add experiments varying loss/timeout parameters and plotting throughput.
  - Add basic congestion-control style demo (slow start style simulation).
- Application layer:
  - Add simple HTTP client (manual request over sockets and using `requests`).
  - Add DNS lookup example (using `socket.getaddrinfo`).

### Packet Tracer labs

- Add labs focusing on:
  - Static vs dynamic routing.
  - NAT and PAT.
  - Simple ACL examples.

### Tooling / docs

- More lab sheets in `docs/` for each experiment.
- Screenshot gallery showing expected output and Wireshark traces (optional).

Contributions implementing any of these are welcome in any mainstream language
(Python, C, C++, Java, etc.) as long as there is a clear `README.md` and
`PROBLEM.md` explaining how to run and what to observe.

