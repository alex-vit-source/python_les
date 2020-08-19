import random

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b, a+b

#x=fib()
#print (next(x))

def  task1():
    a1 = random.randint(0,100)
    while True:
        yield a1
        a1 = random.randint(0,100)

y=task1()
print(next(y))


z=gen_range(1,20)


