from sys import stdin

def read_data(arr: list, n: int) -> None:
    for i in next_data[n].strip().split("\n")[:-2]:
        arr.append(list(map(int, i.split())))
    
puzzle_input = stdin.read().rstrip()
_, *next_data = puzzle_input.split(":")
next_data[-1] += "\n\nm"

seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

read_data(seeds, 0)
read_data(seed_to_soil, 1)
read_data(soil_to_fertilizer, 2)
read_data(fertilizer_to_water, 3)
read_data(water_to_light, 4)
read_data(light_to_temperature, 5)
read_data(temperature_to_humidity, 6)
read_data(humidity_to_location, 7)

current_data = seeds[0]

def coa(data):
    for i in range(len(current_data)):
        q = current_data[i]
        for arr in data:
            x,y,z = arr
            if q >= y and q<= y+z-1:
                current_data[i] = x+q-y

coa(seed_to_soil)
coa(soil_to_fertilizer)
coa(fertilizer_to_water)
coa(water_to_light)
coa(light_to_temperature)
coa(temperature_to_humidity)
coa(humidity_to_location)

print(current_data)
print(min(current_data))