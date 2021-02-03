def pictures(mat, x, y):
    for i in range(len(mat)-y):
        for j in range(len(mat[i])-x):
            if mat[i][j] = 0:
                cords = (i, j)
                cnt = x
                while cnt > 0:
                    if 

def main():
    h, w, x, y = list(map(int, input().split()))
    mat = [list(map(int, input().split())) for _ in range(h)]
    print(pictures(mat, x, y))


if __name__ == '__main__':
    main()
