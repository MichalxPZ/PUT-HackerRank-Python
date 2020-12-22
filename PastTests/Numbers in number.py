def numbersInNumber(num):
    ret = ''
    for i in range(1, len(num)+1):
        occurences = {}
        for j in range(len(num)-i+1):
            number = 0
            for e in num[j:j+i]:
                number = number * 10 + e
            if int(number) not in occurences.keys():
                occurences[int(number)] = 1
            else:
                occurences[int(number)] += 1
        most = max(occurences.values())
        tab = []
        for occ in occurences.keys():
            if occurences[occ]==most:
                tab.append(occ)
        ret += (str(sorted(tab)[0]))
        ret += "\n"
    return ret

def main():
    nums = list(map(int, input()))
    print(numbersInNumber(nums))


if __name__ == '__main__':
    main()
