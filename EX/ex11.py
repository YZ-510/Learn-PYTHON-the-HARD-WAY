print("How old are you?", end='')
age = input()           # Python 3.0 版本后用 input 替换了 raw_input
print("How tall are you?", end='')
height = input()
print("How much do you weigh?", end='')
weight = input()

print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))