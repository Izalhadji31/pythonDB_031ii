import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
import sqlite3

# Fungsi untuk menyimpan data ke SQLite
def create_database_table():
    conn = sqlite3.connect("appdb.db")
    cursor = conn.cursor()

    # Buat tabel jika belum ada
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            biologi INT,
            fisika INT,
            inggris INT,
            prediksi_fakultas TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Fungsi untuk menentukan prediksi fakultas
def Hasil_prediksi_fakultas():
    nama_siswa = NAMA.get()
    biologi =(BIOLOGI.get())
    fisika =(FISIKA.get())
    inggris = (INGGRIS.get())
    
    if not all([nama_siswa,BIOLOGI.get(),FISIKA.get(),INGGRIS.get]):
        showerror("Eror", "Fieldnya harus diisi!")
        return
    if biologi > fisika and biologi > inggris:
        prediksi_fakultas = "Kedokteran"
        output_label.config(text=prediksi_fakultas)
    elif fisika > biologi and fisika > inggris:
        prediksi_fakultas = "Teknik"
        output_label.config(text=prediksi_fakultas)
    elif inggris > biologi and inggris > fisika:
        prediksi_fakultas = "Bahasa"
        output_label.config(text=prediksi_fakultas)
    elif biologi == fisika or biologi == inggris or inggris == fisika:
        prediksi_fakultas = "Bisa Memilih"
    else:
        showerror("Eror","Harap isi nilai yang benar!")
        return
    
    # Hitung prediksi fakultas
    showinfo("Hasil_prediksi_fakultas", f"Hasil_prediksi_fakultas untuk {nama_siswa}: {prediksi_fakultas}")
    try:
        conn = sqlite3.connect("appdb.db")
        cursor = conn.cursor()

        # Masukkan data ke tabel
        cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
        ''', (nama_siswa, biologi, fisika, inggris, prediksi))

        conn.commit()
        conn.close()
    
        showinfo("Selamat" ,"Data anda telah disimpan!")
    except sqlite3 as err:
        showerror("Error", f"Error: {err}")
        
    window = tk.TK()
    window.configure =(bg="gray")
    window.geometry("700x700")
    window.title("Test program")
    
    # Fungsi yang dijalankan saat tombol submit ditekan
def submit_nilai():
    nama_siswa = entry_nama.get()
    nilai_biologi = int(entry_biologi.get())
    nilai_fisika = int(entry_fisika.get())
    nilai_inggris = int(entry_inggris.get())

    # Simpan data ke database
    simpan_ke_database(nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris)

    # Kosongkan input setelah submit
    entry_nama.delete(0, tk.END)
    entry_biologi.delete(0, tk.END)
    entry_fisika.delete(0, tk.END)
    entry_inggris.delete(0, tk.END)

# Membuat GUI menggunakan tkinter
root = tk.Tk()
root.title("Prediksi Nilai Siswa")

label_nama = tk.Label(root, text="Nama Siswa:")
label_biologi = tk.Label(root, text="Nilai Biologi:")
label_fisika = tk.Label(root, text="Nilai Fisika:")
label_inggris = tk.Label(root, text="Nilai Inggris:")

entry_nama = tk.Entry(root)
entry_biologi = tk.Entry(root)
entry_fisika = tk.Entry(root)
entry_inggris = tk.Entry(root)

button_submit = tk.Button(root, text="Submit", command=submit_nilai)

label_nama.grid(row=0, column=0)
label_biologi.grid(row=1, column=0)
label_fisika.grid(row=2, column=0)
label_inggris.grid(row=3, column=0)

entry_nama.grid(row=0, column=1)
entry_biologi.grid(row=1, column=1)
entry_fisika.grid(row=2, column=1)
entry_inggris.grid(row=3, column=1)

button_submit.grid(row=4, column=0, columnspan=2)

root.mainloop()
