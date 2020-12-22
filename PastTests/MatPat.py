def matpat(board):
    king = []
    rooks = []
    rows = [0, 1, 2, 3, 4, 5, 6, 7]
    cols = [0, 1, 2, 3, 4, 5, 6, 7]
    for i in rows:
        for j in cols:
            if board[i][j] == "k":
                king = [i, j]
            if board[i][j] == "w":
                rooks.append([i, j])
    for i in rooks:
        if [i[0], i[1]] == [king[0] - 1, king[1] - 1]:
            i[0] = 10
            i[1] = 10
        elif [i[0], i[1]] == [king[0] -1, king[1]]:
            i[0] = 10
            i[1] = 10
        elif [i[0], i[1]] == [king[0] - 1, king[1] + 1]:
            i[0] = 10
            i[1] = 10
        elif [i[0], i[1]] == [king[0], king[1] + 1]:
            i[0] = 10
            i[1] = 10
        elif [i[0], i[1]] == [king[0] + 1, king[1] + 1]:
            i[0] = 10
            i[1] = 10
        elif [i[0], i[1]] == [king[0] + 1, king[1]]:
            i[0] = 10
            i[1] = 10
        elif [i[0], i[1]] == [king[0] + 1, king[1] - 1]:
            i[0] = 10
            i[1] = 10
        elif [i[0], i[1]] == [king[0], king[1] - 1]:
            i[0] = 10
            i[1] = 10
    for i in rooks:
        if i[0] in rows:
            rows[i[0]] = 9
        if i[1] in cols:
            cols[i[1]] = 9
    rows = sorted(rows)
    for i in range(len(rows)):
        if rows[i] == 9:
            rows = rows[:i]
            break
    cols = sorted(cols)
    for i in range(len(cols)):
        if cols[i] == 9:
            cols = cols[:i]
            break
    attack = False
    if king[0] not in rows or king[1] not in cols:
        attack = True
    if king[0] - 1 in rows and king[1] - 1 in cols:
        return "game goes on"
    elif king[0] - 1 in rows and king[1] in cols:
        return "game goes on"
    elif king[0] - 1 in rows and king[1] + 1 in cols:
        return "game goes on"
    elif king[0] in rows and king[1] + 1 in cols:
        return "game goes on"
    elif king[0] + 1 in rows and king[1] + 1 in cols:
        return "game goes on"
    elif king[0] + 1 in rows and king[1] in cols:
        return "game goes on"
    elif king[0] + 1 in rows and king[1] - 1 in cols:
        return "game goes on"
    elif king[0] in rows and king[1] - 1 in cols:
        return "game goes on"

    if attack:
        return "mat"
    else:
        return "pat"

def main():
    board = [[char for char in input()] for _ in range(8)]
    print(matpat(board))


if __name__ == '__main__':
    main()
