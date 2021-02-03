def rectangle(tab):
    maxRec = len(tab)
    for i in range(2,max(tab)):
        cnt = 0
        for j in range(len(tab)):
            if tab[j] >= i:
                cnt = 1
                while j + cnt < len(tab):
                    if tab[j+cnt] >= i:
                        cnt += 1
                    else:
                        break
                    maxRec = max(maxRec, cnt * i)
    return maxRec


def main():
    n = int(input())
    tab = []
    for _ in range(n):
        tab.append(int(input()))
    print(rectangle(tab))


if __name__ == '__main__':
    main()
