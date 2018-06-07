# 合成
class Other:
    
    def override(self):
        print("Other override()")
        
    def implicit(self):
        print("Other implicit()")
        
    def altered(self):
        print("Other altered()")
    
class Child:
    
    def __init__(self):
        self.other = Other()        # 调用 Other 类
    
    def implicit(self):
        self.other.implicit()
        
    def override(self):
        print("Child override()")
        
    def altered(self):
        print("Child, before Other altered()")
        self.other.altered()
        print("Child, after Other altered()")
        
son = Child()

son.implicit()
son.override()
son.altered()
