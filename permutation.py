n = int(input())

if n == 1:
    print(1)
elif n == 2 or n == 3:
    print("NO SOLUTION")
elif n % 2 == 0:
    for i in range(2, n+1, 2):
        print(i, end=" ")
    for i in range(1, n, 2):
        print(i, end=" ")
else:
    for i in range(2, n, 2):
        print(i, end=" ")
    for i in range(1, n+1, 2):
        print(i, end=" ")
