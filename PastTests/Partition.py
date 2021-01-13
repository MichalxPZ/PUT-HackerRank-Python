def partition(numbers):
    max_sum = []
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            for k in range(len(numbers)):
                for l in range(k, len(numbers)):
                    if sum([x for x in numbers[k:l+1:3]]) == sum([x for x in numbers[i:j+1:2]]):
                        max_sum.append(sum([x for x in numbers[i:j+1:2]]))
    return max(max_sum)

def main():
    n = input()
    line = list(map(int, input().split()))
    print(partition(line))


if __name__ == '__main__':
    main()
