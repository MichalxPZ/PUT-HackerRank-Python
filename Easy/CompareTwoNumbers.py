t = int(input())
for i in range(t):
    line = input()
    line = line.split()
    if int(line[0]) > int(line[1]):
        print(line[0],' is greater than ',line[1])
    elif int(line[0]) == int(line[1]):
        print('n is equal m: ',line[0])
    elif int(line[0]) < int(line[1]):
        print(line[0],' is smaller than ',line[1])