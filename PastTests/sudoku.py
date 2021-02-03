def sudoku(mat):
    onetonine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(mat)):
        if sorted(mat[i]) != onetonine:
            return "False"
    for j in range(len(mat[0])):
        vert = []
        for i in range(len(mat)):
            vert.append(mat[i][j])
        if sorted(vert) != onetonine:
            return "False"
    diag1 = []
    diag2 = []
    for i in range(len(mat)):
        diag1.append(mat[i][i])
        diag2.append(mat[len(mat)-1-i][i])
    if sorted(diag2) != onetonine or sorted(diag1) != onetonine:
        return "True"
    return "X"

def main():
    mat = [list(map(int, input().split())) for _ in range(9)]
    print(sudoku(mat))


if __name__ == '__main__':
    main()
