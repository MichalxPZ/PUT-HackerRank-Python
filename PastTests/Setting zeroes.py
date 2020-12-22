def set(mat):
    mat2 = []
    for i in range(len(mat)):
        tab = []
        for j in range(len(mat[i])):
            tab.append(mat[i][j])
        mat2.append(tab)

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                for k in range(len(mat[i])):
                    mat2[i][k] = 0
                for col_elem in range(len(mat2)):
                    mat2[col_elem][j] = 0
    ret = ''
    for i in mat2:
        for j in i:
            ret += str(j) + " "
        ret += "\n"

    return ret


def main():
    mat = [list(map(int, input().split())) for _ in range((list(map(int, input().split())))[0])]
    print(set(mat))


if __name__ == '__main__':
    main()
