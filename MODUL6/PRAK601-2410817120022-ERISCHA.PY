baris, kolom = map(int, input().split())
isi = list(map(int, input().split()))
matrix = [[0 for _ in range(kolom)] for _ in
range(baris)]
index = 0
for i in range(baris):
    for j in range(kolom):
        matrix[i][j] = isi[index]
        index += 1
for i in range(baris):
    for j in range(kolom):
        print(matrix[i][j], end=" ")
    print()
