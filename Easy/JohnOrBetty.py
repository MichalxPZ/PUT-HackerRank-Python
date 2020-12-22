line = input().split()
if int(line[0])>int(line[1]):
    print('John')
elif int(line[0])<int(line[1]):
    print('Betty')
elif int(line[0])==int(line[1]):
    print('NOBODY')