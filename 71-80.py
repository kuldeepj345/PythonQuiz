###############################################################################
#                             YouTube: @KuldeepJangidd                        #
###############################################################################
#                             🎉 Easy Python Quiz 🎉                          #
###############################################################################
#                 GitHub Repo: https://github.com/kuldeepj345/PythonQuiz.git   #
###############################################################################

# 71. What is the output of this code?
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers if x % 2 == 0]
print(squared)

#A. [4, 16]    #B. [1, 4, 9, 16, 25]
#C. [2, 4]     #D. [4, 16, 36]

# 2. What will this code print?
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))

#A. Hello, Alice!
#   Hi, Bob!
#B. Hello, Alice!
#   Hello, Bob!
#C. Error
#D. Alice!
#   Bob!


# 73. What is the result of this code?
text = "python"
result = text[1:4:2]
print(result)

#A. "yt"       #B. "yh"
#C. "pt"       #D. "yo"

# 74. What does this code print?
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
print(closure(5))

#A. 15         #B. 10
#C. 5          #D. Error

# 75. What is the output of this code?
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

animal = Animal()
dog = Dog()
animal.speak()
dog.speak()

#A. Animal speaks
#   Dog barks
#B. Animal speaks
#   Animal speaks
#C. Dog barks
#   Dog barks
#D. Error

# 76. What will be printed after running this code?
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(len(unique_numbers))

#A. 7          #B. 5
#C. 4          #D. Error

# 77. What does this code print?
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(f"Result is {result}")
    finally:
        print("Division attempted")

divide(10, 2)
divide(10, 0)

#A. Result is 5.0
#   Division attempted
#   Cannot divide by zero
#   Division attempted
#B. Result is 5.0
#   Division attempted
#   Error
#C. Result is 5.0
#   Cannot divide by zero
#   Division attempted
#D. Result is 5.0
#   Division attempted
   

# 78. What is the result of this code?
import re

text = "The price is $23.45"
pattern = r'\$\d+\.\d{2}'
result = re.search(pattern, text)
print(result.group())

#A. $23.45     #B. 23.45
#C. $23        #D. Error

# 79. What will this code print?
from collections import Counter

words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'date']
word_counts = Counter(words)
print(word_counts.most_common(2))

#A. [('apple', 2), ('banana', 2)]
#B. ['apple', 'banana']
#C. {'apple': 2, 'banana': 2}
#D. Error

# 80. What is the output of this code?
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)

#A. [2, 4, 6, 8, 10]    #B. [4, 8]
#C. [2, 6, 10]          #D. [4]

# Answers:
# 71. A ([4, 16])
# 72. A (Hello, Alice!
#       Hi, Bob!)
# 73. B ("yh")
# 74. A (15)
# 75. A (Animal speaks
#       Dog barks)
# 76. B (5)
# 77. A (Result is 5.0
#       Division attempted
#       Cannot divide by zero
#       Division attempted)
# 78. A ($23.45)
# 79. A ([('apple', 2), ('banana', 2)])
# 80. B ([4, 8])