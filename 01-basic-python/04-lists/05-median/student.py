# Write your code here
def median(ns):
    ns.sort()
    if len(ns) % 2 == 0:
        return (ns[len(ns)//2-1] + ns[len(ns)//2])/2
    return ns[len(ns)//2]
