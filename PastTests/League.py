def league(teams, results, t):
    to_play = len(teams) - 1
    played = {}
    wins = {}
    for i in teams:
        played[i] = 0
        wins[i] = 0
    for res in results.keys():
        played[res[0]] += 1
        played[res[1]] += 1
        if int(results[res][0]) > int(results[res][1]):
            wins[res[0]] += 1
        elif int(results[res][1]) > int(results[res][0]):
            wins[res[1]] += 1
    teams_to_win = []
    for team in sorted(teams):
        if to_play - played[team] + wins[team] >= t:
            teams_to_win.append(team)
    ret = ''
    for i in teams_to_win:
        ret = ret + i + "\n"
    return ret



def main():
    n, m, t = list(map(int, input().split()))
    teams = []
    results = {}
    for _ in range(n):
        teams.append(input())
    for _ in range(m):
        line = list(input().split(":"))
        results[line[0], line[1]] = (int(line[2]), int(line[3]))
    print(league(teams, results, t))


if __name__ == '__main__':
    main()
