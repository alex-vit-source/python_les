import random

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b, a+b

#x=fib()
#print (next(x))
'''
def  task1():
    a1 = random.randint(0,100)
    while True:
        yield a1
        a1 = random.randint(0,100)

y=task1()
print(next(y))


z=gen_range(1,20,2)

def task2(a,b,step):
    c = a
    while c <= b:
        yield c
        c = c + step

z = task2(1,100,5)
print(next(z))
print(next(z))
print(next(z))
print(next(z))

def work(value):  #остаток от деления на 5
    return value * 5

def task3(func,t):
    for i in t:
        result= func(i)
        yield result

z = task3 (work,[1,4,5,30,99])
while True:
       
    try:
        print(next(z))
    except StopIteration as e:
        print ('Работа окончена', e)
        break

'''
def my_zip(a,b,c):
    l = len(a)
    i = 0
    while i < l :
        yield (a[i],b[i],c[i])
        i += 1

a1 = [[12,123,123],
     [123,123,123],
     [45,123,234]]
b1 = 'qwe'
c1 = ('asd', 23, True)
z = my_zip(a1,b1,c1)
while True:
       
    try:
        print(next(z))
    except StopIteration as e:
        print ('Работа окончена', e)
        break