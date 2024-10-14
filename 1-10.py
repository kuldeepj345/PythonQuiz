###############################################################################
#                             YouTube: @KuldeepJangidd                        #
###############################################################################
#                             🎉 Easy Python Quiz 🎉                          #
###############################################################################
#                 GitHub Repo: https://github.com/kuldeepj345/PythonQuiz.git   #
###############################################################################

# 1. What is the output of the following code?
def mystery(n):
    if n <= 1:
        return n
    else:
        return mystery(n-1) + mystery(n-2)

result = mystery(4)
print(result)

#A. 3          #B. 4
#C. 5          #D. 8

# 2. What will be printed after running this code?
x = [1, 2, 3]
y = x
y.append(4)
print(x)

#A. [1, 2, 3]      #B. [1, 2, 3, 4]
#C. [4, 1, 2, 3]   #D. Error

# 3. What is the output of this code?
def weird_sum(a, b):
    try:
        return a + b
    except:
        return str(a) + str(b)

print(weird_sum('2', 3))

#A. 5          #B. 23
#C. '23'       #D. Error

# 4. What will this code print?
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1

c1 = Counter()
c2 = Counter()
c1.increment()
c2.increment()
c2.increment()
print(c1.count, c2.count)

#A. 1 1        #B. 1 2
#C. 2 2        #D. 3 3

# 5. What is the result of this code?
def multiply(x):
    return x * 2

numbers = [1, 2, 3, 4]
result = list(map(multiply, numbers))
print(result)

#A. [1, 2, 3, 4]           #B. [2, 4, 6, 8]
#C. [1, 4, 9, 16]          #D. None of the above

# 6. What will be the output of this code?
x = {1: 'a', 2: 'b', 3: 'c'}
y = {}
for k, v in x.items():
    y[v] = k
print(y)

#A. {1: 'a', 2: 'b', 3: 'c'}   #B. {'a': 1, 'b': 2, 'c': 3}
#C. {1: 1, 2: 2, 3: 3}         #D. Error

# 7. What does this code print?
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
    inner()
    return x

print(outer())

#A. 1          #B. 2
#C. None       #D. Error

# 8. What is the output of this code?
import re

text = "The price is $23.45"
pattern = r'\$\d+\.\d{2}'
result = re.findall(pattern, text)
print(result)

#A. ['$23.45']     #B. ['23.45']
#C. ['$23']        #D. []

# 9. What will this code print?
from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)
print(result)

#A. 15         #B. 120
#C. [120]      #D. Error

# 10. What is the output of this code?
class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 2

b = B()
print(hasattr(b, 'x'), hasattr(b, 'y'))

#A. True False     #B. False True
#C. True True      #D. False False

# Answers:
# 1. C (5)
# 2. B ([1, 2, 3, 4])
# 3. C ('23')
# 4. B (1 2)
# 5. B ([2, 4, 6, 8])
# 6. B ({'a': 1, 'b': 2, 'c': 3})
# 7. B (2)
# 8. A (['$23.45'])
# 9. B (120)
# 10. C (True True)