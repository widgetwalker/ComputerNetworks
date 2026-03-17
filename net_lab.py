import textwrap


def print_header(title: str) -> None:
    print("=" * len(title))
    print(title)
    print("=" * len(title))


def main() -> None:
    while True:
        print_header("Computer Networks Lab Toolkit")
        print("Select a module:")
        print("  1) Socket basics (TCP/UDP)")
        print("  2) Duplex chat")
        print("  3) Reliable data transfer (ARQ)")
        print("  4) Application layer (SMTP/FTP)")
        print("  q) Quit")
        choice = input("> ").strip().lower()

        if choice in {"q", "quit", "exit"}:
            break
        elif choice == "1":
            show_socket_basics()
        elif choice == "2":
            show_duplex_chat()
        elif choice == "3":
            show_arq()
        elif choice == "4":
            show_application_layer()
        else:
            print("Unknown choice. Please try again.\n")


def show_socket_basics() -> None:
    print_header("Socket basics")
    print(
        textwrap.dedent(
            """
            Concepts: TCP vs UDP, connection-oriented vs connectionless.

            To try TCP interactive chat (two terminals):

              # Terminal 1
              python python/01_socket_basics/tcp/tcpserver.py

              # Terminal 2
              python python/01_socket_basics/tcp/tcpclient.py

            To try UDP message exchange (two terminals):

              # Terminal 1
              python python/01_socket_basics/udp/udpserver.py

              # Terminal 2
              python python/01_socket_basics/udp/udpclient.py
            """
        )
    )


def show_duplex_chat() -> None:
    print_header("Duplex chat")
    print(
        textwrap.dedent(
            """
            Concepts: half-duplex vs full-duplex chat over TCP.

            Half-duplex (turn-based, server receives first):

              # Terminal 1
              python python/02_duplex_chat/half_duplex/half_duplex_server.py

              # Terminal 2
              python python/02_duplex_chat/half_duplex/half_duplex_client.py

            Full-duplex (threads, both sides can type any time):

              # Terminal 1
              python python/02_duplex_chat/full_duplex/full_duplex_server.py

              # Terminal 2
              python python/02_duplex_chat/full_duplex/full_duplex_client.py
            """
        )
    )


def show_arq() -> None:
    print_header("Reliable data transfer (ARQ)")
    print(
        textwrap.dedent(
            """
            Concepts: Stop-and-Wait, Go-Back-N, Selective Repeat.

            Run in this order to compare behavior (two terminals each time):

            1) Stop-and-Wait (UDP version)

              # Terminal 1
              python python/03_reliable_data_transfer/stop_and_wait/stop_and_wait_receiver_udp.py

              # Terminal 2
              python python/03_reliable_data_transfer/stop_and_wait/stop_and_wait_sender_udp.py

            2) Go-Back-N (UDP version)

              # Terminal 1
              python python/03_reliable_data_transfer/go_back_n/go_back_n_receiver_udp.py

              # Terminal 2
              python python/03_reliable_data_transfer/go_back_n/go_back_n_sender_udp.py

            3) Selective Repeat (UDP version)

              # Terminal 1
              python python/03_reliable_data_transfer/selective_repeat/selective_repeat_receiver_udp.py

              # Terminal 2
              python python/03_reliable_data_transfer/selective_repeat/selective_repeat_sender_udp.py
            """
        )
    )


def show_application_layer() -> None:
    print_header("Application layer (SMTP / FTP)")
    print(
        textwrap.dedent(
            """
            Concepts: application-layer protocols over sockets and libraries.

            1) SMTP socket simulation (localhost)

              # Terminal 1
              python python/04_application_layer/smtp_socket_sim/smtp_server.py

              # Terminal 2
              python python/04_application_layer/smtp_socket_sim/smtp_client.py

            2) SMTP using Ethereal test SMTP

              python python/04_application_layer/smtp_ethereal/smtp_ethereal_send.py

            3) FTP client (ftplib)

              python python/04_application_layer/ftp_client/ftp_client.py
            """
        )
    )


if __name__ == "__main__":
    main()

