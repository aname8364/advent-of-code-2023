from sys import stdin

engine = []
for line in stdin:
    engine.append(line.rstrip())

width = 0
height = 0
stars = []

for y, row in enumerate(engine):
    height = y
    for x, v in enumerate(row):
        width = x
        if v == "*":
            stars.append([x,y])
        
already = []
filter_char = "1234567890"
def lets_go(x, y):
    global first, second, total
    if x >= 0 and x <= width and y >= 0 and y <= height:
        if any(engine[y][x] in i for i in filter_char):
            full_number = ""
            while x > 0 and any(engine[y][x-1] in j for j in filter_char):
                x -= 1
            full_number += engine[y][x]
            engine[y] = engine[y][:x] + "." + engine[y][x+1:]
            while x < width and any(engine[y][x+1] in j for j in filter_char):
                x += 1
                full_number += engine[y][x]
                engine[y] = engine[y][:x] + "." + engine[y][x+1:]
            
            result[k] += 1
            if first == 0:
                first = int(full_number)
            else:
                second = int(full_number)
            
            if result[k] == 2:
                total += first*second
                
total = 0
first, second = 0, 0
result = []
for k, star_pos in enumerate(stars):
    first, second = 0, 0
    result.append(0)
    x, y = star_pos
    lets_go(x-1, y-1)
    lets_go(x, y-1)
    lets_go(x+1, y-1)
        
    lets_go(x-1, y)
    lets_go(x+1, y)
        
    lets_go(x-1, y+1)
    lets_go(x, y+1)
    lets_go(x+1, y+1)
    
print(total)