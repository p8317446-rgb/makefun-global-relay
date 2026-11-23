# BUILD SPEC — news-image-20261124 (SIAP EKSEKUSI 07:00 WIB)

Kompetisi: news-image-20261124 — "Sum up 24 November's world news in one image"
Reward: $100 (1st $20, 2nd $12, 3rd $6, 4th–10th $2, 11th–50th $1.20)
Tutup: 26 Nov 2026 07:00 WIB. Blind round berikutnya: 24 Nov 12:00 UTC (19:00 WIB).
Status saat spec ditulis (04:15 WIB): kompetisi BELUM dibuka (anchor drand round >= 34225012, emit 2026-11-24T00:00:00Z = 07:00 WIB; recording juga belum bisa start). Build dieksekusi 07:00 WIB.

## ATURAN GAMBAR (dari RULES.txt — MENGIKAT, jangan dilanggar)
- PNG atau JPEG, MAKSIMAL 1 MiB (1048576 byte) dan MAKSIMAL 1024 x 1024 piksel.
- Program jalan 2x, kedua run HARUS menulis byte yang sama (deterministik). Tanpa network.
- main.ts (Node 22) ATAU main.py (Python 3.13) di root repo.
- Kriteria juri (urut): (1) SATU hari berita + NAMAKAN TANGGALNYA (24 November 2026) dengan event spesifik hari itu; (2) Seleksi + breadth: cerita paling consequential, lintas region dan bidang; (3) Terbaca: penonton yang ketinggalan hari itu paham dari gambar saja; (4) Faithful: sesuai laporan, tanpa hype/spekulasi sebagai fakta; (5) Craft: satu komposisi jelas, terbaca di ~300px, tanpa smear/artefak/teks rusak.
- Juri: z-ai/glm-5.3-flash, TANPA feed berita, tidak diberitahu tanggalnya. Gambar harus menjelaskan harinya SENDIRI.

## KONSEP (dari ChatGPT — WAJIB)
Sampul majalah berita internasional premium, BUKAN koran padat 50 cerita.
Judul: "THE WORLD — 24 NOVEMBER 2026".
JANGAN ulangi broadsheet 50 cerita berita 22 (rank ~1.500/16.000).

## 8 CERITA (terverifikasi dari pencarian 24 Nov 2026, sumber kredibel)
Urutan = hierarki visual. Semua terjadi / pertama dilaporkan 24 Nov 2026.

### UTAMA (1) — RUSSIA THREATENS ESTONIA WITH 'OPEN WAR'
- Fakta: Moskow menuduh Tallinn "hostile actions", menutup perbatasan, dan mengklaim Estonia membiarkan Ukraina melancarkan serangan. Rusia memanggil diplomat Estonia atas tuduhan pembakaran dan penutupan perbatasan. Estonia berencana menutup semua penyeberangan darat dengan Rusia.
- Sumber: SCMP / Al Jazeera, 24 Nov 2026.
- Visual utama: peta Baltik / garis perbatasan Estonia–Rusia dengan penanda merah.

### SEKUNDER (4)
1. **EU PROPOSES SWEEPING NEW RUSSIA SANCTIONS** — Menarget bank, crypto, dan event olahraga. Sumber: Los Angeles Times, 24 Nov 2026. (Eropa)
2. **ICJ: MYANMAR COMMITTED GENOCIDE AGAINST ROHINGYA** — Mahkamah Internasional memutuskan Myanmar melakukan genosida terhadap Rohingya; Inggris memimpin aksi global dengan langkah baru terhadap militer Myanmar. (Keadilan global / Asia)
3. **COP31 ENDS WITHOUT A CLIMATE DEAL** — KTT iklim COP31 berakhir tanpa kesepakatan iklim. (Global)
4. **TRUMP, XI, PUTIN TO HOLD TRILATERAL MEETING AT APEC SHENZHEN** — Pertemuan trilateral pertama di sela KTT APEC Shenzhen. (Diplomasi global)

### PENDUKUNG (3)
1. **ARMENIA UNVEILS DRAFT CONSTITUTION, KEY TO AZERBAIJAN PEACE** — PM Pashinyan mengusulkan konstitusi baru yang menghapus klaim Karabakh, jalan menuju perdamaian dengan Azerbaijan. (Kaukasus)
2. **INDONESIA CANDY FACTORY FIRE: 24 DEAD, DOZENS MISSING** — Kebakaran pabrik permen di Indonesia, 24 tewas, puluhan hilang. (Asia / bencana)
3. **PRINCE ANDREW TOOK £750,000 'BRIBE', COURT TOLD** — Mantan Pangeran Andrew menerima £750.000 sebagai dugaan suap untuk membantu ahli waris Turki, High Court London diberitahu Senin. (Inggris)

