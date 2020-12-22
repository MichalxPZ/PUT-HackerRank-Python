def greenbin(words):
    pairs = 0
    counter = {}
    for i in range(len(words)):
        temp_word = "".join(sorted(words[i]))
        if temp_word in counter:
            counter[temp_word] += 1
        else:
            counter[temp_word] = 1
    for i in counter.values():
        pairs += i * (i - 1) // 2

    return pairs


def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    print(greenbin(words))


if __name__ == "__main__":
    main()
