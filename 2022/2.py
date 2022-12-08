from enum import Enum

input_path = "input/2.txt"

class Gesture(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

class Points(Enum):
    Lose = 0
    Draw = 3
    Win = 6

mapping_a = {
    "A": Gesture.Rock, "X": Gesture.Rock,
    "B": Gesture.Paper, "Y": Gesture.Paper,
    "C": Gesture.Scissors, "Z": Gesture.Scissors
}

mapping_b = {
    "A": Gesture.Rock, "X": Points.Lose,
    "B": Gesture.Paper, "Y": Points.Draw,
    "C": Gesture.Scissors, "Z": Points.Win
}

results_a = {
    Gesture.Rock: { Gesture.Rock: Points.Draw, Gesture.Paper: Points.Win, Gesture.Scissors: Points.Lose },
    Gesture.Paper: { Gesture.Rock: Points.Lose, Gesture.Paper: Points.Draw, Gesture.Scissors: Points.Win },
    Gesture.Scissors: { Gesture.Rock: Points.Win, Gesture.Paper: Points.Lose, Gesture.Scissors: Points.Draw }
}

results_b = {
    Gesture.Rock: { Points.Draw: Gesture.Rock, Points.Win: Gesture.Paper, Points.Lose: Gesture.Scissors },
    Gesture.Paper: { Points.Lose: Gesture.Rock, Points.Draw: Gesture.Paper, Points.Win: Gesture.Scissors },
    Gesture.Scissors: { Points.Win: Gesture.Rock, Points.Lose: Gesture.Paper, Points.Draw: Gesture.Scissors }
}

def calculate_result_a(enemy_gesture, my_gesture):
    return results_a[enemy_gesture][my_gesture].value + my_gesture.value

def calculate_result_b(enemy_gesture, points_needed):
    return results_b[enemy_gesture][points_needed].value + points_needed.value

def a():
    points = 0
    with open(input_path) as file:
        for line in file:
            enemy_gesture, my_gesture = line.strip().split(" ")
            points += calculate_result_a(mapping_a[enemy_gesture], mapping_a[my_gesture])
    return points

def b():
    points = 0
    with open(input_path) as file:
        for line in file:
            enemy_gesture, points_needed = line.strip().split(" ")
            points += calculate_result_b(mapping_b[enemy_gesture], mapping_b[points_needed])
    return points


def main():
    points = b()
    print("Points: " + str(points))

if __name__ == "__main__":
    main()
