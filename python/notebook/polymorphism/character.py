
# coding: utf-8

# In[1]:

# 같은 코드 다른 결과 -> 폴리모르피즘?
# abstract_class : 객체를 만들 수 없는 클래스
# 기본 클래스, 부모 클래스의 역할.

from abc import * # abstract base class

class Character(metaclass = ABCMeta):
    def __init__(self):
        self.hp = 100
        self.attack_power = 20
       
    def attack(self, other, attack_kind):
        other.get_damage(self.attack_power, attack_kind)
        
    @abstractmethod # 객체를 만들 수 없는 클래스이므로, abstract메소드를 가져야 인스턴스 생성 가능? -> abstract메소드를 꼭 쓰게 할 때.
    def get_damage(self, attack_power, attack_kind):
        pass


# In[2]:

# 모듈을 불러올때는 py파일로 저장해야됨.


# In[ ]:



