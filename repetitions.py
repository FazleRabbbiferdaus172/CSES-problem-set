s = input()
ans, c, a = 1, 0, s[0]
for i in s:
    if i == a:
        c += 1
        ans = max(c, ans)
    else:
        a = i
        c = 1

print(ans)
