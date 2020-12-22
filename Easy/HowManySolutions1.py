def howmanysolutions(line):
    line = list(map(int, line.split()))
    n = line[0]
    x = line[1]
    y = line[2]
    a = 0
    b = 0
    c = 0
    d = 0
    solutions = 0
    for i in range(n+1):
        a = i
        for j in range(n+1):
            b = j
            for k in range(n+1):
                c = k
                for l in range(n+1):
                    d = l
                    if ((x * a * a) + (y * b * b)) ==(( x * c * c) + (y * d * d)):
                        solutions += 1
    print(solutions)


def main():
    howmanysolutions(input())


if __name__ == '__main__':
    main()
