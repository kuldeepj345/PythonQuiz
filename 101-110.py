###############################################################################
#                             YouTube: @KuldeepJangidd                        #
###############################################################################
#                             🎉 Easy Python Quiz 🎉                          #
###############################################################################
#                 GitHub Repo: https://github.com/kuldeepj345/PythonQuiz.git   #
###############################################################################

# 101. What is the output of this code?
text = "Python is awesome"
result = text.replace("o", "0").swapcase()
print(result)

#A. PYTH0N IS AWES0ME    #B. python is awesome
#C. PYTHON IS AWESOME    #D. pyth0n is awes0me

# 102. What will this code print?
numbers = [1, 2, 3, 4, 5]
result = [num if num % 2 == 0 else num * 2 for num in numbers]
print(result)

#A. [2, 2, 6, 4, 10]    #B. [1, 2, 3, 4, 5]
#C. [2, 4, 6, 8, 10]    #D. [1, 4, 3, 8, 5]

# 103. What is the result of this code?
def outer(x):
    def inner(y):
        return x + y
    return inner

closure = outer(10)
print(closure(5))
print(closure(10))

#A. 15 20      #B. 15 25
#C. 10 10      #D. Error

# 104. What does this code print?
import re

text = "The price is $23.45"
pattern = r'\$(\d+\.\d{2})'
match = re.search(pattern, text)
if match:
    print(match.group(1))

#A. $23.45     #B. 23.45
#C. 23         #D. Error

# 105. What is the output of this code?
from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)
print(result)

#A. 15         #B. 120
#C. 60         #D. [1, 2, 3, 4, 5]

# 106. What will be printed after running this code?
class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 2

obj = B()
print(hasattr(obj, 'x'), hasattr(obj, 'y'))

#A. True True    #B. False True
#C. True False   #D. False False

# 107. What does this code print?
import itertools

numbers = [1, 2, 3]
combinations = list(itertools.combinations(numbers, 2))
print(combinations)

#A. [(1, 2), (1, 3), (2, 3)]    #B. [(1, 2), (2, 3)]
#C. [(1, 2), (1, 3)]            #D. [(1, 1), (2, 2), (3, 3)]

# 108. What is the result of this code?
from collections import deque

d = deque([1, 2, 3, 4, 5], maxlen=3)
d.append(6)
print(list(d))

#A. [1, 2, 3]    #B. [4, 5, 6]
#C. [1, 2, 3, 4, 5, 6]    #D. [3, 4, 5]

# 109. What will this code print?
import json

data = '{"name": "John", "age": 30}'
person = json.loads(data)
print(type(person))
print(person['name'])

#A. <class 'dict'>
#   John
#B. <class 'str'>
#   John
#C. <class 'json'>
#   John
#D. Error

# 110. What is the output of this code?
numbers = [1, 2, 3, 4, 5]
result = all(num > 0 for num in numbers) and any(num % 2 == 0 for num in numbers)
print(result)

#A. True       #B. False
#C. [True, True]    #D. Error

# Answers:
# 101. A (PYTH0N IS AWES0ME)
# 102. A ([2, 2, 6, 4, 10])
# 103. A (15 20)
# 104. B (23.45)
# 105. B (120)
# 106. A (True True)
# 107. A ([(1, 2), (1, 3), (2, 3)])
# 108. B ([4, 5, 6])
# 109. A (<class 'dict'>
#        John)
# 110. A (True)