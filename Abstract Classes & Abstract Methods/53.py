from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def method(self):
        pass

class Child(Base):
    def method(self):
        print("Implementation for Q53")

if __name__ == "__main__":
    obj = Child()
    obj.method()
