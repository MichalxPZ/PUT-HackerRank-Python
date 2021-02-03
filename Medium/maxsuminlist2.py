def maxsum(lista):
    temp_sum = max_sum = lista[0]

    for i in lista[1:]:
        temp_sum = max(i, temp_sum + i)
        max_sum = max(0, max_sum, temp_sum)
    return max_sum


def main():
    lista = list(map(int, input().split()))
    print(maxsum(lista))


if __name__ == '__main__':
    main()
