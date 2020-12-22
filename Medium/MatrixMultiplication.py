def matrixmultiplication():

    wym = list(map(int, input().split()))
    mat1 = [[0 for x in range(wym[0])] for y in range(wym[1])]
    for i in range(wym[1]):
        mat1[i] = list(map(int, input().split()))
    wym2 = list(map(int, input().split()))

    mat2 = [[0 for x in range(wym2[0])] for y in range(wym2[1])]
    for i in range(wym2[1]):
        mat2[i] = list(map(int, input().split()))
    res = [[0 for x in range(len(mat2[0]))] for y in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                res[i][j] += mat1[i][k] * mat2[k][j]

    for i in res:
        print(str(i).strip().replace(',','').replace('[','').replace(']',''))

def main():
    matrixmultiplication()


if __name__ == '__main__':
    main()
