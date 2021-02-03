def Kadane(lista):
    temp_sum = max_sum = lista[0]

    for i in lista[1:]:
        temp_sum = max(i, temp_sum + i)
        max_sum = max(0, max_sum, temp_sum)
    return max_sum


def maxsuminmat(mat):
    maxRecsum = 0
    for i in range(len(mat[0])+1):
        for j in range(i, len(mat[0])+1):
            tab = []
            for k in range(len(mat)):
                tab.append(sum(mat[k][i:j]))
            temp_sum = Kadane(tab)
            if temp_sum > maxRecsum:
                maxRecsum = temp_sum
    return maxRecsum


def main():
    mat = [list(map(int, input().split())) for _ in range(int(input()))]
    print(maxsuminmat(mat))


if __name__ == '__main__':
    main()
