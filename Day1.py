import numpy as np
import pandas

df = pandas.read_csv("/home/david/Projects/advent/input.csv", header=None, squeeze=True)

summinglist = np.cumsum(df)
answer = summinglist.loc[len(summinglist)-1]


print("Day 1 part 1 answer:", answer)
# df = pandas.read_csv("/home/david/Projects/advent/input.csv", header=None, squeeze=True)

rangetop = len(df)
runner = [0]


for p in range(0, 200):

    for i in range(0, rangetop):
        runner.append(df.loc[i] + runner[-1])


def firstDuplicate(a):
    oldies={}
    notfound=True
    for i in range(len(a)):
        try:
            if oldies[a[i]]==a[i]:
                notfound=False
                return a[i]
        except:
            oldies[a[i]]=a[i]
    if notfound:
        return -1


jerb = firstDuplicate(runner)
print("Day 1 part 2 answer:", jerb)
