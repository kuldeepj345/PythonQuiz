###############################################################################
#                             YouTube: @KuldeepJangidd                        #
###############################################################################
#                             🎉 Easy Python Quiz 🎉                          #
###############################################################################
#                 GitHub Repo: https://github.com/kuldeepj345/PythonQuiz.git   #
###############################################################################

# 41. What is the output of this code?
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

stack = Stack[int]()
stack.push(1)
stack.push("2")
print(stack.pop())

#A. 1           #B. "2"
#C. TypeError   #D. No error, but mypy would catch it


# 42. What will this code print?
import asyncio

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))
    print('started')
    await task1
    await task2

asyncio.run(main())

#A. started hello world     #B. started world hello
#C. hello world started     #D. started hello world
                               

# 43. What is the result of this code?
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(4), cube(3))

#A. 8 9        #B. 16 27
#C. 16 9       #D. 8 27

# 44. What does this code print?
class Descriptor:
    def __get__(self, obj, objtype=None):
        return 42
    def __set__(self, obj, value):
        raise AttributeError("Can't set attribute")

class MyClass:
    x = Descriptor()

m = MyClass()
print(m.x)
m.x = 10

#A. 42              #B. 42 AttributeError
#C. None            #D. 10

# 45. What is the output of this code?
import dis

def func():
    a = 1
    b = 2
    return a + b

dis.dis(func)

#A. Bytecode of the function
#B. 3
#C. Error
#D. None

# 46. What will be printed after running this code?
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    friends: list = field(default_factory=list)

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)
p1.friends.append("Charlie")
print(p2.friends)

#A. ["Charlie"]     #B. []
#C. None            #D. Error

# 47. What does this code print?
import itertools

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print(list(itertools.islice(fibonacci(), 10)))

#A. [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#B. [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#C. [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#D. Error

# 48. What is the result of this code?
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """This is the wrapper function"""
        return func(*args, **kwargs)
    return wrapper

@decorator
def greet(name):
    """This function greets a person"""
    print(f"Hello, {name}!")

print(greet.__doc__)

#A. This is the wrapper function
#B. This function greets a person
#C. None
#D. Error

# 49. What will this code print?
import sys

class Capture:
    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self
        self.captured = []
        return self
    def __exit__(self, *args):
        sys.stdout = self.stdout
    def write(self, s):
        self.captured.append(s)
    def __str__(self):
        return ''.join(self.captured)

with Capture() as output:
    print("Hello")
    print("World")

print(output)

#A. Hello World     #B. HelloWorld
#C. Hello World     #D. None
               

# 50. What is the output of this code?
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None:
        ...

class Circle:
    def draw(self) -> None:
        print("Drawing a circle")

def draw_shape(shape: Drawable) -> None:
    shape.draw()

circle = Circle()
draw_shape(circle)

#A. Drawing a circle   #B. TypeError
#C. None               #D. Error

# Answers:
# 41. D (No error, but mypy would catch it)
# 42. D (started hello
#       world)
# 43. B (16 27)
# 44. B (42 AttributeError)
# 45. A (Bytecode of the function)
# 46. B ([])
# 47. A ([0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
# 48. B (This function greets a person)
# 49. C (Hello
#       World)
# 50. A (Drawing a circle)