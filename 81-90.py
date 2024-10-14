###############################################################################
#                             YouTube: @KuldeepJangidd                        #
###############################################################################
#                             🎉 Easy Python Quiz 🎉                          #
###############################################################################
#                 GitHub Repo: https://github.com/kuldeepj345/PythonQuiz.git   #
###############################################################################

# 81. What is the output of this code?
def modify_list(lst):
    lst.append(4)
    lst = [1, 2, 3]
    return lst

numbers = [1, 2, 3]
result = modify_list(numbers)
print(numbers, result)

#A. [1, 2, 3, 4] [1, 2, 3]    #B. [1, 2, 3] [1, 2, 3]
#C. [1, 2, 3, 4] [1, 2, 3, 4] #D. [1, 2, 3] [1, 2, 3, 4]

# 82. What will this code print?
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

#A. Alice is 25 years old
#  Bob is 30 years old
#   Charlie is 35 years old
#B. Error
#C. Alice is 25 years old
#   Bob is 30 years old
#D. Nothing

# 83. What is the result of this code?
numbers = [1, 2, 3, 4, 5]
result = sum(num for num in numbers if num % 2 == 0)
print(result)

#A. 15         #B. 6
#C. [2, 4]     #D. 9

# 84. What does this code print?
class Counter:
    def __init__(self):
        self.count = 0
    
    def __call__(self):
        self.count += 1
        return self.count

c = Counter()
print(c(), c(), c())

#A. 1 2 3      #B. 0 1 2
#C. 1 1 1      #D. Error

# 85. What is the output of this code?
import json

data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_string = json.dumps(data)
print(type(json_string))
print(json_string)

#A. <class 'dict'>
#   {"name": "John", "age": 30, "city": "New York"}
#B. <class 'str'>
#  {"name": "John", "age": 30, "city": "New York"}
#C. <class 'json'>
#   {"name": "John", "age": 30, "city": "New York"}
#D. Error

# 86. What will be printed after running this code?
from datetime import datetime, timedelta

now = datetime.now()
future = now + timedelta(days=7)
print(future.strftime("%A"))

#A. The name of the current day of the week
#B. The name of the day of the week 7 days from now
#C. Error
#D. 7

# 87. What does this code print?
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)

outer()

#A. inner: nonlocal
#   outer: local
#B. inner: nonlocal
#   outer: nonlocal
#C. inner: local
#   outer: local
#D. Error

# 88. What is the result of this code?
import re

text = "The price is $23.45 and £17.89"
pattern = r'\d+\.\d{2}'
result = re.findall(pattern, text)
print(result)

#A. ['$23.45', '£17.89']
#B. ['23.45', '17.89']
#C. ['23', '17']
#D. []

# 89. What will this code print?
class Parent:
    def __init__(self):
        self.value = "Parent"
    
    def show(self):
        print(self.value)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value = "Child"

c = Child()
c.show()

#A. Parent     #B. Child
#C. Error      #D. None

# 90. What is the output of this code?
from collections import defaultdict

words = ['apple', 'banana', 'apple', 'cherry', 'date', 'banana']
word_count = defaultdict(int)

for word in words:
    word_count[word] += 1

print(word_count['fig'])
print(word_count['apple'])

#A. 0
#   2
#B. KeyError
#   2
#C. None
#   2
#D. 0
#   KeyError

# Answers:
# 81. A ([1, 2, 3, 4] [1, 2, 3])
# 82. A (Alice is 25 years old
#       Bob is 30 years old
#       Charlie is 35 years old)
# 83. B (6)
# 84. A (1 2 3)
# 85. B (<class 'str'>
#       {"name": "John", "age": 30, "city": "New York"})
# 86. B (The name of the day of the week 7 days from now)
# 87. B (inner: nonlocal
#       outer: nonlocal)
# 88. B (['23.45', '17.89'])
# 89. B (Child)
# 90. A (0
#        2)