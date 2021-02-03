def calc(n):
    tab = [0, 1]
    if n == 1:
        return tab[0]
    else:
        for i in range(1, n+1):
            tab.append(1 + tab[i + 1 - tab[tab[i]]])
        return tab[n]


def main():
    n = int(input())
    print(calc(n))


if __name__ == '__main__':
    main()
