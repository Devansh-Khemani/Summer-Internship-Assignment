# Enter your code here. Read input from STDIN. Print output to STDOUT
S = input().strip()
ans = ""
count = 1
for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        ans += '(' + str(count) + ', ' + S[i] + ') '
        count = 1
    else:
        count += 1

ans += '(' + str(count) + ', ' + S[-1] + ')'
print(ans)
