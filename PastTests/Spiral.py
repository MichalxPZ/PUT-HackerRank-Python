def spiral(mat,ret):
    if len(mat) == 1 and len(mat[0]) == 1:
        ret = ret, str(mat[0][0])
        return ret
    elif len(mat) == 2 and len(mat[0]) == 2:
        ret = ret, str(mat[0][0]), str(mat[0][1]), str(mat[1][1]), str(mat[1][0])
        return ret
    else:
        tab = mat[0]
        for i in range(1, len(mat)):
            tab.append(mat[i][-1])
        for j in range(len(mat[0])-1, 0, -1):
            tab.append(mat[-1][j])
        for k in range(len(mat)-1, 1, -1):
            tab.append(mat[k][0])
        for l in tab:
            ret = ret, str(l)
        mat2 = []
        for p in range(1, len(mat)-1):
            line = []
            for h in range(1, len(mat[p])-1):
                line.append(mat[p][h])
            mat2.append(line)
        return spiral(mat2, ret)


def main():
    h = int(input())
    mat = [list(map(int, input().split())) for _ in range(h)]
    print(spiral(mat, ''))


if __name__ == '__main__':
    main()
