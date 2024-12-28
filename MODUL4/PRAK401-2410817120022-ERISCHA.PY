angka, simbol = input().split() 
angka = int(angka) 
i = 1 
while i <= 50: 
    if i % angka == 0: print(simbol, end=" ") 
    else: print(i, end = " ") 
    i+=1 