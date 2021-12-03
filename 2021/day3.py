# read input
with open("data/day3.txt") as f:
    vals = [(x.split(" ")[0], int(x.split(' ')[1])) for x in f.readlines()]

print(vals[:5])
print()

x = 0

for v in vals:
    print(v)

# What do you get if you multiply your final horizontal position by your final depth?
print("Part 1 Answer")
print(f"")
print()


print("Part 2 Answer")
print(f"Product of horizontal position {x} and depth {depth} is {x * depth}")
