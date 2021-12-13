# day6.py ---------------
with open("data/day6.txt") as f:
     vals = [int(x) for x in f.read().split(',')]

# print(vals[:5])
print(len(vals))
test_vals = [3,4,3,1,2]


# part 1
def update_population(population):
    new_borns = []
    new_population = []
    for fish in population:
        if fish:
            new_population.append(fish-1)
        else:
            new_population.append(6)
            new_borns.append(8)
    
    return new_population + new_borns

def part1(pop, days):
    population = pop.copy()
    for i in range(days):
        temp_population = update_population(population)
        population = temp_population.copy()
    print(len(population))
    return len(population)

part1(vals, 80)
print (len(vals))
print("Done")

print("Part 2")

def part2 (pop, days):
    # brute force won't work :)
    pass
part2(vals, 1) 


