def distance(mat):
    dist = 1000
    cords = []
    pairs = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 1:
                cords.append((i+1,j+1))
    for i in range(len(cords)-1):
        for j in range(i+1, len(cords)):
            if cords[j][1]%cords[i][1] == 0 and cords[j][0]%cords[i][0] == 0:
                pairs.append([cords[i], cords[j]])
    if len(pairs) == 0:
        return dist
    for i in pairs:
        dist = min(dist, abs(i[0][0]-i[0][1]) + abs(i[1][0] - i[1][1]))
    return dist


def main():
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    print(distance(mat))


if __name__ == '__main__':
    main()
