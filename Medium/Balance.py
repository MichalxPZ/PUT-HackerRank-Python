def balance(weights):
    diff = 100000
    sums1 = [weights[0]]
    for i in range(1, len(weights)):
        sums1.append(sums1[i-1] + weights[i])
    for i in range(0, len(weights)):
        if diff > abs(sums1[i] - (sums1[-1] - sums1[i])):
            diff = abs(sums1[i] - (sums1[-1] - sums1[i]))
    return diff


def main():
    n = input()
    line = list(map(int, input().split()))
    print(balance(line))


if __name__ == '__main__':
    main()
