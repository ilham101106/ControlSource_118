# Task 4: Odd Numbers up to n
n = int(input("Enter the value of n: "))

print(f"Odd numbers up to {n}:")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")
print()
