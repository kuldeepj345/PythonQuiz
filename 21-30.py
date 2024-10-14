###############################################################################
#                             YouTube: @KuldeepJangidd                        #
###############################################################################
#                             🎉 Easy Python Quiz 🎉                          #
###############################################################################
#                 GitHub Repo: https://github.com/kuldeepj345/PythonQuiz.git   #
###############################################################################

# 21. What is the output of this code?
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5))

#A. 3          #B. 5
#C. 8          #D. 13

# 22. What will this code print?
import asyncio

async def foo():
    print("Start foo")
    await asyncio.sleep(0)
    print("End foo")

async def main():
    tasks = [asyncio.create_task(foo()) for _ in range(2)]
    await asyncio.gather(*tasks)

asyncio.run(main())

#A. Start foo End foo Start foo End foo
#B. Start foo Start foo End foo End foo
#C. Start foo End foo
#D. Error

# 23. What is the result of this code?
class A:
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x
    def __hash__(self):
        return hash(self.x)

s = set([A(1), A(2), A(1)])
print(len(s))

#A. 1          #B. 2
#C. 3          #D. Error

# 24. What does this code print?
import sys

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

sys.setrecursionlimit(10)
try:
    print(factorial(11))
except RecursionError:
    print("RecursionError occurred")

#A. 39916800               #B. RecursionError occurred
#C. None                   #D. Error

# 25. What is the output of this code?
from contextlib import suppress

def divide(a, b):
    with suppress(ZeroDivisionError):
        return a / b
    return "Division by zero"

print(divide(5, 2), divide(5, 0))

#A. 2.5 Division by zero   #B. 2.5 None
#C. 2.5 Error              #D. Error Error

# 26. What will be printed after running this code?
from dataclasses import dataclass

@dataclass(order=True)
class Person:
    name: str
    age: int

people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
print(min(people).name)

#A. Alice      #B. Bob
#C. Charlie    #D. Error

# 27. What does this code print?
def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1
        return x
    return inner

counter = outer()
print(counter(), counter(), counter())

#A. 1 1 1      #B. 1 2 3
#C. 0 1 2      #D. Error

# 28. What is the result of this code?
import re

text = "The price is $23.45 and £17.89"
pattern = r'\$\d+\.\d{2}|\£\d+\.\d{2}'
result = re.findall(pattern, text)
print(result)

#A. ['$23.45']
#B. ['$23.45', '£17.89']
#C. ['23.45', '17.89']
#D. []

# 29. What will this code print?
from typing import List, Tuple

def process(data: List[Tuple[int, str]]) -> List[str]:
    return [b.upper() for a, b in data if a > 5]

result = process([(3, "apple"), (7, "banana"), (1, "cherry"), (8, "date")])
print(result)

#A. ['APPLE', 'BANANA', 'CHERRY', 'DATE']
#B. ['BANANA', 'DATE']
#C. ['apple', 'banana', 'cherry', 'date']
#D. []

# 30. What is the output of this code?
import inspect

def foo(a: int, b: str = "hello") -> bool:
    return True

print(inspect.signature(foo))

#A. (a: int, b: str = 'hello') -> bool
#B. (a, b='hello')
#C. foo(a: int, b: str = "hello") -> bool
#D. Error


# Answers:
# 21. B (5)
# 22. B (Start foo Start foo End foo End foo)
# 23. B (2)
# 24. B (RecursionError occurred)
# 25. A (2.5 Division by zero)
# 26. B (Bob)
# 27. B (1 2 3)
# 28. B (['$23.45', '£17.89'])
# 29. B (['BANANA', 'DATE'])
# 30. A ((a: int, b: str = 'hello') -> bool)