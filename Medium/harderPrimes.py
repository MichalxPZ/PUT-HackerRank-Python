from math import sqrt


def isPrime(tab):
    mx = max(tab)[0]
    sito = [x for x in range(2, mx+1)]
    for div in range(2, int(sqrt(mx))+1):
        k = div
        while k < mx:
            try:
                sito.remove(k)
            except:
                pass
            k = k + div
    for num in tab:
        if num[0] in sito:
            print("YES")
        else:
            print("NO")


def main():
    nums = [list(map(int, input().split())) for _ in range(int(input()))]
    isPrime(nums)


if __name__ == '__main__':
    main()
