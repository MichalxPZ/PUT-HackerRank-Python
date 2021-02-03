from math import pow

def convert(bits):
    asc = 0
    for i in range(len(bits)):
        asc += pow(2, len(bits)-i)*int(bits[i])
    return chr(int(asc))


def main():
    text = list(map(str, input().split()))
    for ch in text:
        print(convert(ch), end="")


if __name__ == '__main__':
    main()
