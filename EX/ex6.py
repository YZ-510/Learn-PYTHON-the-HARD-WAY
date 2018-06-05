x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"

# 如果在字符串中通过格式化字符放入多个变量，需要将变量放到（）中，变量之间用逗号隔开
y = "Those who know %s and those who is %s." % (binary, do_not)

print(x)
print(y)

print("I said: %r." % x)        # %r 的含义是：不管什么都打印出来
print("I also said: '%s'." %y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)