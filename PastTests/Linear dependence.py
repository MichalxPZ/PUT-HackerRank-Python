def linear(mat):
    pairs = 0
    #rows
    for i in range(len(mat)-1):
        for j in range(i+1, len(mat)):
            lin = True
            for div in range(len(mat[0])):
                if mat[j][div] != 0 and mat[i][div] != 0:
                    k = mat[i][div]/mat[j][div]
                    break
            for p in range(1, len(mat[i])):
                if mat[j][p] != 0:
                    if mat[i][p]/mat[j][p] != k:
                        lin = False
                else:
                    if mat[i][p] != 0:
                        lin = False
            if lin:
                pairs += 1

    return pairs


def main():
    mat = []
    n = int(input())
    for i in range(n):
        mat.append(list(map(int, input().split())))
    for j in range(len(mat)):
        tab = []
        for k in range(len(mat[j])):
            tab.append(mat[k][j])
        mat.append(tab)
    result = linear(mat)
    print(result)


if __name__ == '__main__':
    main()
