# Project CATFISH (Cashflow Tracker and Finance Sharing)

## Meet The Team.

- Dito Syahputra (2106638053)
- Failasuf Indi Marsendy (2106750364)
- Maulana Bayu Risma Santoso Sari (2106750401)
- Mochammad Iqbal (2006531056)
- Ramanti Prajna Pratisthita (2106638495)

## Tautan Heroku APP
https://catfish-apps.herokuapp.com/

## The Story Behind Our Project

Pesatnya perkembangan teknologi kian mendorong manusia untuk dapat beradaptasi terhadapnya. Berbagai macam digitalisasi kian merambah ke tiap sudut kehidupan bermasyarakat melalui suatu gerakan bernama Transformasi Digital. Untuk dapat mencapai potensi penuh dari digitalisasi diperlukan kolaborasi seluruh stakeholder yang terlibat di dalamnya. Elemen masyarakat menjadi salah satu stakeholder terpenting yang menentukan arah perkembangan kehidupan di masa mendatang.

Masyarakat berperan aktif berkontribusi terhadap perkembangan zaman terlebih pada masa Post-Pandemic Era seperti sekarang. Semua negara berlomba untuk pulih lebih cepat dan bangkit lebih kuat dari yang seharusnya. Terutama, pada perekonomian bangsa yang sempat terjun ke arah jurang resesi global. Untuk bisa mengatasi hal tersebut, masyarakat dapat memulainya dari langkah terkecil sekalipun yakni dengan menumbuhkan financial-awareness pada diri masing-masing.

Financial-awareness atau kesadaran finansial merupakan sebuah kemampuan seorang individu dalam mengatur keuangannya dengan optimal. Hal ini dapat dimulai dengan melakukan pembukuan cashflow pribadi agar stabilitas finansial dapat terus terpantau dengan baik. Tentu dalam melakukan pembukuan cashflow sangat diperlukan alat yang komprehensif untuk mengolah data yang dimiliki masing-masing individu. Maka dari itu, dengan bangga kami mempersembahkan sebuah terobosan baru bernama Cashflow Tracker and Finance Sharing atau yang dikenal sebagai CATFISH.

CATFISH merupakan sebuah aplikasi berbasis web yang bertujuan untuk mempermudahkan user-nya untuk melakukan pembukuan dan tracking cashflow dirinya dalam beberapa waktu belakangan. CATFISH hadir di tengah urgensi masyarakat dalam menumbuhkan financial-awareness dalam dirinya. Kami berharap dengan hadirnya CATFISH dapat menjadi jawaban dan alat pendongkrak masyarakat untuk dapat lebih memahami seberapa penting pencatatan sistematis pemasukkan dan pengeluaran. Karena dengan mengetahui alur cash flow pribadi, masyarakat akan lebih memahami langkah finansial yang selanjutnya harus mereka lakukan. Selain itu, CATFISH juga memiliki fitur Article Sharing yang berisi tips and trick seputar finansial dan manajemen keuangan yang tentu akan semakin membantu masyarakat dalam mengatur keuangannya.

## Our Modules

Daftar modul yang akan diimplementasikan:

1. Account
- Dev: Mochammad Iqbal
- Deskripsi: Implementasi halaman dan fungsi register, login, dan logout
- Models: Django's Built-in User model
- Form: Username, Email, Password, Confirm Password
- AJAX: Mengecek apakah username atau email sudah digunakan dan mengecek apakah username dan password benar saat login
- Logout condition: Mengarahkan user ke form login
- Login condition: Hanya dapat melakukan logout dan tidak dapat mengakses halaman register dan login

2. Cash Flow
- Dev: Dito Syahputra, Maulana Bayu Risma Santoso Sari
- Deskripsi: Halaman untuk user mencatat pemasukan dan pengeluarannya
- Models: CashFlow
- Form: Nominal, Kategori (pengeluaran atau pemasukan), Tanggal, Deskripsi
- AJAX: Sebuah pop-up untuk menambahkan atau mengedit riwayat transaksi dan tombol untuk menghapus riwayat
- Logout condition: Mengarahkan user ke form login
- Login condition: Menampilkan daftar transaksi yang sudah dibuat

