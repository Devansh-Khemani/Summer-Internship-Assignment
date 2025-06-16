from collections import Counter
X = int(input())
shoe_sizes = list(map(int, input().split()))
inventory = Counter(shoe_sizes)
N = int(input())
earned = 0
for _ in range(N):
    size, price = map(int, input().split())
    if inventory[size] > 0:
        earned += price
        inventory[size] -= 1
print(earned)
