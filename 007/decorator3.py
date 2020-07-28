import time

def counter(func):
     """
     Декоратор, считающий и выводящий количество вызовов
     декорируемой функции и затраченное время на выпонение
     """
     def wrapper(*args, **kwargs):
         wrapper.count += 1
         t = time.clock()
         res = func(*args, **kwargs)
         print('На функцию ',func.__name__,' затрачено ', time.clock() - t, ' сек')
         print("{0} была вызвана: {1}x".format(func.__name__, wrapper.count))
         return res
     wrapper.count = 0
     return wrapper



@counter
def reverse_string(string):
    return ''.join(reversed(string))

print(reverse_string("А роза упала на лапу Азора"))
print(reverse_string("А роза упала на лапу Азора"))
