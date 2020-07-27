from functools import reduce


def work(value):  #остаток от деления на 5
    return value %5

t=[1,4,5,30,99]
m = map(work,t) #---------------------------map это любое действие с каждым элементом списка t
#или m = map (lambda x: x*2, t)
print(list(m))#------------------------> [2,4,20]

##Превратить числа из массива в строки

def work(value):  #
    return str(value)

t=[3,4,90,-2]
m = map(work,t) #---------------------------map это любое действие с каждым элементом списка t
#или m = map (lambda x: x*2, t)
print(list(m))#------------------------> [2,4,20]

## Убрать из массива все строки
t=['some',1,'v',40, '3a', str]
f= filter (lambda x: not isinstance(x,str) , t)
print(list(f))

## подсчитать количество букв в словах

r= ['some','other', 'something']

result = reduce (lambda a,b: a + b, list(len(x) for x in r  ))
print ('Количество букв ', result )