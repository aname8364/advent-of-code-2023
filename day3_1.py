from sys import stdin

engine = []
for line in stdin:
    engine.append(line.rstrip())

width = 0
height = 0
numbers = []
number = ""
pos = []
for y, row in enumerate(engine):
    height = y
    for x, v in enumerate(row):
        width = x
        if v >= '0' and v <= '9':
            number += v
            pos.append([x,y])
        else:
            if number:
                numbers.append([int(number), pos])
                number = ""
                pos = []
            
total = 0
for data in numbers:
    value, pos_data = data
    is_good = False
    
    filter_char = "1234567890."
    def lets_go(x, y):
        global is_good
        if x >= 0 and x < width and y >= 0 and y < height:
            if all(engine[y][x] not in i for i in filter_char):
                is_good = True
            
    for i, pos in enumerate(pos_data):
        x, y = pos
        lets_go(x-1, y-1)
        lets_go(x, y-1)
        lets_go(x+1, y-1)
        
        lets_go(x-1, y)
        lets_go(x+1, y)
        
        lets_go(x-1, y+1)
        lets_go(x, y+1)
        lets_go(x+1, y+1)
        
    if is_good:
        total += value
        
print(total)