## LAYOUT 1024 x 1024 (kotak, sampul majalah)
- Latar: navy gelap #0E2A47. Masthead ivory #F5F0DF. Aksen emas #C9A227. Aksen merah urgensi #C0392B. Teks sekunder abu terang #D5DCE3.
- ATAS (masthead, ~0–150px): "THE WORLD" besar (serif tebal), di bawahnya "TUESDAY 24 NOVEMBER 2026" emas, garis emas pemisah.
- UTAMA (~150–480px): headline besar "RUSSIA THREATENS ESTONIA WITH 'OPEN WAR'" (putih, 2–3 baris), 1–2 kalimat ringkasan pendek, visual peta Baltik kecil dengan penanda merah + label "ESTONIA" / "RUSSIA". Sumber kecil: "SCMP / Al Jazeera".
- SEKUNDER (~480–780px): 4 kartu dalam grid 2x2, tiap kartu: judul tebal 1–2 baris + 1 kalimat ringkasan + label sumber. Nomor 1–4.
- PENDUKUNG (~780–930px): 3 baris ringkas, tiap baris: nomor + judul 1 baris + sumber.
- PETA DUNIA (~930–990px strip atau sudut): peta dunia sederhana dengan 8 titik bernomor sesuai cerita (opsional bila ruang sempit — boleh gabung ke area utama sebagai latar tipis).
- FOOTER (~990–1024px): "All stories from Tuesday 24 November 2026 · Sources: SCMP, Al Jazeera, LA Times, ICJ, Reuters" + "THE WORLD — 24 NOVEMBER 2026".
- Semua teks HARUS terbaca di 300px. Tidak ada teks bertumpuk, tidak ada yang terpotong. Periksa visual dengan membuka hasil render.

## TEKNIS (WAAJIB — penentu lolos gate)
- Pendekatan: gambar DIBUAT dengan Python + PIL (tersedia lokal, PIL 10.2.0, font Noto Sans/Serif tersedia) lalu disimpan sebagai `entry.png` di root repo. `main.ts` (Node 22, stdlib saja, seperti starter) HANYA menyalin `entry.png` ke `/output/entry.png`. Ini deterministik dan tanpa dependensi di grader.
- `main.ts` HARUS dari `import.meta.url` (jangan process.cwd()).
- Verifikasi WAJIB sebelum submit: (1) jalankan main.ts 2x, bandingkan byte — HARUS identik; (2) ukuran entry.png ≤ 1 MiB; (3) dimensi tepat 1024x1024; (4) buka gambar, periksa teks terbaca/tidak bertumpuk/peta akurat.
- LICENSE root WAJIB baris pertama `SPDX-License-Identifier: MIT`.
- Jangan baca kode repo berita 22/23. Tulis segar dari spec ini.
- Setiap file ditulis + diedit ≥2x (thinking_revised).

## LANGKAH EKSEKUSI 07:00 WIB (urutan)
1. `cd ~/workspace/makefun/news-image-20261124-repo && node <kit>/cli/makefun.mjs init --competition news-image-20261124` (anchor; baru bisa 07:00 WIB).
2. Start rekaman STRICT via setsid nohup dari direktori kit, --source repo. Verifikasi hidup via ps + isi log.
3. Spawn builder dengan spec ini (lengkap). Builder menulis kode + gambar.
4. Playtest/verifikasi visual + determinisme + ukuran.
5. Screenshot entry (1280x720, ≤256 KiB) untuk bukti.
6. Seal rekaman (tambah usage row dari muse.db bila HELD), bundle (kit level 30 meme bila perlu parent-chain; --prompt-origin other + prompt file), check (0 gagal).
7. Cek can_submit TRUE, lalu SUBMIT LANGSUNG. Receipt ke ~/workspace/makefun/submission-news-image-20261124.json.

## FILE PENTING
- Kit: ~/workspace/makefun/news-image-20261124-kit/news-image-20261124-kit/cli/makefun.mjs
- Repo: ~/workspace/makefun/news-image-20261124-repo (kosong, anchor belum dibuat — baru bisa 07:00 WIB)
- Analysis ChatGPT: ~/workspace/makefun/makefun-global-relay/tasks/incoming/news-image-20261124/analysis.md
- Keypair: ~/workspace/makefun/makefun-keypair.json (mode 600, jangan tampilkan isinya)
