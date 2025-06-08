from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

total_combinations = list(combinations(letters, k))

count_no_a = sum(1 for comb in total_combinations if 'a' not in comb)

probability = 1 - (count_no_a / len(total_combinations))

print(f"{probability:.3f}")
