"""
Tugas 3 - Simulasi Pesanan Masuk dengan Multithreading

Skeleton ini sengaja belum lengkap. Isi bagian bertanda TODO.
Jangan mengubah nama fungsi (dipakai untuk pengecekan otomatis oleh asisten).
"""

import threading
import random
import time

NUM_ORDERS = 100        # jumlah pesanan simulasi yang masuk
NUM_WORKERS = 10        # jumlah thread pekerja


# PILIH MODE YG SESUAI:
# False = tanpa lock
# True = dengan lock

USE_LOCK = False

# Counter bersama untuk menghitung total pesanan yang berhasil diproses.
# Sengaja rawan race condition jika diakses tanpa proteksi.
processed_count = 0

# TODO 1: Buat objek Lock di sini untuk melindungi `processed_count`.
lock = threading.Lock()


def process_order(order_id: int) -> None:
    """Proses satu pesanan. Dipanggil oleh tiap thread pekerja."""
    global processed_count

    # Simulasikan kerja nyata (mis. validasi, hitung total harga)
    time.sleep(random.uniform(0.001, 0.01))

    # TODO 2: Tambahkan increment `processed_count` DI SINI.
    if USE_LOCK:
        with lock:
            processed_count += 1
    else:
        current_count = processed_count
        time.sleep(0)
        processed_count = current_count + 1
    # Langkah 1: jalankan dulu tanpa lock (increment biasa: processed_count += 1)
    #            dan buktikan hasil akhirnya sering salah (< NUM_ORDERS).
    # Langkah 2: bungkus increment dengan `with lock:` dan buktikan hasilnya
    #            selalu tepat NUM_ORDERS. Simpan bukti kedua kondisi ini
    #            di JURNAL.md / folder bukti/.


def worker(order_ids: list) -> None:
    """Satu thread pekerja memproses sekumpulan order_id."""
    for order_id in order_ids:
        process_order(order_id)


def main() -> None:
    global processed_count
    
    processed_count = 0
    
    order_ids = list(range(1, NUM_ORDERS + 1))

    # TODO 3: Bagi `order_ids` menjadi NUM_WORKERS bagian, buat satu
    # threading.Thread per bagian yang menjalankan `worker(...)`,
    # start semua thread, lalu join semua thread sebelum lanjut.
    
    order_groups = [
        order_ids[i::NUM_WORKERS]
        for i in range(NUM_WORKERS)
    ]
    
    threads = []
    
    for group in order_groups:
        t = threading.Thread(
            target=worker,
            args=(group,)
        )
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(f"Mode Lock: {USE_LOCK}")
    print(f"Total pesanan diproses: {processed_count} (seharusnya {NUM_ORDERS})")

    if processed_count != NUM_ORDERS:
        print("RACE CONDITION TERDETEKSI!")
    else:
        print("counter sesuai dengan jumlah pesanan.")


if __name__ == "__main__":
    main()
