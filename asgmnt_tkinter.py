import tkinter as tk 
 
def hasil_prediksi(): 
    output_label.config(text="Prodi Pilihan: Teknologi Informasi") #perintah untuk ouput
 
uiApp = tk.Tk() 
uiApp.configure(background='black')  #membuat warna
uiApp.geometry("700x700")  # Ubah ukuran jendela utama 
uiApp.resizable(False, False) 
uiApp.title('Aplikasi Prediksi Prodi Pilihan') #judul
 
# Membuat frame 
inputFrame = tk.Frame(uiApp) 
inputFrame.pack(padx=10, fill="x", expand=True) 
 
# Label Judul dengan ukuran font lebih besar 
judul_label = tk.Label(inputFrame, text="Aplikasi Prediksi Prodi Pilihan") 
judul_label.pack(pady=10) 
 
# 10 Input Nilai Mata Pelajaran 
input_label = tk.Label(inputFrame, text="Masukkan Nilai Mata Pelajaran") 
input_label.pack(pady=5) 
 
input_nilai = [] 
for i in range(10): 
    nilai_label = tk.Label(inputFrame, text=f"Mata Pelajaran {i + 1}:") #string
    nilai_label.pack() 
    nilai_entry = tk.Entry(inputFrame) 
    nilai_entry.pack() 
    input_nilai.append(nilai_entry) #nambah objek ke dalam list
 
# Button Hasil Prediksi 
button_prediksi = tk.Button(inputFrame, text="Hasil Prediksi", command=hasil_prediksi) 
button_prediksi.pack(pady=5) 
 
# Label Luaran Hasil Prediksi 
output_label = tk.Label(inputFrame, text="") 
output_label.config(wraplength=500) 
output_label.pack() 
 
uiApp.mainloop()