def play(results):
    players_wins = {}
    players_points = {}
    for i in results:
        i = i.split()
        player_one = i[0].split(':')
        player_two = i[1].split(":")
        if player_one[0] not in players_wins.keys():
            players_wins[player_one[0]] = 0
            players_points[player_one[0]] = 0
        if player_two[0] not in players_wins.keys():
            players_wins[player_two[0]] = 0
            players_points[player_two[0]] = 0
        players_points[player_one[0]] += int(player_one[1])
        players_points[player_two[0]] += int(player_two[1])
        if int(player_one[1]) > int(player_two[1]):
            players_wins[player_one[0]] += 1
        elif int(player_two[1]) > int(player_one[1]):
            players_wins[player_two[0]] += 1

    result_dict = {}
    for i in set(players_wins.values()):
        if i not in result_dict.keys():
            result_dict[int(i)] = []
        for k in players_wins.keys():
            if players_wins[k] == i:
                result_dict[int(i)].append(k)
    result_tab = []
    while result_dict != {}:
        maks = max(result_dict.keys())
        result_tab.append(result_dict[maks])
        del result_dict[maks]

    for draw in result_tab:
        if len(draw) > 1:
            for j in range(len(draw)):
                for k in range(j, len(draw)):
                    if players_points[draw[j]] < players_points[draw[k]]:
                        draw[j],draw[k] = draw[k], draw[j]
                    elif players_points[draw[j]] == players_points[draw[k]]:
                        if draw[j] > draw[k]:
                            draw[j], draw[k] = draw[k], draw[j]

    result = ""
    for i in result_tab:
        for j in i:
            result += str(j) + "\n"
    return result


def main():
    N = int(input())
    results = []
    for i in range(N):
        results.append(input())
    print(play(results))


if __name__ == '__main__':
    main()
