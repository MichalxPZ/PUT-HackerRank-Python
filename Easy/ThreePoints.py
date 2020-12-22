def colinear(A, B, C):
    triangle = 0.5 * (A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))
    if triangle == 0:
        print("True")
    else:
        print("False")


def main():
    A = input()
    A = A.split()
    A[0] = int(A[0])
    A[1] = int(A[1])
    B = input()
    B = B.split()
    B[0] = int(B[0])
    B[1] = int(B[1])
    C = input()
    C = C.split()
    C[0] = int(C[0])
    C[1] = int(C[1])
    colinear(A, B, C)


if __name__ == '__main__':
    main()
