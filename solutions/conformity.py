N = int(input())

combos = dict()

for n in range(N):
    courses = sorted(input().split(' '))
    tupCourses = tuple(courses)
    if tupCourses not in combos:
        combos[tupCourses] = 0
    combos[tupCourses] += 1

maxCombo = max(combos.values())

print(sum([v for v in combos.values() if v == maxCombo]))