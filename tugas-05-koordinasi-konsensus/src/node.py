"""
Tugas 5 - Simulasi Node untuk Bully Algorithm

Infrastruktur jaringan (socket server/client) sudah disediakan.
Logika Bully Algorithm (bagian # TODO) harus kalian lengkapi sendiri.

Contoh menjalankan (5 terminal terpisah):
    python3 node.py --id 1 --port 5001 --peers 5002,5003,5004,5005
    python3 node.py --id 2 --port 5002 --peers 5001,5003,5004,5005
    ... dst untuk id 3, 4, 5
"""

import argparse
import socket
import threading
import time

ELECTION_TIMEOUT = 2.0  # detik menunggu balasan OK sebelum menyatakan diri leader


class Node:
    def __init__(self, node_id: int, port: int, peers: dict):
        self.node_id = node_id
        self.port = port
        # peers: dict {peer_id: peer_port} untuk semua node LAIN
        self.peers = peers
        self.leader_id = None
        self.lock = threading.Lock()
        self.election_running = False
        self.election_round = 0
        self.ok_received = threading.Event()

    # ---------- Infrastruktur jaringan (SUDAH LENGKAP, jangan diubah) ----------

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("localhost", self.port))
        server.listen()
        print(f"[Node {self.node_id}] Listening di port {self.port}")
        while True:
            conn, _ = server.accept()
            threading.Thread(target=self.handle_connection, args=(conn,), daemon=True).start()

    def handle_connection(self, conn: socket.socket):
        with conn:
            data = conn.recv(1024).decode()
            if not data:
                return
            sender_id, msg_type = data.split(":")
            self.on_message(int(sender_id), msg_type)

    def send_message(self, target_port: int, msg_type: str) -> bool:
        """Kirim pesan ke node lain. Return False jika node target tidak merespons (dianggap mati)."""
        try:
            with socket.create_connection(("localhost", target_port), timeout=1.0) as s:
                s.sendall(f"{self.node_id}:{msg_type}".encode())
            return True
        except (ConnectionRefusedError, socket.timeout, OSError):
            return False

    # ---------- Logika Bully Algorithm (LENGKAPI BAGIAN INI) ----------

    def on_message(self, sender_id: int, msg_type: str):
        """Dipanggil setiap kali node ini menerima pesan dari node lain."""
        if sender_id not in self.peers:
            return  
        if msg_type == "ELECTION":
            print(
                f"[Node {self.node_id}]"
                f"Menerima ELECTION dari node {sender_id}"
            )
            if self.node_id > sender_id:
                self.send_message(self.peers[sender_id], "OK")
                self.start_election()
        elif msg_type == "OK":
            with self.lock:
                if self.election_running and sender_id > self.node_id:
                    self.ok_received.set()
            print(
                f"[Node {self.node_id}]"
                f"Menerima OK dari node {sender_id}"
            )
        elif msg_type == "COORDINATOR":
            if sender_id < self.node_id:
                self.start_election()
                return

            with self.lock:
                self.leader_id = sender_id
                self.election_running = False
                self.election_round += 1
                self.ok_received.set()

            print(
                f"[Node {self.node_id}] "
                f"Leader sekarang: node {sender_id}"
            )

        elif msg_type == "PING":
            return
        
    def start_election(self):
        """Dipanggil saat node ini mendeteksi leader tidak ada / tidak merespons."""
        with self.lock:
            if self.election_running:
                return

            self.election_running = True
            self.election_round += 1
            current_round = self.election_round
            self.leader_id = None
            self.ok_received.clear()

        def election_worker():
            higher_peers = {
                pid: p
                for pid, p in self.peers.items()
                if pid > self.node_id
            }
            print(
                f"[Node {self.node_id}] "
                f"Mulai election ke peer lebih tinggi: {higher_peers}"
            )

            for peer_id, peer_port in higher_peers.items():
                with self.lock:
                    if current_round != self.election_round:
                        return

                print(
                    f"[Node {self.node_id}] "
                    f"Mengirim ELECTION ke node {peer_id}"
                )
                self.send_message(peer_port, "ELECTION")

            self.ok_received.wait(ELECTION_TIMEOUT)

            with self.lock:
                if current_round != self.election_round:
                    return

                received_ok = self.ok_received.is_set()

            if not received_ok:
                self.declare_leader()
                return

            print(
                f"[Node {self.node_id}] "
                "Menunggu pengumuman COORDINATOR"
            )

            coordinator_timeout = (
                len(self.peers) + 1
            ) * (ELECTION_TIMEOUT + 1)

            deadline = time.monotonic() + coordinator_timeout

            while time.monotonic() < deadline:
                with self.lock:
                    if current_round != self.election_round:
                        return

                time.sleep(0.1)

            with self.lock:
                if current_round != self.election_round:
                    return

                self.election_running = False

            print(
                f"[Node {self.node_id}] "
                "COORDINATOR belum diterima, mengulang election"
            )
          
            self.start_election()

        threading.Thread(
            target=election_worker,
            daemon=True
        ).start()        

    def declare_leader(self):
        """Node ini menyatakan dirinya leader dan memberi tahu semua node lain."""
        with self.lock:
            self.leader_id = self.node_id
            self.election_running = False
            self.election_round += 1

        print(f"[Node {self.node_id}] Saya menjadi LEADER")

        for peer_id, peer_port in self.peers.items():
            self.send_message(peer_port, "COORDINATOR")
            print(
                f"[Node {self.node_id}] "
                f"Mengirim COORDINATOR ke node {peer_id}"
            )

    def monitor_leader(self):
        """Loop periodik: cek apakah leader masih hidup, trigger election jika mati."""
        while True:
            time.sleep(3)

            with self.lock:
                leader = self.leader_id
                election_running = self.election_running

            if election_running:
                continue

            if leader is None:
                self.start_election()
                continue

            # Leader tidak perlu memeriksa dirinya sendiri.
            if leader == self.node_id:
                continue

            leader_port = self.peers.get(leader)
            alive = (
                leader_port is not None
                and self.send_message(leader_port, "PING")
            )

            if not alive:
                with self.lock:
                    # Pastikan belum ada pengumuman leader baru.
                    if self.leader_id != leader:
                        continue
                    self.leader_id = None

                print(
                    f"[Node {self.node_id}] "
                    f"Leader node {leader} tidak merespons"
                )
                self.start_election()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", type=int, required=True)
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("--peers", type=str, required=True,
                         help="daftar port peer dipisah koma, mis. 5002,5003,5004,5005")
    args = parser.parse_args()

    # Asumsi konvensi port: id N selalu di port 5000+N (lihat contoh perintah di README).
    peer_ports = [int(p) for p in args.peers.split(",")]
    peers = {port - 5000: port for port in peer_ports}

    node = Node(args.id, args.port, peers)

    threading.Thread(target=node.start_server, daemon=True).start()
    threading.Thread(target=node.monitor_leader, daemon=True).start()

    time.sleep(1)  # beri waktu semua node lain start dulu sebelum election awal
    node.start_election()

    while True:
        time.sleep(60)


if __name__ == "__main__":
    main()
