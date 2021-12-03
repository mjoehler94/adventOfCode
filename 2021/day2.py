# submarine steering

# read input
with open("data/day2.txt") as f:
    vals = [(x.split(" ")[0], int(x.split(' ')[1])) for x in f.readlines()]

print(vals[:5])
print()

x = 0
depth = 0

for direction, distance in vals:
    if direction == "forward":
        x += distance
    elif direction == "up":
        depth -= distance
    elif direction == 'down':
        depth += distance

# What do you get if you multiply your final horizontal position by your final depth?
print("Part 1 Answer")
print(f"Product of horizontal position {x} and depth {depth} is {x * depth}")
print()


x = 0
depth = 0
aim = 0
for direction, distance in vals:
    if direction == "forward":
        x += distance
        depth += aim * distance
    elif direction == "up":
        aim -= distance
    elif direction == 'down':
        aim += distance
print("Part 2 Answer")
print(f"Product of horizontal position {x} and depth {depth} is {x * depth}")
