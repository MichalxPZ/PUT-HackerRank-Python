def vertsort(mat):
    for i in range(len(mat[0])):
        vect = []
        for j in range(len(mat)):
            vect.append(mat[j][i])

        vect = sorted(vect)
        for j in range(len(mat)):
            mat[j][i] = vect[j]
    ret = ''
    for i in mat:
        for j in i:
            ret += str(j) + " "
        ret += "\n"
    return ret


def main():
    line = list(map(int, input().split()))
    mat = []
    for i in range(line[1]):
        mat.append(list(map(int, input().split())))
    print(vertsort(mat))


if __name__ == '__main__':
    main()
