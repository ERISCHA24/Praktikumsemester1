kode = input().rstrip()
pesan = input().rstrip()
Bintang = 0
Pagar = 0
pesanTransformasi = ""
for i in range(len(kode)):
    if kode[i] == pesan[i]:
        pesanTransformasi += '*'
        Bintang += 1
    else:
        pesanTransformasi += '#'
        Pagar += 1
if len(kode) != len(pesan):
    print("Panjang kalimat berbeda, pesan palsu")
else:
    print(pesanTransformasi)
    print("* =", Bintang)
    print("# =", Pagar)
    if Bintang >= Pagar:
        print("Pesan Asli")
    else:   
        print("Pesan palsu")