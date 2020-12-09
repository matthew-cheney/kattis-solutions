N = int(input())
ans = list(input())

adrian = ['A', 'B', 'C']*40
bruno = ['B', 'A', 'B', 'C']*40
goran = ['C', 'C', 'A', 'A', 'B', 'B']*40

adrian = sum([ans[i] == adrian[i] for i in range(N)])
bruno = sum([ans[i] == bruno[i] for i in range(N)])
goran = sum([ans[i] == goran[i] for i in range(N)])

M = max(adrian, bruno, goran)
print(M)
if adrian == M:
    print('Adrian')
if bruno == M:
    print('Bruno')
if goran == M:
    print('Goran')