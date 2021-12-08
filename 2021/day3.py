# day3 ----------
def binaryToDecimal(binary):
     
    binary = int(binary)
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

# read input
with open("data/day3.txt") as f:
    vals = [x.strip() for x in f.readlines()]

print(vals[:5])
print()

bit_count = dict()
for v in vals:
    for i in range(len(v)):
        if not bit_count.get(i, False):
            bit_count[i] = int(v[i])
        else:
            bit_count[i] += int(v[i])



gamma = ""
epsilon = ""
for k, v in bit_count.items():
    if v >= len(vals) / 2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

gamma_as_decimal = binaryToDecimal(gamma)
epsilon_as_decimal = binaryToDecimal(epsilon)


# What do you get if you multiply your final horizontal position by your final depth?
print("Part 1 Answer")
print(gamma, gamma_as_decimal)
print(epsilon, epsilon_as_decimal)
print(gamma_as_decimal * epsilon_as_decimal)
print()


print("Part 2 Answer")
oxygen = 0
co2 = 0



def get_most_common_bit(vals, position):
    count = 0
    for v in vals:
        count += int(v[position])
    return int(count >= len(vals)/2)

def filter_numbers(vals, position, value):
    return [v for v in vals if v[position] == value]

# print([get_most_common_bit(vals, x) for x in range(len(vals[0]))])



def get_rating(vals, most_common=True):
    temp_vals = vals.copy()
    position = 0
    count = 0
        
    while(len(temp_vals) > 1):
        for v in temp_vals:
            count += int(v[position])
        if check == '1':
            pass


    return binaryToDecimal(*temp_vals)


