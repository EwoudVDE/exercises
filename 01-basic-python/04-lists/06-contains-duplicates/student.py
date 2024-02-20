# Write your code here
def contains_duplicates(xs):
    a = set(xs)
    if len(a) == len(xs):
        return False
    return True
