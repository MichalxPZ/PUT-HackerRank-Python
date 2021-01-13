def przelej(a,b,c):
    s = a + b
    if s != 0:
        s = c/s
    else:
        s = 0
    return a*s, b*s


def przelej_eliksiry(eliksiry, przelania):
    for przelej in przelania:
        A = eliksiry[przelej[0]]
        B = eliksiry[przelej[1]]
        zawartosc_A = A[0] + A[1]
        zawartosc_B = B[0] + B[1]
        pojemnosc_B = B[2]
        pojemnosc_A = A[2]
        if pojemnosc_B - zawartosc_B >= zawartosc_A:
            eliksiry[przelej[1]] = [B[0] + A[0], B[1] + A[1], pojemnosc_B]
            eliksiry[przelej[0]] = [0, 0, pojemnosc_A]
        else:
            a,b = przelej(eliksiry[0][0], eliksiry[0][1], (eliksiry[1][2] - eliksiry[1][1] - eliksiry[1][0]))
            eliksiry[przelej[0]][0] -= a
            eliksiry[przelej[0]][0] -= b
            eliksiry[przelej[1]][0] += a
            eliksiry[przelej[1]][0] += b
    nazwy_rosnaco = sorted(eliksiry.keys())
    ret = ''
    for nazwa in nazwy_rosnaco:
        ret = ret + str(eliksiry[nazwa][0]) + "\n"
    return ret


def main():
    n = int(input())
    eliksiry = {}
    przelania = []
    for i in range(n):
        line = list(input().split())
        eliksiry[line[0]] = [float(line[1]), float(line[2]), float(line[3])]
    m = int(input())
    for i in range(m):
        przelania.append(list(input().split()))
    print(przelej_eliksiry(eliksiry, przelania))


if __name__ == '__main__':
    main()
