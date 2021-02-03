def knight(mat):
    moves = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 's':
                if i >= 2 and j >= 1:
                    if mat[i-2][j-1] == 's':
                        moves += 1
                if i <= len(mat)-3 and i >= 1:
                    if mat[i+2][j-1] == 's':
                        moves += 1
                if i >= 1 and j >=2:
                    if mat[i-1][j-2] == 's':
                        moves += 1
                if i <= len(mat)-2 and j >=2:
                    if mat[i+1][j-2] == 's':
                        moves += 1
                if i <= len(mat)-3 and j <= len(mat[0])-2:
                    if mat[i+2][j+1] == 's':
                        moves += 1
                if i <= len(mat)-2 and j <= len(mat[0])-3:
                    if mat[i+1][j+2] == 's':
                        moves += 1
                if i >= 2 and j <= len(mat[0])-2:
                    if mat[i-2][j+1] == 's':
                        moves += 1
                if i >= 1 and j <= len(mat[0])-3:
                    if mat[i-1][j+2] == 's':
                        moves +=1
    return moves


def main():
    n = int(input())
    mat = []
    for _ in range(n):
        mat.append(list(input()))
    print(knight(mat))


if __name__ == '__main__':
    main()
