from collections import defaultdict

dataset = open("day4Input.txt")
df = dataset.readlines()

ttt = sorted(df)
splits = list()
guardlist = list()
guardsleeps = defaultdict(int)
guardminutes = defaultdict(lambda: defaultdict(int))


def timecheck(linein):
    return linein[0].split(" ")[1].split(":")[1]


for row in ttt:  # clean up data
    row = row.rstrip("\n")
    row = row.replace('[', '')
    splits.append(row.split("]"))

for line in splits:
    if 'begins shift' in line[1]:
        guardph = line[1].find('#') + 1
        guardnumber = line[1][guardph:(guardph + 4)]
        if guardnumber not in guardlist:
            guardlist.append(guardnumber)
            guardsleeps[guardnumber]
            guardminutes[guardnumber]
    elif 'falls asleep' in line[1]:
        start = timecheck(line)
    elif 'wakes up' in line[1]:
        # print(line)
        end = timecheck(line)
        for sleeptime in range(int(start), int(end)):
            guardminutes[guardnumber][sleeptime] += 1


guardchoice = 0
maxminutes = 0
minutechoice = 0
mostsleep = 0

for guard in guardlist:
    for minute in guardminutes[guard]:
        if guardminutes[guard][minute] > maxminutes:
            maxminutes = int(guardminutes[guard][minute])
            guardchoice = int(guard)
            minutechoice = int(minute)
        guardsleeps[guard] += guardminutes[guard][minute]

day4pt2answer = guardchoice * minutechoice

for guard in guardlist:
    if guardsleeps[guard] > mostsleep:
        mostsleep = guardsleeps[guard]
        guardchoice = guard

maxminutes = 0

for minute in guardminutes[guardchoice].keys():
    if guardminutes[guardchoice][minute] > maxminutes:
            maxminutes = int(guardminutes[guardchoice][minute])
            minutechoice = int(minute)

print("Day 4 part 1 Answer:", minutechoice * int(guardchoice))
print("Day 4 part 2 answer:", day4pt2answer)
