def dodaj(line):
    line = line.split()
    wynik = 0
    i = 0

    def jedziemy(line, i):
        nonlocal wynik
        if i < len(line):
            wynik += int(line[i])
            jedziemy(line, i + 1)

    jedziemy(line, i)
    print(wynik)


def main():
    dodaj(input())


if __name__ == '__main__':
    main()
