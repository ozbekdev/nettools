"""

Tarmoq Sozlamalari
Muallif - Ozbek Dev <ozbekdev@gmail.com>

"""

import time
import socket
import requests

# Ping o'lchash funksiyasi
def ping(host):
    try:
        start_time = time.time()
        socket.create_connection((host, 80), timeout=2)  # HTTP port (80) orqali ulanish
        end_time = time.time()
        return (end_time - start_time) * 1000  # millisekundda qaytariladi
    except socket.timeout:
        return None

# Download tezligini o'lchash funksiyasi
def download_speed(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        start_time = time.time()  # Yaratilgan vaqtni saqlaymiz
        response = requests.get(url, stream=True, headers=headers, timeout=30)  # Timeout va User-Agent qo'shildi

        total_downloaded = 0  # Yuklab olingan jami ma'lumotlar
        for chunk in response.iter_content(chunk_size=1024):  # 1KB bo'lib yuklab olish
            total_downloaded += len(chunk)  # Yuklab olingan ma'lumotlar sonini qo'shish

        end_time = time.time()  # Yakuniy vaqtni olish
        download_time = end_time - start_time  # Yuklab olish uchun sarflangan vaqtni hisoblash

        # Tezlikni hisoblash (Mbps) formatida
        download_speed_mbps = (total_downloaded * 8) / (download_time * 1_000_000)  # Mbps
        return download_speed_mbps

    except requests.exceptions.RequestException as e:
        print(f"Xato yuz berdi: {e}")
        return None

# Asosiy dastur
def main():
    # Pingni o'lchash
    ping_time = ping('aleph.uz')  # Pingni O'zimizni serverimizga yuboramiz
    if ping_time:
        print(f"Ping (USA): {ping_time:.2f} ms")
    else:
        print("Ping ishlamadi")

    # Download tezligini o'lchash
    # Serverdagi 10M hajmli faylni yuklab olib tekshiramiz
    url = 'https://www.aleph.uz/test.bin'
    speed = download_speed(url)
    if speed:
        print(f"Yuklab olish tezligi: {speed:.2f} Mbps")
    else:
        print("Yuklab olish tezligi o'lchanmadi")

# Dastur ishga tushiriladi
if __name__ == "__main__":
    main()
