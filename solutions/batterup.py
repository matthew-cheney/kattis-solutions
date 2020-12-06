N = input()
bats = [int(ea) for ea in input().split(' ') if ea != '-1']
print(sum(bats) / len(bats))