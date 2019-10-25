import pandas

# open file
dataset = open("day3input.txt")
df = dataset.readlines()
splits = list()

for row in df:
    splits.append(row.split(" "))

commasplit = list()
lwdims = list()
leftstart = list()
topstart = list()
widths = list()
heights = list()

# separate into locations and dimensions
for list in splits:
    commasplit.append(list[2].split(","))
    lwdims.append(list[3].split("x"))

# separate into separate lists as integers after removing non-numerical characters
for line in range(len(commasplit)):
    commasplit[line][1] = commasplit[line][1].rstrip(":")
    leftstart.append(int(commasplit[line][0]))
    topstart.append(int(commasplit[line][1]))

for line in range(len(lwdims)):
    lwdims[line][1] = lwdims[line][1].rstrip("\n")
    widths.append(int(lwdims[line][0]))
    heights.append(int(lwdims[line][1]))

# establis full cloth dimensions
widetotal = max(leftstart) + max(widths)
heighttotal = max(topstart) + max(heights)

# initialize cloth 2D Array
cloth = [[0 for i in range(widetotal+1)] for j in range(heighttotal+1)]

# each claim of cloth on a specific location adds 1 to that location
for i in range(len(splits)):
    for j in range(widths[i]):
        for k in range(heights[i]):
            cloth[leftstart[i]+j][topstart[i]+k] += 1

m = 0
# find locations with more than 1 claim on it (location value >1)
for i in range(widetotal):
    for j in range(heighttotal):
        if cloth[i][j] > 1:
            m += 1
print("Day 3 part 1 Answer:", m)











# --- Day 3: No Matter How You Slice It ---
#
# The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still affecting them - nobody can even agree on how to cut the fabric.
#
# The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.
#
# Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:
#
#     The number of inches between the left edge of the fabric and the left edge of the rectangle.
#     The number of inches between the top edge of the fabric and the top edge of the rectangle.
#     The width of the rectangle in inches.
#     The height of the rectangle in inches.
#
# A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies
# a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall.
# Visually, it claims the square inches of fabric represented by #
# (and ignores the square inches of fabric represented by .) in the diagram below:
#
# ...........
# ...........
# ...#####...
# ...#####...
# ...#####...
# ...#####...
# ...........
# ...........
# ...........
#
# The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:
#
# #1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2
#
# Visually, these claim the following areas:
#
# ........
# ...2222.
# ...2222.
# .11XX22.
# .11XX22.
# .111133.
# .111133.
#
#
# ........
#
# The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not overlap either of them.)
#
# If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric are within two or more claims?
#
# To begin, get your puzzle input.