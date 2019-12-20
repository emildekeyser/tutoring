answers = []

f = open("survey.txt", "r")
for line in f.readlines():
    line = line.strip()
    ans = set(line.split())
    answers.append(ans)
f.close()
print(answers)

teams = {'Bel', 'Eng', 'Ger', 'Ita', 'Fra', 'Spa', 'Cam'}
selected = set()
for an in answers:
    selected = selected.union(an)

print("Teams that are not selected by any fan: ", teams.difference(selected))

count = 0
for an in answers:
    if {'Bel', 'Ger'}.issubset(an):
        count += 1
print("Number of fans who both selected Bel and Ger: ", count)


count = 0
for i in range(len(answers)):
    for j in range(i + 1, len(answers)):
        if len(answers[i].difference(answers[j])) == 0:
            count += 1

print("Number of pairs of fans with the same favorite teams: ", count)
