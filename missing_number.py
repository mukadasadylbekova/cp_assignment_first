n = int(input())
arr = list(map(int, input().split()))

total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
actual_sum = sum(arr)         # Sum of given numbers

missing_number = total_sum - actual_sum
print(missing_number)
