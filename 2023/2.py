input_path = "input/2.txt"

class Game:
    max_cubes = {
        "red": 12,
        "blue": 14,
        "green": 13
    }

    def __init__(self, game_id, games):
        self.game_id = game_id
        self.games = games

    @staticmethod
    def create(line):
        game_id, games = line.split(":")
        game_id = int(game_id.strip().split()[1])

        games = games.strip().split(";")

        games_list = []
        for game in games:
            games_dict = {
                "red": 0,
                "blue": 0,
                "green": 0
            }

            parts = game.strip().split(",")
            for part in parts:
                number, color = part.strip().split()
                games_dict[color] = int(number)
            games_list.append(games_dict)

        return Game(game_id, games_list)

    def valid(self) -> bool:
        for game in self.games:
            for color in Game.max_cubes.keys():
                if game.get(color) > Game.max_cubes.get(color):
                    return False

        return True

    def necessary_cubes(self) -> dict:
        cubes = {
            "red": 0,
            "blue": 0,
            "green": 0
        }

        for game in self.games:
            for color in game.keys():
                if game.get(color) > cubes.get(color):
                    cubes[color] = game.get(color)

        return cubes




def a():
    res = 0
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()
            game = Game.create(line_stripped)
            if game.valid():
                res += game.game_id

    return res


def b():
    res = 0
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()
            game = Game.create(line_stripped)

            cubes = game.necessary_cubes()

            power = 1
            for number in cubes.values():
                power *= number

            res += power

    return res


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
