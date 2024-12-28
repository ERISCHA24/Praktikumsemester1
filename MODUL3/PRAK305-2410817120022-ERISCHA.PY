waktu = int(input("Masukan Jumlah Detik : ")) 
hari = waktu // 86400 
jam = (waktu % 86400) // 3600         
menit = (waktu % 3600) // 60   
detik = waktu % 60 
print(f"{hari} hari {jam}:{menit}:{detik}")