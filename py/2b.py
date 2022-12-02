def game_score(game):
    them = ord(game[0]) - ord("A")
    goal = ord(game[1]) - ord("X") # 0 lose 1 draw 2 win
    if goal == 1:
        return them + 1 + 3
    if goal == 2:
        return (them + 1) % 3 + 1 + 6
    return (them - 1) % 3 + 1

with open("2.input") as f:
    lines = [line.strip().split() for line in f.readlines()]

print(sum(map(game_score, lines)))
