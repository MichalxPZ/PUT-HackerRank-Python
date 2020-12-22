def lower(N):
    heights = list(map(int, input().split()))
    max_steps = 0
    for i in range(N-2):
        current_steps = 0
        k = i
        while heights[k+1] <= heights[k]:
            current_steps += 1
            k += 1
            if k > (N-2):
                break
        if current_steps > max_steps:
            max_steps = current_steps
    print(max_steps)

def main():
    lower(int(input()))


if __name__ == '__main__':
    main()
