FID = open("day5Input.txt")
df = FID.readlines()


polymerstart = df[0].rstrip('\n')
# removem = list()


# def cutdown(bigstring):
#     for i in range(1, len(bigstring)):
#         if bigstring[i].isupper() & bigstring[i-1].islower():
#             if bigstring[i] == bigstring[i-1].upper():
#                 removem.append(i-1)
#                 removem.append(i)
#         elif bigstring[i].islower() & bigstring[i-1].isupper():
#             if bigstring[i] == bigstring[i-1].lower():
#                 removem.append(i-1)
#                 removem.append(i)
#     phase2 = list()
#     for k in range(len(bigstring)):
#         if k not in removem:
#             phase2.append(bigstring[k])
#     round2 = ""
#     zed = round2.join(phase2)
#     return zed

def cutdowntwice(bigstring):
    removem = list()
    safespace = list()
    for i in range(1, len(bigstring)):
        if bigstring[i].isupper() & bigstring[i-1].islower() & (i-1) not in safespace:
            if bigstring[i] == bigstring[i-1].upper():
                removem.append(i-1)
                removem.append(i)
                # safespace.append(i-i)
                safespace.append(i)
        elif bigstring[i].islower() & bigstring[i-1].isupper() & (i-1) not in safespace:
            if bigstring[i] == bigstring[i-1].lower():
                removem.append(i-1)
                removem.append(i)
                # safespace.append(i-i)
                safespace.append(i)
    phase2 = list()
    if len(removem) > 1:
        for k in range(len(bigstring)):
            if k not in removem:
                phase2.append(bigstring[k])
        print("phase2", len(phase2), phase2)
        round2 = ""
        zed = round2.join(phase2)
    else:
        zed = bigstring
    return zed


patsy = cutdowntwice(polymerstart)
reggie = cutdowntwice(patsy)
tank = cutdowntwice(reggie)
u = cutdowntwice(tank)
v = cutdowntwice(u)
w = cutdowntwice(v)
x = cutdowntwice(w)
y = cutdowntwice(x)
z = cutdowntwice(y)
print("tank", tank)
print("u", u)
print("v", v)
print("w", w)
print("x", x)
print("y", y)
print("z", z)

# while len(patsy) != len(reggie):
#     # if patsy == reggie:
#     #     print("this is the break")
#     #     print("patsy", patsy)
#     #     print("reggie", reggie)
#
#         # break
#     patsy = cutdowntwice(reggie)
#     reggie = cutdowntwice(patsy)
#     print("not yet")
#
# print("patsy", len(patsy), patsy)
# print("reggie", len(reggie), reggie)



# print(len(bigstring))

# print(bigstring[:20])

# z = list(bigstring)
# print(removem[:20])
# phase2 = list()

# for i in range(len(bigstring)):
#     if i not in removem:
#         phase2.append(bigstring[i])

# print(phase2)

# round2 = ""
# zed = round2.join(phase2)
# print(zed)

