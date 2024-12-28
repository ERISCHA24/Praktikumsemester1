stop = int(input()) 
for i in range(1, stop + 1, 2): print(i, end=" ") 
print() 
for i in range(stop if stop % 2 == 0 else stop - 1, 1, -2): print(i, end=" ") 