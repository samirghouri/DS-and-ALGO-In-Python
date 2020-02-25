# The time complexity of a simple recusrive funtion is proportional to n for factorial of a number
# The space complexity of the same recusrive function is proportional to n for factorial of a number

# the time complexity of a simple recusrive function is proportional to 2^n for fibonacci of a number
# where as the complexity for iterative fibonacci functioni is proportional to n

# Now to make things a bit better we can use recusion with memoization

# Pseudo Code for this -

# Fib(n):
# {
#     if n<=1:
#         return n
#     if F_n is in memory :
#         return F_n
#     else:
#         F_n = Fib(n-1) + Fib(n-2)
#         save F_n in memory
#         return F_n
# }

'''
class FibMem(object):
    def __init__(self):
        self.F_n = [-1]*51

    def Fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        if self.F_n[n] != -1:
            return self.F_n[n]
        self.F_n[n] = self.Fib(n-1)+self.Fib(n-2)
        return self.F_n[n]


obj = FibMem().Fib(40)
print(obj)
'''
# Now the above does not solves the memory problem as much as iterative function
# But it does makes the running time as close to iterative functions
