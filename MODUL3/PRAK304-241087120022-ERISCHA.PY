N = float(input("Masukkan Bilangan Bulat: ")) 
if N == 0: 
    print("Nol")
elif 1 <= N <= 9: 
    print("Satuan") 
elif N == 10 or 20 <= N <= 99: 
    print ("Puluhan") 
elif 11 <= N <= 19: 
    print("Belasan") 
else: 
    print("Anda Menginput Melebihi Limit Bilangan") 