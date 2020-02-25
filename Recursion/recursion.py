# lets start with a basic example of factorial

# Factorial of n = n*(n-1)*(n-2)....*3*2*1

# Now when we use recursion to calculate the above
# ----------Pseudo code---------
# Factorial(n){
#     if n == 0:
#       return 1
#     else:
#       return n*Factorial(n-1)
# }
# Function        return            state
#  F(4)            4*F(3)           Paused
#  F(3)            3*F(2)           Paused
#  F(2)            2*F(1)           Paused
#  F(1)            1*F(0)           Paused
#  F(0)            1                -


def factorial(n):
    print("Calculating F({})".format(n))
    if n == 0:
        return 1
    F = n*factorial(n-1)
    print("Done Calculating F({})".format(n))
    return F


print(factorial(5))
