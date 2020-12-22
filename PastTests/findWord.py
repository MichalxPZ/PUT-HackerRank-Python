def find_word(mat, pattern):
    for i in mat:
        if pattern in i or rev_str(pattern) in i:
            return "YES"
    for i in range(len(mat[0])):
        vert = ''
        for j in range(len(mat)):
            vert = vert + (mat[j][i])
        if pattern in vert or rev_str(pattern) in vert:
            return "YES"
    return "NO"


def rev_str(str):
    return str[::-1]


def main():
    line = list(map(int, input().split()))
    pattern = input()
    mat = [0] * line[0]
    for i in range(line[0]):
        mat[i] = input()
    print(find_word(mat, pattern))


if __name__ == '__main__':
    main()
