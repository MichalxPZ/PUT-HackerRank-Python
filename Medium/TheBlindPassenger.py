from math import ceil

def passenger(s):
    results = {
        0: 'A L',
        1: 'W L',
        2: 'W L',
        3: 'A L',
        4: 'A R',
        5: 'M R',
        6: 'W R',
        7: 'W R',
        8: 'M R',
        9: 'A R'
    }
    if s == 1:
        return('poor conductor')
    else:
        row = ceil((s-1)/5)
        return(str(row) + ' ' + str(results[s%10]))


def main():
    for i in range(int(input())):
        print(passenger(int(input())))


if __name__ == '__main__':
    main()
