line = input()

whites, lowers, uppers = 0, 0, 0

for c in line:
    whites += c == '_'
    lowers += 97 <= ord(c) <= 122
    uppers += 65 <= ord(c) <= 90

print(whites / len(line))
print(lowers / len(line))
print(uppers / len(line))
print((len(line) - (whites + lowers + uppers)) / len(line))