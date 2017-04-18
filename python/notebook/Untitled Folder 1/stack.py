class Stack(list):
    push = list.append
    
    def is_empty(self):
        if not len(self): # 리스트를 상속받았기 때문에 가능.
            return True
        else:
            return False
    
    def peek(self):
        return self[-1]  # ㅇㅇ  peek : 최상위 값만 확인.