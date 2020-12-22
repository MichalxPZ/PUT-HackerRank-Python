s = input()
print(sum([x*x for x in range(int((s.split())[0]),int((s.split())[1])+1)]))