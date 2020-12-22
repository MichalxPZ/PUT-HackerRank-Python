def najdluzszy_ciag(fraza):
    aktualna_dl = 0
    aktualna_litera = ''
    max_dl = 0
    max_litera = ''

    for i in range(len(fraza)):
        if fraza[i] == aktualna_litera:
            aktualna_dl += 1
        else:
            aktualna_litera = fraza[i]
            aktualna_dl = 1
        if aktualna_dl > max_dl:
            max_dl = aktualna_dl
            max_litera = aktualna_litera

    return (max_litera)


def main():
    print(najdluzszy_ciag(input()))


if __name__ == '__main__':
    main()
