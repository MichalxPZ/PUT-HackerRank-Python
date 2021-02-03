import copy

def whopass(mat):
    mat2 = []
    for i in range(len(mat)):
        tab = []
        for j in range(len(mat[i])):
            tab.append(mat[i][j])
        mat2.append(tab)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] >= 3:
                mat2[i][j] = 1
            else:
                avg = 0
                n = 0
                if i == 0 and j == 0:
                    avg = mat[i+1][j] + mat[i][j+1] + mat[i+1][j+1]
                    avg = avg/3
                elif i == len(mat)-1 and j == len(mat)-1:
                    avg = mat[i-1][j] + mat[i-1][j-1] + mat[i][j-1]
                    avg = avg/3
                elif i == len(mat)-1 and j == 0:
                    avg = mat[i-1][j] + mat[i-1][j+1] + mat[i][j+1]
                    avg = avg/3
                elif i == 0 and j == len(mat)-1:
                    avg = mat[i+1][j] + mat[i+1][j-1] + mat[i][j-1]
                    avg = avg/3
                elif i == 0 and j != len(mat)-1:
                    avg = mat[i][j-1] + mat[i+1][j-1] + mat[i+1][j] + mat[i+1][j+1] + mat[i][j+1]
                    avg = avg/5
                elif j == 0 and i != len(mat)-1:
                    avg = mat[i+1][j] + mat[i+1][j+1] + mat[i][j+1] + mat[i-1][j+1] + mat[i-1][j]
                    avg = avg/5
                elif i == len(mat)-1 and j != len(mat)-1:
                    avg = mat[i][j-1] + mat[i-1][j-1] + mat[i-1][j] + mat[i-1][j+1] + mat[i][j+1]
                    avg = avg/5
                elif j == len(mat)-1 and i != len(mat)-1:
                    avg = mat[i-1][j] + mat[i-1][j-1] + mat[i][j-1] + mat[i+1][j-1] + mat[i+1][j]
                    avg = avg/5
                else:
                    avg = mat[i-1][j-1] + mat[i][j-1] + mat[i+1][j-1] + mat[i+1][j] + mat[i+1][j+1] + mat[i][j+1] + mat[i-1][j+1] + mat[i-1][j]
                    avg = avg/8
                if avg >= 3:
                    mat2[i][j] = 1
                else:
                    mat2[i][j] = 0

    ret = ''
    for i in mat2:
        for j in i:
            ret += str(j) + " "
        ret += "\n"
    return ret


def main():
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    print(whopass(mat))


if __name__ == '__main__':
    main()
