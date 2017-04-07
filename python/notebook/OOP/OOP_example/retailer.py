from person import Person

# Retailer 클래스

class Retailer(Person):
    # 제품 가격 : 클래스 멤버
    price = 1000
    
    def __init__(self, name, age, money, product):
        super().__init__(name, age, money)
        self.product = product
        
    def sell(self, other, how_many):
        if self.product > how_many:
            self.product -= how_many
            other.product += how_many
            
            #total = Retailer.price + how_many  # 
            total = self.price * how_many # 객체로 접근.
            other.give_money(self, total) # 아래와 같이 바꿔써도됨.   
            #self.money += total
            #other.money -= tatal
            
        else:
            print("제품 물량이 부족합니다.")
    
    def __str__(self):
        return super().__str__() + '''
I am a retailer
I have {} products'''.format(self.product)
    
if __name__=="__main__":
    r1 = Retailer('yang', 20, 5000, 20)
    p1 = Person('kim', 10, 10000)
    print(r1)
    print(p1)
    r1.sell(p1, 3)
    print(r1)
    print(p1)