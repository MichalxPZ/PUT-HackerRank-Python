def compare(mat1, mat2):
    for row in range(len(mat1)):
        temp_mat = mat1[:row] + mat1[row+1:]
        for col in range(len(mat1[row])):
            probmat2 = []
            for j in range(len(temp_mat)):
                probmat2.append(temp_mat[j][:col]+temp_mat[j][col+1:])
                if probmat2 == mat2:
                    return "True"
    return "False"


def main():
    n = int(input())
    mat1 = [list(input().split()) for _ in range(n)]
    mat2 = [list(input().split()) for _ in range(n-1)]
    print(compare(mat1, mat2))


if __name__ == '__main__':
    main()
