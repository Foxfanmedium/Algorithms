from collections import Counter

"""
Варианты создания счетчиков
"""
# a = Counter()
# b = Counter('abracadabra')
# c = Counter({'red': 2, 'white': 3})
# d = Counter(cats=4, dogs=1)
# print(a, b, c, d, sep='\n')

# >>>
# Counter()
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
# Counter({'white': 3, 'red': 2})
# Counter({'cats': 4, 'dogs': 1})

# print(b['z'])
# >>> 0

# b['z'] = 4
# print(a, b, c, d, sep='\n')
# >>>
# Counter()
# Counter({'a': 5, 'z': 4, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
# Counter({'white': 3, 'red': 2})
# Counter({'cats': 4, 'dogs': 1})

# print(b.elements())
# >>> <itertools.chain object at 0x000001E47AC20320>
# print(list(b.elements()))
# >>> ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'c', 'd', 'z', 'z', 'z', 'z']

# print(b.most_common(2))
# # >>> [('a', 5), ('z', 4)]


# e = Counter(a=4, b=5, c=-2, d=0)
# f = Counter(a=2, b=3, c=1, d=-2)
# print(e, f)
# >>> Counter({'b': 5, 'a': 4, 'd': 0, 'c': -2}) Counter({'b': 3, 'a': 2, 'c': 1, 'd': -2})

# print(e + f)
# >>> Counter({'b': 8, 'a': 6})

# print(e - f)
# >>> Counter({'a': 2, 'b': 2, 'd': 2})

# print( e & f)  >>> Counter({'b': 3, 'a': 2})
# print( e | f)  >>> Counter({'b': 5, 'a': 4, 'c': 1})


# =====================================================================================================================
"""
Очереди основаны на словаре
"""

from collections import deque
# a = deque()
# b = deque('abcd')
# c = deque([1,2,3,4,5])
# print(a,b,c, sep='\n')
# >>> deque([])
# >>> deque(['a', 'b', 'c', 'd'])
# >>> deque([1, 2, 3, 4, 5])


# b = deque('abcd', maxlen=2)
# c = deque([1,2,3,4,5], maxlen=4)
# print('', b,c, sep='\n')
# >>> deque(['c', 'd'], maxlen=2)
# >>> deque([2, 3, 4, 5], maxlen=4)

# d = deque([i for i in range(5)], maxlen=7)
# d.append(5)
# d.appendleft(6)
# print(d)
# >>> deque([6, 0, 1, 2, 3, 4, 5], maxlen=7)

# d.extend([7,8])
# print(d)
# >>> deque([1, 2, 3, 4, 5, 7, 8], maxlen=7)

# d.extendleft([9, 10])
# print(d)
# >>> deque([10, 9, 1, 2, 3, 4, 5], maxlen=7)


# spam = d.popleft()
# print(spam) >>> 10
# print(d) >>> deque([9, 1, 2, 3, 4, 5], maxlen=7)

# print('*' * 50)
# d.reverse()
# print(d)
# >>> deque([5, 4, 3, 2, 1, 9, 10], maxlen=7)

# d.rotate(2)
# print(d)  >>> deque([9, 10, 5, 4, 3, 2, 1], maxlen=7)


# =====================================================================================================================
from collections import defaultdict

# a = defaultdict()
# print(a)

# >>> defaultdict(None, {})

# s = 'abracadabra'
# b = defaultdict(int)
# for i in s:
#     b[i] +=1
# print(b)
# >>> defaultdict(<class 'int'>, {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})


# list_1 = [('cat', 1), ('dog', 2), ('cat', 3), ('dog', 2)]
# c1 = defaultdict(list)
# for key, value in list_1:
#     c1[key].append(value)
# print(c1)
# >>> defaultdict(<class 'list'>, {'cat': [1, 3], 'dog': [2, 2]})

# for key, value in c.items():
#     print(key)
# >>> cat
# >>> dog

# list_2 = [('cat', 1), ('dog', 2), ('cat', 3), ('dog', 2), ('cat', 33)]
# d = defaultdict(set)
# for key, value in list_2:
#     d[key].add(value)
#
# print(d)
# >>> defaultdict(<class 'set'>, {'cat': {1, 3, 33}, 'dog': {2}})

# =====================================================================================================================

# from collections import OrderedDict
#
# a = {'cat': 5,'mouse': 4, 'dog': 2}
# new_a = OrderedDict(sorted(a.items(), key=lambda x: x[0]))
# print(new_a)
# >>> OrderedDict([('cat', 5), ('dog', 2), ('mouse', 4)])
# b = {'cat': 5,'mouse': 4, 'dog': 2}
# new_b = OrderedDict(sorted(a.items(), key=lambda x: x[1]))
# print(new_b)
# >>> OrderedDict([('dog', 2), ('mouse', 4), ('cat', 5)])

# print(a == b)
# >>> True
# print(new_a == new_b)
# >>> False

# new_b['mouse'] = 55
# print(new_b) >>> OrderedDict([('dog', 2), ('mouse', 55), ('cat', 5)])

# new_b['horse'] = 1
# print(new_b)   >>> OrderedDict([('dog', 2), ('mouse', 55), ('cat', 5), ('horse', 1)])


# new_b.move_to_end('mouse')
# print(new_b)    >>> OrderedDict([('dog', 2), ('cat', 5), ('horse', 1), ('mouse', 55)])

# new_b.move_to_end('mouse', last = False)
# print(new_b)   >>> OrderedDict([('mouse', 55), ('dog', 2), ('cat', 5), ('horse', 1)])

# new_b.popitem()
# print(new_b)   >>> OrderedDict([('mouse', 55), ('dog', 2), ('cat', 5)])

# new_b.popitem(last=False)
# print(new_b)   >>> OrderedDict([('dog', 2), ('cat', 5), ('horse', 1)])


# =====================================================================================================================

from collections import namedtuple

# hero_1 = {'Nike', 'nigga', 100, 250}

# print(hero_1)


# class Person:
#     def __init__(self, name, race, health, armor):
#         self.health = health
#         self.armor = armor
#         self.name = name
#         self.race = race


# hero_2 = Person('Nike', 'nigga', 100, 250)
#
# print(hero_2.health)

# New_Person = namedtuple('New_Person', 'name, race, health, armor') # Создание класса за 1 строчку кода
# hero_3 = New_Person('Nike', 'nigga', 100, 250)
# print(hero_3)
# >>> New_Person(name='Nike', race='nigga', health=100, armor=250)
# print('*' * 50)
Point = namedtuple('Point', 'x y z') # Первый аргумент = имя класса, второй аргумент = перечисление аргументов класса

# p1 = Point(2, z=5, y=3)
# print(p1)   >>> Point(x=2, y=3, z=5)
# print(p1.x)   >>> 2


t = [5, 10, 15]
p2 = Point._make(t)
# print(p2)        >>> Point(x=5, y=10, z=15)



# d2 = p2._asdict()
# print(d2)      >>> OrderedDict([('x', 5), ('y', 10), ('z', 15)])


# p2.x = 6

p2 = p2._replace(x = 6)
print(p2)    >>> Point(x=6, y=10, z=15)







