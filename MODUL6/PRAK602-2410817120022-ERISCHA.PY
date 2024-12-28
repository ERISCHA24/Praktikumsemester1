Ruangan = int(input())
zetsuPutih = list(map(int, input().split()))
for i in range(Ruangan):
    print(zetsuPutih[i] * (i + 1), end=" ")