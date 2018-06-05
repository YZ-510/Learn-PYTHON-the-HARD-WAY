ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()             # pop() 默认 index = -1，删除最后一个列表值
    print("Adding:", next_one)
    stuff.append(next_one)
    print("There's %d items now." % len(stuff))
    
print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())                          # pop() 返回从列表中删除的元素                        
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
