nums = set()
for i in range(10):
    n = int(input().strip())
    nums.add(n % 42)
print(len(nums))