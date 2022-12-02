def game_score(game):
    them = game[0]
    you = game[1]
    A_offset = ord("A")
    X_offset = ord("X") - ord("A") + A_offset
    them = ord(them) - A_offset
    you = ord(you) - X_offset
    result = you + 1
    if them == you:
        return result + 3
    if you - them == 1 or you - them == -2:
        return result + 6
    return result

with open("2.input") as f:
    lines = [line.strip().split() for line in f.readlines()]

print(sum(map(game_score, lines)))
