###############################################################################
#                             YouTube: @KuldeepJangidd                        #
###############################################################################
#                             🎉 Easy Python Quiz 🎉                          #
###############################################################################
#                 GitHub Repo: https://github.com/kuldeepj345/PythonQuiz.git   #
###############################################################################

# 51. What is the output of this code?
import sys

class Proxy:
    def __init__(self, obj):
        self._obj = obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

class RealClass:
    def method(self):
        print(f"Method called from {self.__class__.__name__}")

proxy = Proxy(RealClass())
proxy.method()

#A. Method called from Proxy
#B. Method called from RealClass
#C. AttributeError
#D. TypeError

# 52. What will this code print?
from typing import Literal

def process_fruit(fruit: Literal["apple", "banana", "cherry"]):
    print(f"Processing {fruit}")

process_fruit("apple")
process_fruit("grape")

#A. Processing apple
#   Processing grape
#B. Processing apple
#   TypeError
#C. Processing apple
#   No error, but mypy would catch it
#D. TypeError

# 53. What is the result of this code?
import operator
from functools import reduce

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

tree = Node(1, Node(2, Node(4), Node(5)), Node(3))

def tree_sum(node):
    if node is None:
        return 0
    return reduce(operator.add, map(tree_sum, (node.left, node.right)), node.value)

print(tree_sum(tree))

#A. 15         #B. 10
#C. 6          #D. Error

# 54. What does this code print?
from contextlib import contextmanager

@contextmanager
def managed_resource(*args):
    print(f"Acquiring {args}")
    yield 42
    print(f"Releasing {args}")

with managed_resource(1, 2) as r, managed_resource(3, 4) as s:
    print(f"Resource values: {r}, {s}")

#A. Acquiring (1, 2)
#   Acquiring (3, 4)
#   Resource values: 42, 42
#   Releasing (3, 4)
#   Releasing (1, 2)
#B. Acquiring (1, 2)
#   Resource values: 42, 42
#   Releasing (1, 2)
#C. Acquiring (1, 2)
#   Acquiring (3, 4)
#   Resource values: 42, 42
#   Releasing (1, 2)
#   Releasing (3, 4)
#D. Error

# 55. What is the output of this code?
import threading
import time

def worker(event):
    print("Worker: Waiting for event")
    event.wait()
    print("Worker: Event received, doing work")

event = threading.Event()
thread = threading.Thread(target=worker, args=(event,))
thread.start()

time.sleep(1)
print("Main: Triggering event")
event.set()
thread.join()

#A. Worker: Waiting for event
#   Main: Triggering event
#   Worker: Event received, doing work
#B. Main: Triggering event
#   Worker: Waiting for event
#   Worker: Event received, doing work
#C. Worker: Waiting for event
#   Worker: Event received, doing work
#   Main: Triggering event
#D. Main: Triggering event
#   Worker: Event received, doing work

# 56. What will be printed after running this code?
from typing import TypedDict

class Movie(TypedDict):
    name: str
    year: int
    rating: float

def print_movie(movie: Movie):
    print(f"{movie['name']} ({movie['year']}): {movie['rating']}")

movie: Movie = {"name": "Inception", "year": 2010, "rating": 8.8}
print_movie(movie)

movie["director"] = "Christopher Nolan"
print_movie(movie)

#A. Inception (2010): 8.8
#   Inception (2010): 8.8
#B. Inception (2010): 8.8
#   TypeError
#C. Inception (2010): 8.8
#   Inception (2010): 8.8
#   (No error, but mypy would catch it)
#D. TypeError

# 57. What does this code print?
from typing import Any

def safe_getattr(obj: Any, attr: str, default: Any = None) -> Any:
    try:
        return object.__getattribute__(obj, attr)
    except AttributeError:
        return default

class MyClass:
    x = 1

    def __getattribute__(self, name):
        if name.startswith('_'):
            raise AttributeError(f"Can't access {name}")
        return super().__getattribute__(name)

obj = MyClass()
print(safe_getattr(obj, 'x'), safe_getattr(obj, '_y', 'default'))

#A. 1 default              #B. 1 None
#C. AttributeError         #D. 1 AttributeError

# 58. What is the result of this code?
import asyncio
from typing import AsyncIterator

async def aiter(iterable):
    for item in iterable:
        yield item
        await asyncio.sleep(0)

async def process():
    async for item in aiter([1, 2, 3]):
        print(item, end=' ')

asyncio.run(process())
print()

#A. 1 2 3     #B. Error
#C. Nothing   #D. 1

# 59. What will this code print?
from dataclasses import dataclass, field
from typing import List, ClassVar

@dataclass
class School:
    name: str
    students: List[str] = field(default_factory=list)
    max_students: ClassVar[int] = 30

    def add_student(self, student: str) -> None:
        if len(self.students) < self.max_students:
            self.students.append(student)

school = School("Python High")
school.add_student("Alice")
print(len(school.students), school.max_students)

#A. 1 30       #B. 1 None
#C. 0 30       #D. AttributeError

# 60. What is the output of this code?
from functools import singledispatchmethod

class Formatter:
    @singledispatchmethod
    def format(self, arg):
        return f"General format: {arg}"

    @format.register
    def _(self, arg: int):
        return f"Int format: {arg:d}"

    @format.register
    def _(self, arg: float):
        return f"Float format: {arg:.2f}"

f = Formatter()
print(f.format("hello"))
print(f.format(42))
print(f.format(3.14159))

#A. General format: hello
#   Int format: 42
#   Float format: 3.14
#B. General format: hello
#   General format: 42
#   General format: 3.14159
#C. TypeError
#D. General format: hello
#   Int format: 42
#   Float format: 3.14159

# Answers:
# 51. B (Method called from RealClass)
# 52. C (Processing apple
#       No error, but mypy would catch it)
# 53. A (15)
# 54. A (Acquiring (1, 2)
#       Acquiring (3, 4)
#       Resource values: 42, 42
#       Releasing (3, 4)
#       Releasing (1, 2))
# 55. A (Worker: Waiting for event
#       Main: Triggering event
#       Worker: Event received, doing work)
# 56. C (Inception (2010): 8.8
#       Inception (2010): 8.8
#       (No error, but mypy would catch it))
# 57. A (1 default)
# 58. A (1 2 3)
# 59. A (1 30)
# 60. A (General format: hello
#         Int format: 42
#         Float format: 3.14)