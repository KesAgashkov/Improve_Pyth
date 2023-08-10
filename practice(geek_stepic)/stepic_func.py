def matrix(n=1, m = None, value=0):
    if m == None:
        m = n
    return [[value]*m for i in range(n)]