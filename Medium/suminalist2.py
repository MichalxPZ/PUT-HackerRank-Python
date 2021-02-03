def suminalist(list, a, b):
    return list[b+1] - list[a]


def main():
    lista = list(map(int, input().split()))
    n = int(input())
    list_pom = [0]
    for i in range(len(lista)):
        list_pom.append(lista[i] + list_pom[i])
    for _ in range(n):
        a, b = list(map(int, input().split()))
        print(suminalist(list_pom, a, b))


if __name__ == '__main__':
    main()
