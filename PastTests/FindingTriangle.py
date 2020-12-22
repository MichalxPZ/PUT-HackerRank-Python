def area(A, B, C):

    ar = abs((A[0] * (B[1]- C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))/2)
    return ar

def find_triangle(cords):
    max_area = 0
    min_area = area(cords[0], cords[1], cords[2])
    for i in range(len(cords)):
        for j in range(i+1, len(cords)):
            for k in range(j+1, len(cords)):
                ar = area(cords[i], cords[j], cords[k])
                if ar < min_area and ar != 0:
                    min_area = ar
                if ar > max_area:
                    max_area = ar
    ret_str = str(min_area) + " " + str(max_area)
    return ret_str


def main():
    n = int(input())
    cords = []
    for x in range(n):
        cords.append(tuple(map(int, input().split())))
    print(find_triangle(cords))


if __name__ == '__main__':
    main()
