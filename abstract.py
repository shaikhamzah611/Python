from abc import ABC,abstractmethod
class  absclass(ABC):
    def print(self,x):
        print("The passed value:",x)
    
    @abstractmethod
    def task(self):
        print("We are inside  absclass task")
    
class test(absclass):
    def task(self):
        print("We are in a test class task")
obj = test()
obj.task()
obj.print(100)