# 显式覆盖
class Parent:
    
    def override(self):
        print("Parent override()")
        
class Child(Parent):
    
    def override(self):
        print("Child override")
        
dad = Parent()
son = Child()

dad.override()
son.override()
