def transform(mat, operations):
    for operation in operations:
        if operation.split()[0] == "RR":
            mat[int(operation.split()[1])].reverse()
        elif operation.split()[0] == "RC":
            tab = []
            col = int(operation.split()[1])
            for j in range(len(mat)):
                tab.append(mat[j][col])
            tab.reverse()
            for j in range(len(mat)):
                mat[j][col] = tab[j]
        elif operation == "T":
            mat2 = []
            for col in range(len(mat[0])):
                tab = []
                for row in range(len(mat)):
                    tab.append(mat[row][col])
                mat2.append(tab)
            mat = mat2
    ret = ''
    for i in mat:
        for j in i:
            ret += str(j) + " "
        ret += "\n"

    return ret


def main():
    line = list(map(int, input().split()))
    mat = []
    operations = []
    for i in range(line[0]):
        mat.append(list(map(int, input().split())))
    k = int(input())
    for i in range(k):
        operations.append(input())
    print(transform(mat, operations))


if __name__ == '__main__':
    main()
