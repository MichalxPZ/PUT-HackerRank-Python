a = input()
a = a.split()
suma = 0
for i in range(int(a[0]),int(a[1])+1):
    suma = suma + i*i
print(suma)