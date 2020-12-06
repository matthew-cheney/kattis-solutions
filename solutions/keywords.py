N = int(input())

keywords = set()

for n in range(N):
    word = input().strip()
    word = word.replace('-', ' ')
    word = word.lower()
    keywords.add(word)

print(len(keywords))