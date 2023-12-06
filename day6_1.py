from sys import stdin

stdin = open("input.txt")
data = stdin.read()

_, *data = data.split(":")
time, distance = data
time = list(map(int, time.split("\n")[0].split()))
distance = list(map(int, distance.split()))

game_round = len(time)

result = [0] * game_round

for i in range(game_round):
    round_time = time[i]
    round_distance = distance[i]
    for j in range(1, round_time+1):
        current_distance = (round_time-j)*j
        if current_distance > round_distance:
            result[i] += 1

x = 1
for i in result:
    x *= i
print(x)