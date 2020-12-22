def encrypt(n, slowo):
    shift = n % 26
    for i in slowo:
        if ord(i) < 97:
            if ord(i) - shift < 65:
                i = chr(ord(i) - shift + 26)
            else:
                i = chr(ord(i) - shift)
        else:
            if ord(i) - shift < 97:
                i = chr(ord(i) - shift + 26)
            else:
                i = chr(ord(i) - shift)
        print(i, end='')


def main():
    encrypt(int(input()), input())


if __name__ == '__main__':
    main()