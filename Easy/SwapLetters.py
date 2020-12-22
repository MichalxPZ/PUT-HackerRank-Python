def swap(N, M):
    line = list(map(int, input().split()))
    for i in range(M):
        swap_values = list(map(int, input().split()))
        line[swap_values[0]],line[swap_values[1]] = line[swap_values[1]],line[swap_values[0]]
    for i in range(len(line)):
        print(line[i], end=' ')

if __name__ == '__main__':
    dane = input().split()
    swap(int(dane[0]), int(dane[1]))
