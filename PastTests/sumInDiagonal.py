def diag_sum(mat):
    max_sum = 0
    rows = len(mat)
    columns = len(mat[0])
    for i in range(columns):
        start_col = i
        start_row = 0
        temp_sum = 0
        while start_col < columns and start_row < rows:
            temp_sum += mat[start_row][start_col]
            start_col += 1
            start_row += 1
        if temp_sum > max_sum:
            max_sum = temp_sum
        temp_sum = 0
        start_row = 0
        start_col = i
        while start_col > 0 and start_row < rows:
            temp_sum += mat[start_row][start_col]
            start_col -= 1
            start_row += 1
        if temp_sum > max_sum:
            max_sum = temp_sum

    return max_sum


def main():
    line = list(map(int, input().split()))
    mat = []
    for i in range(line[0]):
        mat.append(list(map(int, input().split())))
    print(diag_sum(mat))


if __name__ == '__main__':
    main()
