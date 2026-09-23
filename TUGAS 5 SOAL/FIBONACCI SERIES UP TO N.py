# Task 3: Fibonacci Series up to n
n = int(input("Enter the value of n: "))

a, b = 0, 1
print(f"Fibonacci series up to {n} terms:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
