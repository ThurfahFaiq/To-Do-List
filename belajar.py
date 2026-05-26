
todo_list = []


def tambah_tugas():

    tugas = input("Masukkan tugas: ")

    data = {
        "tugas": tugas,
        "selesai": False
    }

    todo_list.append(data)

    print("Tugas berhasil ditambahkan")

\

def lihat_tugas():

    if len(todo_list) == 0:
        print("Belum ada tugas")
        return

    print("\n----- DAFTAR TUGAS -----")

    for i in range(len(todo_list)):

        status = "V" if todo_list[i]["selesai"] else "X"

        print(f"{i + 1}. [{status}] {todo_list[i]['tugas']}")


# FUNCTION HAPUS TUGAS
def hapus_tugas():

    if len(todo_list) == 0:
        print("Tidak ada tugas")
        return

    lihat_tugas()

    try:
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))

        if nomor <= 0 or nomor > len(todo_list):
            print("Nomor tidak valid")

        else:
            del todo_list[nomor - 1]
            print("Tugas berhasil dihapus")

    except:
        print("Input harus angka")


# FUNCTION TUGAS SELESAI
def tandai_selesai():

    if len(todo_list) == 0:
        print("Tidak ada tugas")
        return

    lihat_tugas()

    try:
        nomor = int(input("Masukkan nomor tugas yang selesai: "))

        if nomor <= 0 or nomor > len(todo_list):
            print("Nomor tidak valid")

        else:
            todo_list[nomor - 1]["selesai"] = True
            print("Tugas ditandai selesai")

    except:
        print("Input harus angka")


# FUNCTION TOTAL TUGAS
def total_tugas():

    total = len(todo_list)

    selesai = 0

    for tugas in todo_list:

        if tugas["selesai"] == True:
            selesai += 1

    belum = total - selesai

    print("\n----- TOTAL TUGAS -----")
    print("Total tugas :", total)
    print("Selesai     :", selesai)
    print("Belum selesai :", belum)


# MENU UTAMA
while True:

    print("\n" + "-" * 35)
    print("         TO DO LIST CLI")
    print("-" * 35)

    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Tandai Selesai")
    print("5. Total Tugas")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_tugas()

    elif pilihan == "2":
        lihat_tugas()

    elif pilihan == "3":
        hapus_tugas()

    elif pilihan == "4":
        tandai_selesai()

    elif pilihan == "5":
        total_tugas()

    elif pilihan == "6":
        print("Program selesai")
        break

    else:
        print("Menu tidak tersedia")