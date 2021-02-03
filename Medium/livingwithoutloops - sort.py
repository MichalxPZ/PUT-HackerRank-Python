def srt(lista):
    res = ''
    if len(lista) == 1:
        return (res + ' ' + str(lista[0])).lstrip()
    else:
        a = min(lista)
        lista.remove(min(lista))
        return (res + ' ' + str(a) + ' ' + str(srt(lista))).lstrip()


def toInt(lista, i):
    x = lambda a: int(a)
    if i < len(lista):
        lista[i] = x(lista[i])
        toInt(lista, i+1)
    return lista


def main():
    lista = input().split()
    lista = toInt(lista, 0)
    print(srt(lista))


if __name__ == '__main__':
    main()
