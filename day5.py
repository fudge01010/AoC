import json
from pprint import pprint

seeds: [int] = []

# maps:
mappings = []
mappings = [[] for i in range(7)]
# seedtosoil = []
# soiltofert = []
# ferttowater = []
# watertolight = []
# lighttotemp = []
# temptohumid = []
# humidtoloc = []


def mapper(range: [[int]], input: int) -> int:
    # print(input)
    # print(range)
    for tmap in range:
        if tmap[1] <= input <= tmap[1] + tmap[2]:
            # seed is within this range
            return input - tmap[1] + tmap[0]
    return input


# load input data in
with open("input.txt", "r") as file:
    input_data = file.read().splitlines()

seeds = [int(x) for x in input_data[0].split()[1:]]
print(input_data)

phase = 0
for row in input_data[2:]:
    if row == "":
        continue
    if not row[0].isnumeric():
        # heading
        if "seed-to-soil" in row:
            phase = 0
        elif "soil-to-ferti" in row:
            phase = 1
        elif "fertilizer-to-water" in row:
            phase = 2
        elif "water-to-light" in row:
            phase = 3
        elif "light-to-temp" in row:
            phase = 4
        elif "temperature-to-humidity" in row:
            phase = 5
        elif "humidity-to-loca" in row:
            phase = 6
        else:
            # shouldn't get here
            pass
    else:
        # is a number
        mappings[phase].append([int(x) for x in (row.split())])
locations = {}
for seed in seeds:
    # run each seed through the mapper fn and store it's "location"
    temp_loc = seed
    for translation_map in mappings:
        temp_loc = mapper(translation_map, temp_loc)
        # print(temp_loc)
    locations[seed] = temp_loc
    print(f"result for {seed} is location {locations[seed]}")

print(
    f"closest seed is {min(locations, key=locations.get)} at {min(locations.values())}"
)
# pprint(mappings)
