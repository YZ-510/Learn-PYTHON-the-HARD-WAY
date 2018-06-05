# 使用反斜杠（\）可以将难打印出来的字符放到字符串
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# 可以在一组三引号之间放入任意多行的文字
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print("%s\r" % i)