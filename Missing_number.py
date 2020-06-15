n = int(input())
s = [int(x) for x in input().split()]

sums = sum(s)

print((n*(n+1))//2 - sums)
