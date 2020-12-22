def resistors():
    input()
    line = list(map(int, input().split()))
    suma = 0
    for i in line:
        suma += 1/i

    print(1/suma)


if __name__ == '__main__':
    resistors()
