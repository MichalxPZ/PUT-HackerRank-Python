def czy_takie_same(n):
    tab=[0]*n
    for i in range(n):
        tab[i]=input()
    aktualna=tab[0]
    for i in range(n):
        if aktualna!=tab[i]:
            return("False")
    return("True")

n=int(input())
print(czy_takie_same(n))