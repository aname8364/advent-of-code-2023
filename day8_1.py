from sys import stdin

stdin = open("input.txt")

data = stdin.readlines()

instruction = reversed(data[0].rstrip())

data = data[2:]
nodes = {}

for i in data:
    x = i.split("=")
    nodes[x[0].rstrip()] = x[1].rstrip().replace("(", "").replace(")", "").replace(",", "").split()

arr = []
for i in instruction:
    arr.append(i)

tmp = list(arr)

count = 0
current = "AAA"
while current != "ZZZ":
    count += 1
    if not arr:
        arr = list(tmp)
    v = arr.pop()
    if v == "L":
        current = nodes[current][0]
    elif v == "R":
        current = nodes[current][1]

print(current, count)