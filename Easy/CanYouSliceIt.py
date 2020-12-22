def canyousliceit(line):
    line = line.split()
    for i in range(len(line)):
        line[i] = int(line[i])
    line = sorted(line)
    start = int(line[0])
    end = int(line[-1]) + 1
    step = 0
    if len(line) <= 2:
        return ('True')
    else:
        step = int(line[1]) - int(line[0])
        for i in range(1, len(line)):
            if int(line[i]) - int(line[i - 1]) != step:
                return ('False')
        return ('True')


def main():
    print(canyousliceit(input()))


if __name__ == '__main__':
    main()