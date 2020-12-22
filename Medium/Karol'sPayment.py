N = int(input())
for i in range(N):
    line = list(map(int, input().split()))
    a = line[0]
    suma = 0
    M = line[1]
    dzien = 0
    while suma < M:
        suma += a * pow(2, dzien)
        dzien+=1
    print(dzien)