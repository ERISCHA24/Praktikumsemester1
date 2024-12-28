while (True): 
    print("Pilih program") 
    print("1. Pertambahan") 
    print("2. Pengurangan") 
    print("3. Perkalian") 
    print("4. Pembagian") 
    print("5. Exit") 
    PROGRAM = int(input("Masukkan Pilihan : ")) 
    if PROGRAM == 5: break 
    if PROGRAM > 5 or PROGRAM < 0:  
        print("Input anda salah, silahkan coba lagi") 
        continue 
    a = float(input("Masukkan nilai pertama : ")) 
    b = float(input("Masukkan nilai kedua : ")) 
    if PROGRAM == 1:  
        print(f"Hasil penjumlahan antara {a:.2f} dan {b:.2f} adalah {a + b:.2f}") 
    elif PROGRAM == 2 : 
        print(f"Hasil pengurangan antara {a:.2f} dan {b:.2f} adalah {a - b:.2f} ") 
    elif PROGRAM == 3 : 
        print(f"Hasil perkalian antara {a:.2f} dan {b:.2f} adalah {a * b:.2f} ") 
    elif PROGRAM == 4 : 
        if b != 0: print(f"Hasil pembagian antara {a:.2f} dan {b:.2f} adalah {a / b:.2f} ") 
        else: print("Hasil pembagian tidak terdefinisi") 
print("Terima kasih, telah menggunakan kalkulator ERISCHA MARSELA") 