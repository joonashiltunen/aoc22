def game_score(game):
    them = ord(game[0]) - ord("A")
    you = ord(game[1]) - ord("X")
    result = you + 1
    if them == you:
        return result + 3
    if (you - them) % 3 == 1:
        return result + 6
    return result

with open("2.input") as f:
    lines = [line.strip().split() for line in f.readlines()]

print(sum(map(game_score, lines)))
