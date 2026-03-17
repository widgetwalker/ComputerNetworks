import argparse
import json
from pathlib import Path
from typing import Any, Dict, List


def load_events(path: Path) -> List[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def ascii_timeline(events: List[Dict[str, Any]]) -> None:
    """
    Print a simple ASCII timeline of sender/receiver events.
    """
    sender_line = []
    recv_line = []

    max_time = max(e["time"] for e in events)
    by_time: Dict[int, List[Dict[str, Any]]] = {t: [] for t in range(max_time + 1)}
    for e in events:
        by_time[e["time"]].append(e)

    for t in range(max_time + 1):
        sender_symbol = " "
        recv_symbol = " "
        for e in by_time[t]:
            role = e.get("role")
            etype = e.get("type")
            status = e.get("status")
            if role == "sender":
                if etype == "send":
                    sender_symbol = "S" if status == "ok" else "X"
                elif etype == "timeout":
                    sender_symbol = "T"
            elif role == "receiver":
                if etype == "ack":
                    recv_symbol = "A" if status == "ok" else "X"
        sender_line.append(sender_symbol)
        recv_line.append(recv_symbol)

    print("time:  ", "".join(str(t % 10) for t in range(max_time + 1)))
    print("sender:", "".join(sender_line))
    print("recv:  ", "".join(recv_line))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="ASCII timeline for ARQ events (optionally plots with matplotlib if available)."
    )
    parser.add_argument(
        "--from",
        dest="from_path",
        required=True,
        help="Path to JSON events file (e.g. examples/arq_example_sequence.json)",
    )
    args = parser.parse_args()

    events = load_events(Path(args.from_path))
    ascii_timeline(events)

    try:
        import matplotlib.pyplot as plt  # type: ignore[import]

        times = [e["time"] for e in events if e.get("type") in {"send", "ack"}]
        seqs = [e["seq"] for e in events if e.get("type") in {"send", "ack"}]
        kinds = [e["type"] for e in events if e.get("type") in {"send", "ack"}]

        colors = ["tab:blue" if k == "send" else "tab:green" for k in kinds]
        plt.scatter(times, seqs, c=colors)
        plt.xlabel("time")
        plt.ylabel("sequence number")
        plt.title("ARQ events timeline")
        plt.grid(True)
        plt.show()
    except ImportError:
        # matplotlib is optional; just skip plotting if not available
        pass


if __name__ == "__main__":
    main()

