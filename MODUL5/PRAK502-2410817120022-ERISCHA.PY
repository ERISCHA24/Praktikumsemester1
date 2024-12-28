def hitung(nilai1, nilai2): 
    return nilai1 + nilai2 
def mutlak(angka): 
    return abs(angka) 
def main(): 
    a, b, c, d = map(int, input().split()) 
    Hasil = hitung(c, d) - hitung(a, b) 
    print(mutlak(Hasil)) 
if __name__ == "__main__": 
    main() 