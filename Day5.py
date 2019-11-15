FID = open("day5Input.txt")
df = FID.readlines()


polymerstart = df[0].rstrip('\n')


def reduce(a):
    seconde = []
    for i in a:
        if not seconde:
            seconde.append(i)
        elif i == seconde[-1].swapcase():
            seconde.pop()
        else:
            seconde.append(i)
    return len(seconde)


def findbest(baker):
    testarooni = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        wild = baker.replace(i.lower(), '')
        salmon = wild.replace(i.upper(), '')
        testarooni.append(reduce(salmon))
    return min(testarooni)


print("day 5 part 1 answer:", reduce(polymerstart))
print("Day 5 part 2 answer:", findbest(polymerstart))



