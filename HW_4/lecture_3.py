"""
Terminal:
$ python -m timeit -n 100 -s "import lecture_3" "lecture_3.fib(10)"

"""
import sys
import cProfile
import functools

sys.setrecursionlimit(1001)


# рекурсия
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n - 1) + fib(n - 2)

# Вариант обертывания в декоратор @functools - кэширование данных приводит к ускорению обработки почти
# в 10 раз в данном случае
@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# 100 loops, best of 3: 0.111 usec per loop - lru_cache 10

cProfile.run('fib(10)')
# 11/1    0.000    0.000    0.000    0.000 lecture_3.py:24(fib) - всего 11 вызовов рекурсии!!!

# cProfile.run('fib(10)')
# 177/1    0.000    0.000    0.000    0.000 lecture_3.py:8(fib)
# cProfile.run('fib(15)')
# 1973/1    0.000    0.000    0.000    0.000 lecture_3.py:8(fib)
# рекурсия + словарь

def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:  # проверка по ключам
            return fib_d[n]
        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)

# 100 loops, best of 3: 3.61 usec per loop - 10
# 100 loops, best of 3: 5.31 usec per loop - 15
# 100 loops, best of 3: 7.02 usec per loop - 20
# 100 loops, best of 3: 45.2 usec per loop - 100

# cProfile.run('fib_dict(10)')
# 19/1    0.000    0.000    0.000    0.000 lecture_3.py:31(_fib_dict)
# cProfile.run('fib_dict(100)')
# 199/1    0.000    0.000    0.000    0.000 lecture_3.py:31(_fib_dict)



# цикл
def fib_loop(n):
    if n < 2:
        return n
    first = 0
    second = 1
    for i in range(2, n + 1):
        first, second = second, first + second
    return second


# print(fib_loop(8))
# 100 loops, best of 3: 1.45 usec per loop - 10
# 100 loops, best of 3: 1.06 usec per loop - 15
# 100 loops, best of 3: 1.3 usec per loop - 20




# def test_fib(func):
#     lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#     for i, item in enumerate(lst):
#         assert item == func(i)
#         print(f'Test {i} OK')


# test_fib(fib)
# test_fib(fib_dict)





"""
Выводы урока:
1) Рекурсия плохо - увеличивает время обработки данных
2) Технология мемолизации ускоряет рекурсию
3) Вычисления на прямую и в цикле это бытро
4) Встроеное кэширование позволяет ускорить рекурсию 
"""