###############################################################################
#                             YouTube: @KuldeepJangidd                        #
###############################################################################
#                             🎉 Easy Python Quiz 🎉                          #
###############################################################################
#                 GitHub Repo: https://github.com/kuldeepj345/PythonQuiz.git   #
###############################################################################

# 61. What is the output of this code?
from typing import NewType, List

UserId = NewType('UserId', int)
GroupId = NewType('GroupId', int)

def process_user(user_id: UserId):
    print(f"Processing user {user_id}")

def process_group(group_id: GroupId):
    print(f"Processing group {group_id}")

user_id = UserId(1)
group_id = GroupId(1)

process_user(user_id)
process_group(group_id)
process_user(group_id)

#A. Processing user 1
#   Processing group 1
#   Processing user 1
#B. Processing user 1
#   Processing group 1
#   TypeError
#C. Processing user 1
#   Processing group 1
#   Processing user 1
#   (No error, but mypy would catch it)
#D. TypeError'''

# 62. What will this code print?
import sys

class Metaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['x'] = 42
        return super().__new__(cls, name, bases, attrs)

class Base:
    pass

class Derived(Base, metaclass=Metaclass):
    pass

print(hasattr(Base, 'x'), hasattr(Derived, 'x'))

#A. False True    #B. True True
#C. False False   #D. True False

# 63. What is the result of this code?
from functools import cache

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))

#A. RuntimeError (maximum recursion depth exceeded)
#B. 354224848179261915075 (correct Fibonacci number)
#C. OverflowError
#D. Hangs indefinitely

# 64. What does this code print?
from typing import Callable, TypeVar

T = TypeVar('T')
U = TypeVar('U')

def compose(f: Callable[[U], T], g: Callable[[T], U]) -> Callable[[T], T]:
    return lambda x: f(g(x))

def double(x: int) -> int:
    return x * 2

def square(x: int) -> int:
    return x ** 2

composed = compose(double, square)
print(composed(3))

#A. 18         #B. 36
#C. 9          #D. TypeError

# 65. What is the output of this code?
import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(1)
    return "Data"

async def process_data(data):
    print(f"Processing {data}...")
    await asyncio.sleep(1)
    return f"Processed {data}"

async def main():
    data = await fetch_data()
    result = await process_data(data)
    print(result)

asyncio.run(main())


#A. Fetching data...
#   Processing Data...
#   Processed Data
#B. Fetching data...
#   Data
#   Processing Data...
#   Processed Data
#C. Processed Data
#D. Error          '''

# 66. What will be printed after running this code?
from typing import Protocol, runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None:
        print("Drawing a circle")

class Square:
    def draw(self) -> None:
        print("Drawing a square")

def draw_shape(shape: Drawable):
    shape.draw()

shapes = [Circle(), Square(), "Not a shape"]
for shape in shapes:
    if isinstance(shape, Drawable):
        draw_shape(shape)
    else:
        print(f"{shape} is not drawable")

#A. Drawing a circle
#   Drawing a square
#  Not a shape is not drawable
#B. Drawing a circle
#   Drawing a square
#   AttributeError
#C. TypeError
#D. Drawing a circle
#   Drawing a square    

# 67. What does this code print?
import dis

def func(x):
    if x > 0:
        return x
    else:
        return -x

dis.dis(func)
print(func.__code__.co_nlocals)

#A. Disassembly of the function
#   1
#B. Disassembly of the function
#   2
#C. 1
#D. Error 

# 68. What is the result of this code?
from typing import List, TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

def process_stack(stack: Stack[int]) -> None:
    while stack.items:
        item = stack.pop()
        print(item)

int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
int_stack.push("3")  # Type error, but will run

process_stack(int_stack)

#A. 3
#   2
#   1
#B. 2
#   1
#C. TypeError
#D. 3
#   2
#   1
#   (No error at runtime, but mypy would catch it)   '''

# 69. What will this code print?
from dataclasses import dataclass, field
from typing import List, Any

@dataclass
class Node:
    value: Any
    children: List['Node'] = field(default_factory=list)

    def __post_init__(self):
        self.parent: 'Node' = None
        for child in self.children:
            child.parent = self

root = Node(1, [Node(2), Node(3)])
print(root.children[0].parent.value)

#A. 1          #B. 2
#C. 3          #D. None

# 70. What is the output of this code?
from typing import overload, Union

class MyClass:
    @overload
    def method(self, arg: int) -> int: ...
    
    @overload
    def method(self, arg: str) -> str: ...
    
    def method(self, arg: Union[int, str]) -> Union[int, str]:
        if isinstance(arg, int):
            return arg * 2
        elif isinstance(arg, str):
            return arg.upper()

obj = MyClass()
print(obj.method(5))
print(obj.method("hello"))


#A. 10
#   HELLO
#B. TypeError
#C. 5
#  hello
#D. Error

# Answers:
# 61. C (Processing user 1
#       Processing group 1
#       Processing user 1
#       (No error, but mypy would catch it))
# 62. A (False True)
# 63. B (354224848179261915075 (correct Fibonacci number))
# 64. A (18)
# 65. A (Fetching data...
#       Processing Data...
#       Processed Data)
# 66. A (Drawing a circle
#       Drawing a square
#       Not a shape is not drawable)
# 67. A (Disassembly of the function
#       1)
# 68. D (3
#       2
#       1
#       (No error at runtime, but mypy would catch it))
# 69. A (1)
# 70. A (10
#        HELLO)