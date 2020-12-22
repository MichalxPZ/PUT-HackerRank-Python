N = int(input())
tab = list(map(int, input().split()))
def dif(tab, N):
    for i in range(N):
        for j in range(N):
            if tab[i]-tab[j] == 1 or tab[i]-tab[j]==-1:
                return('YES')
    return('NO')

print(dif(tab,N))