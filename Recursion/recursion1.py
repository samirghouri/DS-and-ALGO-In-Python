# Lets take a look at the Fibonacci Series Example

# We have the following conditions
# F(0) = 0, F(1) = 1, F(2) = F(1) + F(0) , F(3) = F(2) +F(1) and so on

#         0,1 when  n =0,1
# F(n) =
#         F(n-1) + F(n-1) when n >=2

# Lets implement the function using two methods - 1.Iteratively 2. Recursively

# 1.Iteratively
'''
# n refers to  nth element
def FibonacciIterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    else:
        F_0 = 0
        F_1 = 1
        for i in range(2, n):
            number = F_0 + F_1
            F_0 = F_1
            F_1 = number
        return number


print(FibonacciIterative(8))
'''

# 2.Recursively
'''
def FibonacciRecursive(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return FibonacciRecursive(n-1)+FibonacciRecursive(n-2)


print(FibonacciRecursive(8))
'''

# Now as we can see that Recusion take much longer the iterative methods
# Because in recusion:
#                             Fib(5)
#                         /             \
#                     Fib(4)           Fib(3)
#                 /           \           /      \
#             Fib(3)           Fib(2)  Fib(2)    Fib(1)
#             /    \       /           \
#         Fib(2)  Fib(1)   Fib(1)      Fib(0)
#         /   \
#     Fib(1)  Fib(0)

#     The calculation of many of numbers are iterative like for n=2,Fib(2) is calculated 3 times
#     So the running time grows exponentially
