import time
import itertools

# Simulasi MAC address target (hanya untuk tampilan)
TARGET_MAC = 'DE:AD:BE:EF:00:01'

# Fungsi untuk generate kombinasi user/password dari keyword
def generate_credentials(keyword):
    credentials = set()

    # Kombinasi username/password sederhana
    credentials.add((keyword, keyword))
    credentials.add((keyword.lower(), keyword))
    credentials.add((keyword, keyword + '123'))
    credentials.add((keyword + '123', keyword))
    credentials.add((keyword[:3], keyword[::-1]))
    credentials.add((keyword[::-1], keyword[:3]))

    # Gabung kombinasi username dan password 1–2 kata
    for u, p in itertools.product([keyword, keyword.lower(), keyword.upper()], repeat=2):
        credentials.add((u, p))

    return list(credentials)

# Fungsi simulasi brute force
def try_mac_login_sim(mac, username, password):
    print(f"[+] Trying {username}:{password} on {mac}")
    time.sleep(0.1)  # simulasi delay
    return False  # ubah ke True jika ingin simulasi sukses

# Main program
def main():
    keyword = input("Masukkan keyword: ").strip()

    credentials = generate_credentials(keyword)
    print(f"[i] Generated {len(credentials)} username:password combinations.\n")

    for username, password in credentials:
        success = try_mac_login_sim(TARGET_MAC, username, password)
        if success:
            print(f"[✓] SUCCESS: {username}:{password}")
            break
    else:
        print("[x] Semua percobaan gagal.")

if __name__ == "__main__":
    main()
