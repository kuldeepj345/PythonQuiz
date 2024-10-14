###############################################################################
#                             YouTube: @KuldeepJangidd                        #
###############################################################################
#                             🎉 Easy Python Quiz 🎉                          #
###############################################################################
#                 GitHub Repo: https://github.com/kuldeepj345/PythonQuiz.git   #
###############################################################################

# 91. What is the output of this code?
numbers = [1, 2, 3, 4, 5]
squared = (x**2 for x in numbers)
print(list(squared))
print(list(squared))

#A. [1, 4, 9, 16, 25]
#   [1, 4, 9, 16, 25]
#B. [1, 4, 9, 16, 25]
#   []
#C. [1, 4, 9, 16, 25]
#   [1, 4, 9, 16, 25]
#D. Error

# 92. What will this code print?
import random
random.seed(42)
print(random.randint(1, 10))
print(random.randint(1, 10))

#A. Different random numbers each time
#B. The same two random numbers each time
#C. 42
#   42
#D. Error

# 93. What is the result of this code?
text = "hello world"
result = text.split()
print(result)
print(len(result))

#A. ['hello', 'world']
#   2
#B. ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
#   11
#C. 'hello world'
#   1
#D. Error

# 94. What does this code print?
def multiply(a, b=2):
    return a * b

print(multiply(3))
print(multiply(3, 3))
print(multiply(b=3, a=3))

#A. 6
#   9
#   9
#B. 6
#   9
#   6
#C. Error
#D. 3
#   9
#   9

# 95. What is the output of this code?
numbers = [1, 2, 3, 4, 5]
even_sum = sum(filter(lambda x: x % 2 == 0, numbers))
print(even_sum)

#A. 6          #B. 9
#C. [2, 4]     #D. 15

# 96. What will be printed after running this code?
import os

current_dir = os.getcwd()
file_name = "example.txt"
full_path = os.path.join(current_dir, file_name)
print(os.path.basename(full_path))

#A. The full path to example.txt
#B. example.txt
#C. The current working directory
#D. Error

# 97. What does this code print?
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

dog = Dog("Buddy")
print(dog.speak())

#A. Buddy says Woof!
#B. NotImplementedError
#C. None
#D. Error

# 98. What is the result of this code?
import itertools

numbers = [1, 2, 3]
permutations = list(itertools.permutations(numbers))
print(len(permutations))
print(permutations[0])

#A. 6
#   (1, 2, 3)
#B. 3
#   [1, 2, 3]
#C. 9
#   (1, 2, 3)
#D. 6
#   [1, 2, 3]

# 99. What will this code print?
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])
p = Person('Alice', 30, 'New York')
print(p.name)
print(p[1])

#A. Alice
#   30
#B. Alice
#   New York
#C. Error
#D. name
#   1

# 100. What is the output of this code?
import datetime

date_string = "2023-06-15"
date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d")
print(date_object.strftime("%B %d, %Y"))

#A. 2023-06-15
#B. June 15, 2023
#C. Error
#D. 15 June 2023

# Answers:
# 91. B ([1, 4, 9, 16, 25]
#       [])
# 92. B (The same two random numbers each time)
# 93. A (['hello', 'world']
#       2)
# 94. A (6
#       9
#       9)
# 95. A (6)
# 96. B (example.txt)
# 97. A (Buddy says Woof!)
# 98. A (6
#       (1, 2, 3))
# 99. A (Alice
#       30)
# 100. B (June 15, 2023)