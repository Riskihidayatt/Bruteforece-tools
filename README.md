# 🛠️ Bruteforce_winbox
Bruteforce_winbox.py adalah tools simulasi brute force login ke perangkat MikroTik melalui MAC Winbox, menggunakan kombinasi username dan password yang dihasilkan dari keyword.

⚠️ Tools ini bersifat simulatif dan tidak benar-benar mengirimkan paket ke router. Ditujukan untuk edukasi dan pengujian sistem milik sendiri.

# 🗂️ Struktur File
bash
Salin
Edit
Bruteforce_winbox.py   # File utama script Python
✅ Prasyarat
Python 3.x

Tidak perlu menginstal library tambahan

# 🚀 Cara Penggunaan
#### 1. Simpan script dengan nama:
bash
Salin
Edit
Bruteforce_winbox.py
#### 2. Jalankan script:
bash
Salin
Edit
python Bruteforce_winbox.py
#### 3. Masukkan keyword:
bash
Salin
Edit
Masukkan keyword: mikrotik
Tools akan menghasilkan kombinasi username dan password berdasarkan keyword tersebut dan mencoba login (secara simulatif) ke MAC address target.

# 💡 Contoh Output
ruby
Salin
Edit
Masukkan keyword: mikrotik

[i] Generated 11 username:password combinations.
[+] Trying mikrotik:mikrotik on DE:AD:BE:EF:00:01
[+] Trying mikrotik:mikrotik123 on DE:AD:BE:EF:00:01
[+] Trying mikrotik123:mikrotik on DE:AD:BE:EF:00:01
...
[x] Semua percobaan gagal.
# ⚙️ Fitur
🔑 Generate username dan password otomatis dari satu keyword

🕗 Delay per percobaan untuk simulasi realistis

🧰 Siap dikembangkan menjadi tools MAC Winbox brute force sungguhan

💬 Output log setiap percobaan login

# 🔐 Legal & Etika
Hanya untuk pengujian sistem milik sendiri.

Akses ke perangkat tanpa izin melanggar hukum, termasuk UU ITE Indonesia.

Ini adalah simulasi, bukan serangan nyata.

# 🧩 Pengembangan Lanjutan
Untuk mengubah menjadi brute force nyata via MAC Winbox:

Gunakan scapy atau socket untuk crafting packet Layer 2.

Buat parser MNDP untuk menemukan MikroTik di jaringan lokal.

Implementasi challenge-response login sesuai protokol MikroTik Winbox.
