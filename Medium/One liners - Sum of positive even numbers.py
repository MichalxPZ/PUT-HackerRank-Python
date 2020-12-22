s = input()
print(sum([x for x in list(map(int, s.split())) if x%2 == 0 and x > 0]))