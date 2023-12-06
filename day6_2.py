from sys import stdin

stdin = open("input.txt")

data = stdin.read()

_, *data = data.split(":")
time, distance = data
time = int(time.split("\n")[0].replace(" ", ""))
distance = int(distance.replace(" ", ""))

count = 0
for i in range(1, time+1):
    dist = (time-i)*i
    if dist > distance:
        count += 1
        
print(count)