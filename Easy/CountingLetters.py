def licznik(fraza):
    fraza = fraza.lower()
    tab = [0] * 26
    for i in range(len(fraza)):
        if ord(fraza[i]) > 96 and ord(fraza[i]) < 123:
            tab[ord(fraza[i]) - 97] += 1
    w = 0
    litera = 'a'
    for i in range(len(tab)):
        if tab[i] > w:
            litera = chr(i + 97)
            w = tab[i]
    return (litera)


fraza = input()
print(licznik(fraza))