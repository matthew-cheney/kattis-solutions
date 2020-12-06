line = input().split(' ')
words = set()
msg = 'yes'
for word in line:
    if word in words:
        msg = 'no'
        break
    words.add(word)
print(msg)