# day5.py ---------------------
from collections import Counter

with open("data/day5.txt") as f:
    vals = [x.strip() for x in f.readlines()]

print(vals[:5])
print(len(vals))
print()

temp = vals[:5]
temp = [x.split(' -> ') for x in temp]
print(temp)
test = [(int(x), int(y)) for x, y in [c.split(',') for c in temp[0]]]
print(test)

def get_points(start, end):

    points = []
    if start[0] == end[0]:
        # it's a vertical line
        for y in range(start[1], end[1] + 1):
            points.append((start[0], y))
    elif start[1] == end[1]:
        # it's a horizontal line
        for x in range(start[0], end[0] + 1):
            points.append((x, start[1]))

    return points

print(get_points((0,1), (0,4)))
print(get_points((1,4), (7,4)))

def count_overlap(all_points):
    counts = Counter(all_points)
    # print(counts)
    return len([x for x in counts.values() if x > 1])


print('\nPart 1')

def part1(vals):
    """find the number of points with at least two lines"""
    string_coords = [x.split(" -> ") for x in vals]
    # print('string_coords', string_coords[:3])
    
    all_points = []
    for s in string_coords:
        start = [int(x) for x in s[0].split(',')]
        end = [int(x) for x in s[1].split(',')]
        # print(start, end)
        
        # print(c, get_points(start, end))
        all_points += get_points(start, end)
    print()
    # print(*all_points, '\n')
    
    overlap = count_overlap(all_points)
    return overlap

print(part1(vals))

test_vals = [
'0,9 -> 5,9',
'9,4 -> 3,4',
'8,0 -> 0,8',
'2,2 -> 2,1',
'7,0 -> 7,4',
'6,4 -> 2,0',
'0,9 -> 2,9',
'3,4 -> 1,4',
'0,0 -> 8,8',
'5,5 -> 8,2',
]

print([x for x in test_vals])
print('----------')
print(part1(test_vals))





print("Done")

print("Part 2")
def part2():
    pass



print("Done")