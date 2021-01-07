n, m = map(int, input().split())

cards = [list(map(int, input().split())) for _ in range(n)]
nums = []
for i in range(n):
    nums.append(min(cards[i]))
print(max(nums))
