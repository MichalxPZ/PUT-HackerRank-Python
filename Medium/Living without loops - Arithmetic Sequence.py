line = input().split()
n = int(line[0])
k = int(line[1])
primal_n = n


def dosth(n, k):
    if n > 0:
        print(n, end=' ')
        n -= k
    else:
        k = -k
        print(n, end=' ')
        n -= k

    if n == primal_n:
        pass
    else:
        dosth(n, k)


dosth(n, k)
print(primal_n)