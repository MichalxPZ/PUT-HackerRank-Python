def przelej(a,b, c):
    obj = a + b
    obj = c/obj


def main():
    n = int(input())
    eliksiry = {}
    przelania = []
    for i in range(n):
        line = list(input().split())
        eliksiry[line[0]] = [int(line[1]), int(line[2]), int(line[3])]
    m = int(input())
    for i in range(m):
        przelania.append(list(input().split()))
    print(przelej_eliksiry(eliksiry, przelania))

    for i in range(int(input())):
        A, B = input().split()
        if eliksiry[A][]
