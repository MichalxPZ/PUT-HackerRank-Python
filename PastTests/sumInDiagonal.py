def diag_sum(mat):
    max_sum = 0
    for i in range(len(mat[0])):
        start_col = i
        start_row = 0
        forward_diag = [[] for _ in range((2*len(mat) + 2*len(mat[0]) -2)//2)]
        backward_diag = [[] for _ in range((2*len(mat) + 2*len(mat[0]) -2)//2)]
        for j in range(len(mat[0])):
            for k in range(len(mat)):
                forward_diag[j + k].append(mat[k][j])
                backward_diag[j - k + len(mat)-1].append(mat[k][j])
    for i in forward_diag:
        summ = 0
        for j in i:
            summ += j
        max_sum = max(summ, max_sum)
    for i in backward_diag:
        summ = 0
        for j in i:
            summ += j
        max_sum = max(summ, max_sum)

    return max_sum


def main():
    line = list(map(int, input().split()))
    mat = []
    for i in range(line[0]):
        mat.append(list(map(int, input().split())))
    print(diag_sum(mat))


if __name__ == '__main__':
    main()
