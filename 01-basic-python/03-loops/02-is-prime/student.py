# Write your code here
def is_prime(n):
    i = 2
    if n == 0:
        return False
    if n == 1:
        return False
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True
