# 三种方式组合使用
class Parent:
    
    def override(self):
        print("Parent override()")
        
    def implicit(self):
        print("Parent implicit()")
        
    def altered(self):
        print("Parent altered()")

class Child(Parent):
    
    def override(self):
        print("Child override()")
        
    def altered(self):
        print("Child, before Parent altered()")
        super(Child, self).altered()
        print("Child, After Parent altered()")
        
dad = Parent()
son = Child()

dad.implicit()
son.implicit()          # 隐式继承

dad.override()
son.override()          # 显示覆盖

dad.altered()
son.altered()           # 运行后替换
