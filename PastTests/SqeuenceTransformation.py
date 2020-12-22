def sequenceTransformation(base, operations):
    longest = base
    for i in operations:
        i = i.split(";")
        mini = min(int(i[0]), int(i[1]))
        maxi = max(int(i[0]), int(i[1]))
        sub = str(i[2])
        base = base[:mini] + sub + base[maxi+1:]
        if len(longest) < len(base):
            longest = base
    result = base + "\n" + longest
    return result


def main():
    line = list(map(int, input().split()))
    N = line[0]
    M = line[1]
    base = input()
    operations = []
    for i in range(M):
        operations.append(input())
    print(sequenceTransformation(base, operations))


if __name__ == '__main__':
    main()
