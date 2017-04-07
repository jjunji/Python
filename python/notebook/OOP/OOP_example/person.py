# 공통 속성을 뽑아서 부모 클래스로 사용할 것.
class Person:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money
    
    def give_money(self, other, how_money):
        self.money -= how_money
        other.money += how_money
        
    def __str__(self):
        return '''
My name is {}
I am {} years old
I have {} won'''.format(self.name, self.age, self.money)
    
p1 = Person('greg', 18, 5000)
p2 = Person('kim', 22, 1000)
print(p1)
print(p2)
p1.give_money(p2, 2000)
print(p1)
print(p2)