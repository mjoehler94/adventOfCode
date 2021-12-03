# increases

with open("data/day1.txt") as f:
    vals = [int(x) for x in f.readlines()]

incs = 0
for i in range(len(vals)):
    if i == 0:
        continue
    if vals[i] > vals[i-1]:
        incs += 1

print(incs)
print(sum(vals))


incs = 0
for i in range(len(vals)):
    if i <= 2:
        continue
    if sum(vals[i-2:i+1]) > sum(vals[i-3:i]):
        incs += 1

print(incs)

# answer p1 = 1167
# answer p2 = 1130
