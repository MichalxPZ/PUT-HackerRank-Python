def triangle(h, n):
    for i in range(h):
        line = '* ' * (i + 1)
        print(line)
    if n > 1:
        triangle(h + 1, n - 1)


triangle(int(input()), int(input()))