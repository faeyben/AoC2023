max_red = 12
max_green = 13
max_blue = 14
result = 0

with open("input.txt", "r") as f:
    game_id = 0
    for line in f.readlines():
        game_id = game_id + 1
        game_data = line.split(":")[1]
        grabs = game_data.split(";")
        possible = True
        for grab in grabs:
            # print(grab)
            iteration = 0
            for entry in grab.split(" ")[1:]:
                entry = entry.removesuffix("\n").removesuffix(",")
                if iteration % 2 == 0:
                    number = int(entry)
                else:
                    # print(entry + ": " + str(number))
                    if entry == "red" and number > max_red:
                        possible = False
                    if entry == "green" and number > max_green:
                        possible = False
                    if entry == "blue" and number > max_blue:
                        possible = False
                iteration = iteration + 1

        line = line.removesuffix("\n")
        if possible:
            line = line.removesuffix("\n")
            print(f'{line} is possible. Adding {game_id} to the result.')
            result = result + game_id
        else:
            print(f'{line} is NOT possible')

print(result)
