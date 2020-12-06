N = int(input())
papers = list()
for n in range(N):
    papers.append(int(input()))

papers.sort()
lpapers = len(papers)
ans = 0
for i in range(lpapers):
    if papers[i] >= lpapers - i:
        ans = lpapers - i
        break
print(ans)