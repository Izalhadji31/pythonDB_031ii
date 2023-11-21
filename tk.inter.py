import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

uiApp = tk.Tk()
uiApp.configure(background='black')
uiApp.geometry("500x500")
uiApp.resizable(False,False)
uiApp.title("Multiplatform kelas A")

#make canvas
inputFrame = tk.Frame(uiApp)
inputFrame.pack(padx=10,fill="x", expand=True)

#make label
inputLabel =ttk.Label(inputFrame, text="Ramalan Zodiak")
inputLabel.pack(padx=10, pady=10, fill="x", expand=True)

#1. Membuat Input Tanggal Lahir
labelInputTgl = ttk.Label(inputFrame, text="Masukan Tanggal Lahir Kamu")
labelInputTgl.pack(padx=10,pady=5, fill="x", expand=True)

entryInputTgl = ttk.Entry(inputFrame)
entryInputTgl.pack(padx=10,pady=5, fill="x", expand=True)

#2. Membuat Input Bulan Lahir
labelInputBln = ttk.Label(inputFrame, text="Masukan Bulan Lahir Kamu")
labelInputBln.pack(padx=10,pady=5, fill="x", expand=True)

entryInputBln = ttk.Entry(inputFrame)
entryInputBln.pack(padx=10,pady=5, fill="x", expand=True)

#3. Membuat Button
#membuat fungsi dialog
def klikButton():
    tanggalLahir = entryInputTgl.get()
    bulanLahir = entryInputBln.get()
    messagebox.showinfo("Ramalan Zodiak",
                        "Tanggal Lahir Kamu aladah: " + tanggalLahir +
                        ", Bulan Lahir Kamu aladah: " + bulanLahir +
                        "\n Ramalan Zodiak kamu : Kamu akan menikah dengan Zee JKT48")
    
buttonSubmit = ttk.Button(inputFrame, text="CEK RAMALAN ZODIAK KAMU SEKARANG!!1!1!1", command=klikButton)
buttonSubmit.pack(padx=10,pady=10, fill="x", expand=True)
uiApp.mainloop()