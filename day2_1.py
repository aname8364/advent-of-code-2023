from sys import stdin

result = 0

for line in stdin:
    line = line.rstrip()
    game_number, game_sets = line.split(":")
    game_number = game_number.split()[1]
    game_sets = game_sets.split(";")
    print("-------")
    for game_set in game_sets:
        cubes = {
            "red": 12,
            "green": 13,
            "blue": 14
        }
        game_color = game_set.split(",")
        for color in game_color:
            color = color.lstrip()
            count, name = color.split()
            cubes[name] -= int(count)
            
        can_play = True
        for cube_color, cube_count in cubes.items():
            if cube_count < 0:
                can_play = False
                break
            
        if not can_play:
            break
    
    if can_play:
        result += int(game_number)
        
print(result)