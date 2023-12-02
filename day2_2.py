from sys import stdin

result = 0

for line in stdin:
    cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    line = line.rstrip()
    game_number, game_sets = line.split(":")
    game_number = game_number.split()[1]
    game_sets = game_sets.split(";")
    for game_set in game_sets:
        game_color = game_set.split(",")
        for color in game_color:
            color = color.lstrip()
            count, name = color.split()
            count = int(count)
            if count > cubes[name]:
                cubes[name] = count
        
    mul = 1
    for cube_name, cube_count in cubes.items():
        mul *= cube_count
            
    result += mul
        
print(result)