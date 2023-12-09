input_path = "input/7.txt"

# 1000000 * len(card) * len(card)
# Five of a kind: 25000000
# Four of a kind: 16000000 + 1000000 = 17000000
# Full house: 9000000 + 4000000 = 13000000
# Three of a kind: 9000000 + 1000000 + 1000000 = 11000000
# Two pair: 4000000 + 4000000 + 1000000 = 9000000
# One pair: 4000000 + 1000000 + 1000000 + 1000000 = 7000000
# High card: 5 * 1000000 = 5000000

# + points for position:
# [0 .. 12] * pos
# first: [0 .. 12] * 28.561 = 188 .. 342.732
# second: [0 .. 12] * 2.197 = 88 .. 26.364
# third: [0 .. 12] * 169 = 38 .. 2.028
# fourth: [0 .. 12] * 13 = 13 .. 156
# fifth: [0 .. 12]

# + 0 .. 12 for first card
position_points_offset = {
    0: 28561,
    1: 2197,
    2: 169,
    3: 13,
    4: 1
}

points_card_a = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "J": 9,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0,
}

points_card_b = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
    "J": 0,
}


def get_hand_points_a(hand):
    cards = {}

    points = 0
    for i, card in enumerate(hand[0]):
        points += position_points_offset.get(i) * points_card_a.get(card)
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1

    for card, number in cards.items():
        points += number * number * 1000000

    return points


def a():
    res = 0
    hands = []
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()
            hand, bid = line_stripped.split()
            hands.append((hand, int(bid)))

    hands.sort(key=get_hand_points_a)

    for i, hand in enumerate(hands):
        res += (i + 1) * hand[1]

    return res


def get_hand_points_b(hand):
    cards = {}

    points = 0
    joker = 0
    for i, card in enumerate(hand[0]):
        points += position_points_offset.get(i) * points_card_b.get(card)

        if card == "J":
            joker += 1
            continue

        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1

    if len(cards) > 0:
        cards = dict(sorted(cards.items(), key=lambda item: item[1]))
        key = list(cards)[-1]
        cards[key] += joker
    else:
        cards["J"] = joker

    for card, number in cards.items():
        points += number * number * 1000000

    return points


def b():
    res = 0
    hands = []
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()
            hand, bid = line_stripped.split()
            hands.append((hand, int(bid)))

    hands.sort(key=get_hand_points_b)

    for i, hand in enumerate(hands):
        res += (i + 1) * hand[1]

    return res


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
