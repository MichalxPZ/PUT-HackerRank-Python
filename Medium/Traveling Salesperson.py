from math import sqrt

def travel(cities, order):
    distance = 0
    for i in range(0, len(order)-1):
        x1 = cities[order[i]][0]
        y1 = cities[order[i]][1]
        x2 = cities[order[i+1]][0]
        y2 = cities[order[i+1]][1]
        distance += sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))
    return distance


def main():
    n = int(input())
    cities = {}
    for _ in range(n):
        line = input().split()
        cities[line[0]] = (int(line[1]), int(line[2]))
    order = input().split()
    order.append(order[0])
    print(travel(cities, order))


if __name__ == '__main__':
    main()
