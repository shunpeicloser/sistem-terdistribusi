# Cara Uji Coba #
- Jalankan pyro nameserver.
  ```shell
    pyro4-ns -n localhost -p 50001
  ```
- Buat direktori untuk fileserver sesuai dengan nama fileserver. Pada pengerjaan ini digunakan nama fs1 dan fs2.
  ```shell
    mkdir fs1 fs2
  ```
- Jalankan server menggunakan file server.py dengan parameter masukan program merupakan nama fileserver. Pada pengerjaan ini digunakan nama fs1 dan fs2.
  ```shell
    python3 server.py fs1
  ```
- Jalankan shell script assign_fs_id.sh untuk men-set id dari tiap instance fileserver yang telah dibuat.
  ```shell
    bash assign_fs_id.sh
  ```
- Jalankan client.py untuk memulai menggunakan fileserver disertai dengan parameter nama fileserver yang diakses oleh client.
  ```shell
    python3 client.py fs1
  ```