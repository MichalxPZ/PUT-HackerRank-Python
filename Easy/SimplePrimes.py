def primes(n):
    for i in range(2, n):
        czy_pierwsza(i)


def czy_pierwsza(liczba):
    dzielniki = 2
    for i in range(2, liczba - 1):
        if liczba % i == 0:
            dzielniki += 1
    if dzielniki == 2:
        print(liczba)


def main():
    primes(int(input()))


if __name__ == '__main__':
    main()