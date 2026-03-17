## Lab 1 – TCP vs UDP

### Goals

- Observe the difference between **TCP** and **UDP** communication.
- Run simple client/server programs and compare behavior.

### Pre-lab

- Read:
  - `python/01_socket_basics/README.md`
  - `python/01_socket_basics/PROBLEM.md`

### Tasks

1. **Run TCP chat**

   - Start the TCP server and client as described in the README.
   - Exchange a few messages.
   - Type `bye` to close the connection.

2. **Run UDP message exchange**

   - Start the UDP server and client.
   - Send a few short messages.
   - Type `exit` to stop.

3. **Answer questions**

   - What happens if you start the TCP client before the server?
   - If packets were lost, which protocol (TCP or UDP) would detect it automatically?
   - Which protocol keeps a connection state at the endpoints?

