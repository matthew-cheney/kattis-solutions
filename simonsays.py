N = int(input())

SIMON = "Simon says "

for n in range(N):
    line = input()
    if line.startswith(SIMON):
        print(line.split(SIMON)[1])