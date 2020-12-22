def jump(mat, cords):
    if mat[cords[0]][cords[1]] != min(mat[cords[0]]):
        for i in range(len(mat[cords[0]])):
            if mat[cords[0]][i] == min(mat[cords[0]]):
                cords[1] = i
                jump(mat, cords)
    else:
        tab = []
        for i in range(len(mat)):
            tab.append(mat[i][cords[1]])
        if mat[cords[0]][cords[1]] != min(tab):
            for i in range(len(mat)):
                if mat[i][cords[1]] == min(tab):
                    cords[0] = i
                    jump(mat, cords)
    return (str(cords[0]) + " " + str(cords[1]))


def main():
    mat = []
    n = int(input())
    line = list(map(int, input().split()))
    for i in range(n):
        mat.append(list(map(int, input().split())))
    print(jump(mat, line))


if __name__ == '__main__':
    main()