3. Article write
- Dev: Ramanti Prajna Pratisthita
- Deskripsi: Halaman untuk writer menambahkan sebuah artikel yang akan ditampilkan pada homepage
- Models: Article
- Form: Judul, Deskripsi
- AJAX: Sebuah pop-up untuk menambahkan atau mengedit artikel dan tombol untuk menghapus artikel
- Logout condition: Mengarahkan user ke form login
- Login condition: Menampilkan daftar artikel yang user sudah buat

4. Homepage
- Dev: Failasuf Indi Marsendy
- Deskripsi: Halaman tampilan awal web
- Models: Menggunakan models Article untuk menampilkan artikel dalam urutan waktu
- Form: -
- AJAX: Melakukan pemanggilan GET artikel di database untuk ditampilkan dalam bentuk preview cards
- Logout condition: Mengarahkan user ke home page
- Login condition: Menampilkan preview seluruh artikel yang ada

## User’s Roles

Register and Login Home Page
Untuk mempermudah akses user. CATFISH akan dibagi menjadi dua bagian yang membentuk application system yang saling terintegrasi dengan baik, yaitu Regular User dan Article Writer. User akan diarahkan ke home page yang memiliki fitur Register dan Login terpisah untuk masing-masing user. Baik Regular User maupun Article Writer dapat melakukan login setelah mendaftar terlebih dahulu pada home page tersebut.
Register
Sebelum menikmati fasilitas CATFISH, user mengisi form registrasi terlebih dahulu dengan menginput data pada empat buah form yaitu username, email, password, dan ulangi password. Kemudian user menekan tombol submit, apabila telah terverifikasi valid maka user akan kembali ke home page.
Login
Untuk masuk ke dalam fitur utama, user harus masuk ke halaman login terlebih dahulu, user diminta untuk menginput username dan password, apabila tervalidasi maka user dapat menikmati fasilitas CATFISH.

Regular User
Add history pengeluaran
CATFISH memberikan kemudahan bagi user untuk merekap pengeluaran dan pemasukan, dengan fitur ini user dapat menambahkan jumlah nominal baik pemasukan maupun pengeluaran. Selain itu untuk memperjelas track cash flow, user dapat menambahkan tanggal form tersebut dibuat beserta deskripsi dan judul form.
Delete History
Fleksibilitas merupakan salah satu yang kami tawarkan, dengan fitur ini user dapat menghapus history cash flow dengan mudah
Rekap Pengeluaran
Automasi yang ditawarkan CATFISH akan direalisasikan dalam fitur ini, user dapat melihat total pengeluaran per bulan beserta rinciannya yang terbagi sesuai kategori masing-masing.
Show Artikel
	CATFISH menghadirkan fitur yang saling terintegrasi di antara kedua jenis user, User Reguler dapat melihat artikel yang dibuat oleh Article Writer pada halaman homepage.


Article Writer
Add Artikel
CATFISH mewadahi user untuk memberikan informasi dengan mudah dan efisien, dengan fitur ini user dapat membuat artikel yang dapat dilihat oleh user hanya dengan menginput form.
Delete Artikel
Untuk menunjang fleksibilitas, user dapat menghapus artikel yang sudah dibuat dengan mudah dalam fitur ini.
Show Artikel
	User Article Writer dapat melihat timeline artikel yang telah dibuat oleh Article Writer lainnya pada halaman homepage.


Keterangan Tambahan
Baik User Reguler maupun Article Writer memiliki peran masing-masing dalam menggunakan aplikasi CATFISH (unique user role), artinya satu akun dari user hanya mengambil satu peran baik itu User Reguler maupun Article Writer, apabila user akan menikmati peran yang lain, user harus membuat akun yang baru pada role yang berbeda..

