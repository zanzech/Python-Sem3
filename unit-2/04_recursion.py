def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(0), factorial(1))

# call stack trace
def trace_fact(n, depth=0):
    pad = "  " * depth
    print(f"{pad}factorial({n}) called")
    if n <= 1:
        print(f"{pad}-> base case 1")
        return 1
    res = n * trace_fact(n - 1, depth + 1)
    print(f"{pad}-> returns {res}")
    return res

trace_fact(4)

# recursive countdown
def countdown(n):
    if n <= 0:
        print("Liftoff!")
        return
    print(n)
    countdown(n - 1)

countdown(3)

# fibonacci
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

for i in range(8):
    print(fib(i), end=" ")
print()

# iterative factorial
def fact_loop(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans

print("loop:", fact_loop(5), "| rec:", factorial(5))
