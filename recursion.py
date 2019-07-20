def fac(n):
    if n==0:
        return 1
    else:
        return n * fac(n-1)

#sum  range(1,6) 1+2+3+4+5
def big_sum(n):
    if n==0:
        return n
    else:
        return n + big_sum(n-1)
big_sum(5)

