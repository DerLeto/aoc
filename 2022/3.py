from enum import Enum

input_path = "input/3.txt"

def a():
    points = 0
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()
            compartment1 = line_stripped[0:int(len(line_stripped)/2)]
            compartment2 = line_stripped[int(len(line_stripped)/2):]
            chars_comp1 = [character for character in compartment1]
            for character in compartment2:
                if character in chars_comp1:
                    if character.islower():
                        points += ord(character) - ord('a') + 1
                    else:
                        points += ord(character) - ord('A') + 27
                    break

    return points

def b():
    points = 0
    with open(input_path) as file:
        counter = 0
        lines = file.readlines()
        while counter < len(lines):
            chars1 = [character for character in lines[counter + 1].strip()]
            chars2 = [character for character in lines[counter + 2].strip()]
            for character in lines[counter].strip():
                if character in chars1 and character in chars2:
                    if character.islower():
                        points += ord(character) - ord('a') + 1
                    else:
                        points += ord(character) - ord('A') + 27
                    break
            counter += 3
    return points


def main():
    points = b()
    print("Points: " + str(points))

if __name__ == "__main__":
    main()
