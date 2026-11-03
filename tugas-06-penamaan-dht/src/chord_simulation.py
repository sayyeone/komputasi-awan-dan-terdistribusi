"""
Tugas 6 - Simulasi Chord DHT (single-process, tanpa jaringan sungguhan)

Fungsi hashing & struktur data ring sudah disediakan.
Lengkapi TODO untuk lookup(), join(), dan leave().
"""

import hashlib

M_BITS = 8               # ruang identifier 0..255 (disederhanakan dari Chord asli yang pakai 160-bit)
RING_SIZE = 2 ** M_BITS


def hash_id(key: str) -> int:
    """Hash string (ID node atau ID kurir) ke ruang identifier 0..RING_SIZE-1."""
    digest = hashlib.sha1(key.encode()).digest()
    return int.from_bytes(digest, "big") % RING_SIZE


class ChordRing:
    def __init__(self):
        # node_id (hasil hash) -> alamat IP node tersebut
        self.nodes: dict[int, str] = {}
        # key kurir (hasil hash) -> IP kurir yang disimpan node yang bertanggung jawab
        self.data: dict[int, tuple[str, str]] = {}  # hash -> (kurir_id, ip_kurir)

    def join(self, node_name: str, node_ip: str):
        node_id = hash_id(node_name)
        if node_id in self.nodes:
            return

        # Cari successor lama sebelum node baru ditambahkan.
        successor_lama = (
            self.find_successor(node_id) if self.nodes else None
        )

        # Catat key yang sebelumnya dipegang successor lama.
        key_lama = [
            key for key in self.data
            if self.find_successor(key) == successor_lama
        ]

        self.nodes[node_id] = node_ip

        for key in key_lama:
            if self.find_successor(key) == node_id:
                kurir_id, _ = self.data[key]
                print(
                    f"[JOIN] {kurir_id} (hash={key}): "
                    f"node {successor_lama} -> node {node_id}"
                )
        print(f"[TODO] Node '{node_name}' (id={node_id}) bergabung, alamat {node_ip}")

    def leave(self, node_name: str):
        node_id = hash_id(node_name)
        if node_id not in self.nodes:
            return

        if len(self.nodes) == 1 and self.data:
            print("Node terakhir tidak dapat keluar karena masih ada data.")
            return

        key_dipindahkan = [
            key for key in self.data
            if self.find_successor(key) == node_id
        ]

        del self.nodes[node_id]

        for key in key_dipindahkan:
            successor_baru = self.find_successor(key)
            kurir_id, _ = self.data[key]
            print(
                f"[LEAVE] {kurir_id} (hash={key}): "
                f"node {node_id} -> node {successor_baru}"
            )
        print(f"[TODO] Node '{node_name}' (id={node_id}) keluar dari ring")

    def find_successor(self, key_hash: int) -> int:
        if not self.nodes:
            raise ValueError("Ring masih kosong.")

        node_terurut = sorted(self.nodes.keys())

        for node_id in node_terurut:
            if node_id >= key_hash:
                return node_id

        return node_terurut[0]
        

    def register_kurir(self, kurir_id: str, ip_kurir: str):
        key_hash = hash_id(kurir_id)
        node_id = self.find_successor(key_hash)
        self.data[key_hash] = (kurir_id, ip_kurir)

        print(
            f"[REGISTER] {kurir_id} (hash={key_hash}) "
            f"-> {ip_kurir}, node penanggung jawab: {node_id}"
        )
        

    def lookup(self, kurir_id: str) -> str | None:
        key_hash = hash_id(kurir_id)
        node_id = self.find_successor(key_hash)
        mapping = self.data.get(key_hash)

        if mapping is None or mapping[0] != kurir_id:
            return None

        print(
            f"[LOOKUP] {kurir_id} (hash={key_hash}) "
            f"ditangani node {node_id}"
        )

        return mapping[1]
        


def main():
    ring = ChordRing()

    # Skenario awal: 4 node bergabung
    ring.join("node-jakarta-1", "10.0.0.1")
    ring.join("node-jakarta-2", "10.0.0.2")
    ring.join("node-bandung-1", "10.0.0.3")
    ring.join("node-surabaya-1", "10.0.0.4")

    # Daftarkan beberapa kurir
    ring.register_kurir("kurir-001", "192.168.1.10")
    ring.register_kurir("kurir-002", "192.168.1.11")
    ring.register_kurir("kurir-003", "192.168.1.12")
    ring.register_kurir("kurir-005", "192.168.1.15")
    ring.register_kurir("kurir-012", "192.168.1.22")

    print("\n--- Lookup sebelum perubahan topologi ---")
    print("kurir-001 ->", ring.lookup("kurir-001"))
    print("kurir-002 ->", ring.lookup("kurir-002"))

    print("\n--- Node baru bergabung ---")
    ring.join("node-medan-1", "10.0.0.5")
    print("kurir-001 ->", ring.lookup("kurir-001"))

    print("\n--- Sebuah node keluar ---")
    ring.leave("node-jakarta-1")
    print("kurir-001 ->", ring.lookup("kurir-001"))
    print("kurir-002 ->", ring.lookup("kurir-002"))


if __name__ == "__main__":
    main()
