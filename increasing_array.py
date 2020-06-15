n = int(input())
arr = [int(x) for x in input().split()]
m, ans = arr[0], 0

for i in arr:
    m = max(m, i)
    ans += m - i

print(ans)
