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

for i in range(len(splits)):
    yes = 0
    for j in range(widths[i]):
        for k in range(heights[i]):
            if cloth[leftstart[i]+j][topstart[i]+k] == 1:
                yes += 1
                if yes == widths[i]*heights[i]:
                    print("answer:", i+1)



# m = 0
# find locations with more than 1 claim on it (location value >1)
# for i in range(widetotal):
#     for j in range(heighttotal):
#         if cloth[i][j] > 1:
#             m += 1
# print("Day 3 part 1 Answer:", m)




