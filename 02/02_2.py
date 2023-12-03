result = 0

with open("input.txt", "r") as f:
    game_id = 0
    for line in f.readlines():
        game_data = line.split(":")[1]
        grabs = game_data.split(";")
        possible = True
        minimal_cubes = {
            "red": 0,
            "blue": 0,
            "green": 0,
        }
        for grab in grabs:
            # print(grab)
            iteration = 0
            for entry in grab.split(" ")[1:]:
                entry = entry.removesuffix("\n").removesuffix(",")
                if iteration % 2 == 0:
                    number = int(entry)
                else:
                    if minimal_cubes[entry] < number:
                        minimal_cubes[entry] = number
                iteration = iteration + 1

        power_of_minimal_cubes = minimal_cubes["blue"] * minimal_cubes["red"] * minimal_cubes["green"]
        result = result + power_of_minimal_cubes


print(result)
