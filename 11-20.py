###############################################################################
#                             YouTube: @KuldeepJangidd                        #
###############################################################################
#                             🎉 Easy Python Quiz 🎉                          #
###############################################################################
#                 GitHub Repo: https://github.com/kuldeepj345/PythonQuiz.git   #
###############################################################################

# 11. What is the output of this code?
def decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@decorator
def say_hello():
    print("Hello")

say_hello()

#A. Start Hello End    #B. Hello
#C. Start End          #D. Error

# 12. What will this code print?
x = [1, 2, 3]
y = x[::-1]
x[1] = 4
print(y)

#A. [1, 2, 3]      #B. [3, 2, 1]
#C. [3, 4, 1]      #D. [1, 4, 3]

# 13. What is the result of this code?
import itertools

numbers = [1, 2, 3]
result = list(itertools.permutations(numbers))
print(len(result))

#A. 3          #B. 6
#C. 9          #D. 27

# 14. What does this code print?
class A:
    x = 1

class B(A):
    pass

class C(A):
    x = 2

print(B.x, C.x)

#A. 1 1        #B. 1 2
#C. 2 2        #D. Error

# 15. What is the output of this code?
def generate():
    yield 1
    yield 2
    yield 3

g = generate()
print(next(g) + next(g))

#A. 1          #B. 3
#C. 6          #D. Error

# 16. What will be printed after running this code?
import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][1] = 'X'
print(shallow[0][1], deep[0][1])

#A. X 2        #B. 2 2
#C. X X        #D. 2 X

# 17. What does this code print?
from collections import Counter

text = "hello world"
result = Counter(text)
print(result.most_common(1)[0][1])

#A. 'l'        #B. 3
#C. ('l', 3)   #D. 'o'

# 18. What is the result of this code?
numbers = [1, 2, 3, 4, 5]
result = [x if x % 2 == 0 else 'odd' for x in numbers]
print(result)

#A. [1, 2, 3, 4, 5]               #B. ['odd', 2, 'odd', 4, 'odd']
#C. [False, True, False, True, False]  #D. [2, 4]

# 19. What will this code print?
def func(a, b, c=3, d=4):
    print(a, b, c, d)

func(1, *(5, 6))

#A. 1 5 6 4    #B. 1 5 3 4
#C. 1 5 6 3    #D. Error

# 20. What is the output of this code?
class MyContext:
    def __enter__(self):
        print("Entering")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")
    def hello(self):
        print("Hello")

with MyContext() as mc:
    mc.hello()

#A. Entering Hello     #B. Entering Hello Exiting
#C. Hello Exiting      #D. Entering Exiting


# Answers:
# 11. A (Start Hello End)
# 12. B ([3, 2, 1])
# 13. B (6)
# 14. B (1 2)
# 15. B (3)
# 16. A (X 2)
# 17. B (3)
# 18. B (['odd', 2, 'odd', 4, 'odd'])
# 19. A (1 5 6 4)
# 20. B (Entering Hello Exiting)