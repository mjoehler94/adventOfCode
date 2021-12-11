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
    # start = coords[0]
    # end = coords[1]

    points = []
    if start[0] == end[0]:
        # it's a vertical line
        for y in range(start[1], end[1] + 1):
            points.append((start[0], y))
    else:
        # it's a horizontal line
        for x in range(start[0], end[0] + 1):
            points.append((x, start[1]))
    return points

print(get_points((0,1), (0,4)))

def count_overlap(all_points):
    counts = Counter(all_points)
    return len([x for x in counts.values if x > 1])


print('\nPart 1')

def part1(vals):
    """find the number of points with at least two lines"""
    string_coords = [x.split(" -> ") for x in vals]
    print('string_coords', string_coords[:3])

    # for 
    
    all_points = []
    for c in string_coords:
        print(c)
        start = [(int(x), int(y)) for x, y in c[0].split(',')]
        end = [(int(x), int(y)) for x, y in c[0][1].split(',')]
        

        print(c, get_points(start, end))
        # all_points += get_points(c)
    
    overlap = count_overlap(all_points)
    return overlap

print(part1(vals))


print("Done")

print("Part 2")
def part2():
    pass



print("Done")