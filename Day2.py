import collections

whatsit = open("/home/david/Projects/advent/day2input.txt")
df = whatsit.readlines()

for row in (range(len(df))):
    df[row] = df[row].rstrip('\n')



double = 0
triple = 0

for line in range(len(df)):
    cnt = collections.Counter(df[line])
    chunk = 0
    chunker = 0

    for num in cnt.values():

        if num == 2:
            chunk += 1
        if num == 3:
            chunker += 1

    if chunk > 0:
        double += 1
    if chunker > 0:
        triple += 1

d2pt1answer = double*triple
print("Day 2 part 1 answer:", d2pt1answer)

for row in df:
    for otherrows in df:
        if otherrows > row:
            similarity = 0
            for i in range(len(row)):
                if row[i] == otherrows[i]:
                    similarity += 1
                if similarity == len(row)-1:
                    # print(row, otherrows)
                    answer = list()
                    for j in range(len(row)):
                        if row[j] == otherrows[j]:
                            # answer = list()
                            answer.append(row[j])
                    print("Day 2 part 2 answer is ", ''.join(answer))
