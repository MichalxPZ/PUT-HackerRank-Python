line = input().split()
ij = input().split()
suma=0
for i in range(int(ij[0]),int(ij[1])+1):
    suma+=int(line[i])
print(suma)