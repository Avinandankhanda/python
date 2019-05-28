import timeit
def test():
    odd_number=[]
    for a in range(0,100000):
        if a%2==0:
            pass
        else :
            odd_number.append(a)

print(timeit.timeit("test()"))