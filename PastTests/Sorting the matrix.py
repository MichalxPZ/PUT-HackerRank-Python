def matsort(mat, m):
    mat = sorted(mat)
    retmat = [[0 for col in range(m)] for row in range(len(mat)//m)]
    for i in range(m):
        for j in range(len(mat)//m):
            retmat[j][i] = mat[0]
            for k in range(len(mat)-1):
                mat[k] = mat[k+1]
    ret = ''
    for i in retmat:
        list_to_string = ''
        for j in i:
            list_to_string += str(j) + " "
        ret += list_to_string
        ret += "\n"

    return ret


def main():
    line = list(map(int, input().split()))
    mat = []
    for i in range(line[0]):
        for j in list(map(int, input().split())):
            mat.append(j)
    print(matsort(mat, line[1]))


if __name__ == '__main__':
    main()
