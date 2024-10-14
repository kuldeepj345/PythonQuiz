###############################################################################
#                             YouTube: @KuldeepJangidd                        #
###############################################################################
#                             🎉 Easy Python Quiz 🎉                          #
###############################################################################
#                 GitHub Repo: https://github.com/kuldeepj345/PythonQuiz.git   #
###############################################################################

# 31. What is the output of this code?
import itertools

def prime_factors(n):
    for i in itertools.count(2):
        if n <= 1:
            break
        while n % i == 0:
            n //= i
            yield i

print(list(prime_factors(12)))

#A. [2, 2, 3]      #B. [2, 3]
#C. [2, 2, 3, 3]   #D. [3, 4]

# 32. What will this code print?
from collections import defaultdict

d = defaultdict(int)
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'date']
for word in words:
    d[word] += 1

print(sorted(d.items(), key=lambda x: x[1], reverse=True)[0][0])

#A. apple       #B. banana
#C. cherry      #D. date

# 33. What is the result of this code?
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['attribute'] = 'added by metaclass'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(MyClass.attribute)

#A. 'added by metaclass'   #B. None
#C. AttributeError         #D. TypeError

# 34. What does this code print?
def coroutine():
    while True:
        x = yield
        print(x)

c = coroutine()
next(c)
c.send('Hello')
c.send('World')

#A. Hello World      #B. Hello
#C. World            #D. None

# 35. What is the output of this code?
import functools

@functools.singledispatch
def func(arg):
    print(f"Default: {arg}")

@func.register(int)
def _(arg):
    print(f"Integer: {arg}")

@func.register(list)
def _(arg):
    print(f"List: {arg}")

func('test')
func(5)
func([1, 2, 3])

#A. Default: test Integer: 5 List: [1, 2, 3]
#B. test 5 [1, 2, 3]
#C. Default: test Default: 5 Default: [1, 2, 3]
#D. Error

# 36. What will be printed after running this code?
import weakref

class MyClass:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print(f"{self.name} is being deleted")

obj = MyClass("test")
weak_ref = weakref.ref(obj)
print(weak_ref() is obj)
del obj
print(weak_ref() is None)

#A. True False                   #B. True True
#C. True False test is being deleted
#D. True True test is being deleted

# 37. What does this code print?
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def bark(self):
        return "Woof!"

try:
    dog = Dog()
    print(dog.bark())
except TypeError:
    print("TypeError occurred")

#A. Woof!             #B. TypeError occurred
#C. None              #D. AttributeError

# 38. What is the result of this code?
import operator
from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(operator.add, numbers, 0)
print(result)

#A. 10         #B. [1, 2, 3, 4]
#C. 24         #D. Error

# 39. What will this code print?
class ContextManager:
    def __init__(self):
        self.entered = False
    def __enter__(self):
        self.entered = True
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.entered = False

with ContextManager() as cm:
    print(cm.entered)

print(cm.entered)

#A. True True     #B. True False
#C. False True    #D. False False

# 40. What is the output of this code?
from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

print(list(Color))

#A. [Color.RED, Color.GREEN, Color.BLUE]
#B. ['RED', 'GREEN', 'BLUE']
#C. [1, 2, 3]
#D. Error


# Answers:
# 31. A ([2, 2, 3])
# 32. A (apple)
# 33. A ('added by metaclass')
# 34. A (Hello World)
# 35. A (Default: test Integer: 5 List: [1, 2, 3])
# 36. C (True False test is being deleted)
# 37. B (TypeError occurred)
# 38. A (10)
# 39. B (True False)
# 40. A ([Color.RED, Color.GREEN, Color.BLUE])