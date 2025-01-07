import subprocess

def scan_network():
    try:
        # `arp-scan` buyruqni ishga tushirish
        result = subprocess.run(
            ["sudo", "arp-scan", "--localnet"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Chiqish ma'lumotini qayta ishlash
        output = result.stdout
        devices = []

        # Chiqishni tahlil qilish
        for line in output.splitlines():
            if "192.168." in line:  # IP manzil mavjud bo'lgan qatorni tanlash
                parts = line.split()
                if len(parts) >= 2:
                    devices.append({"ip": parts[0], "mac": parts[1]})

        return devices

    except FileNotFoundError:
        print("arp-scan o'rnatilmagan. Iltimos, o'rnating.")
        return []
    except subprocess.CalledProcessError as e:
        print(f"Xatolik: {e}")
        return []

if __name__ == "__main__":
    devices = scan_network()
    if devices:
        print("Ulangan qurilmalar:")
        for i, device in enumerate(devices, start=1):
            print(f"{i}. IP: {device['ip']}, MAC: {device['mac']}")
    else:
        print("Qurilmalar topilmadi yoki ulanishda muammo bor.")
