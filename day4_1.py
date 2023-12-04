from sys import stdin

total_point = 0

for line in stdin:
    line = line.rstrip()
    number_set = set()
    i, numbers = line.split(":")
    left, right = numbers.split("|")
    winning_numbers = left.split()
    current_numbers = right.split()
    for number in winning_numbers:
        number_set.add(number)
    
    point = 0
    for number in current_numbers:
        if number in number_set:
            point = point*2 if point else 1
    
    total_point += point
    
print(total_point)