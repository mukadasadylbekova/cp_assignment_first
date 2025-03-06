n = int(input())

if n == 2 or n == 3:
    print("NO SOLUTION")
else:
    # Print even numbers first
    for i in range(2, n + 1, 2):
        print(i, end=" ")
    # Print odd numbers second
    for i in range(1, n + 1, 2):
        print(i, end=" ")
