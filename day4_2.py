from sys import stdin

cards = []
total = 0

for line in stdin:
    line = line.rstrip()
    number_set = set()
    name, numbers = line.split(":")
    card, i = name.split()
    winning, current = numbers.split("|")
    winning_numbers = winning.split()
    current_numbers = current.split()
    for number in winning_numbers:
        number_set.add(number)
        
    cards.append({
        "index": int(i),
        "winning": number_set,
        "current": current_numbers
    })

instance_list = [1 for i in range(1, len(cards)+1)]
total += len(instance_list)
print(instance_list)

for index, count in enumerate(instance_list):
    instance = cards[index]
    if instance:
        number_count = 0
        for num in instance["current"]:
            if num in instance["winning"]:
                number_count += 1
        #print(number_count , "=========")
        total += number_count * count
        for i in range(1, number_count+1):
            next_index = instance["index"] + i
            instance_list[next_index-1] += count
        instance_list[index] = 0
        #print(instance_list)
            
print(total)
