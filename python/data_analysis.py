
# coding: utf-8

# In[52]:

# 절차지향 프로그램 예시

from functools import reduce
import math # sqrt
import pickle

# 평균, 분산 함수 만들기

def average(scores):  # score = [95, 23, 46, 25] / reduce로
    return reduce(lambda a,b: a + b, scores) / len(scores)

def variance(scores, arvg):  # scores = [95, 23, 25, 62] avrg : 50
    return reduce(lambda a,b: a +b, map(lambda s: (s-arvg)**2, scores)) / len(scores) # sum(각 점수 - 평균)**2 / 데이터의 개수

def evaluateClass(avrg, std_dev):
    if avrg <50 and std_dev >20:
        print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
    elif avrg > 50 and std_dev >20:
        print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
    elif avrg < 50 and std_dev <20:
        print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
    elif avrg > 50 and std_dev <20:
        print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")
        


# In[53]:

f = open("class_A.bin", "rb") #rb : read binary


# In[54]:

items = []

while 1:
    try:
        data = pickle.load(f)
    except EOFError:
        break
    items.append(data)

print(items)


# In[55]:

# data handling

scores = []

for item in items:
    for value in item.values():
        scores.append(value)

f.close()  # 닫는 시점 : 
print(scores)


# In[56]:

avrg = average(scores)
avrg


# In[57]:

vari = round(variance(scores, avrg), 1)
vari


# In[58]:

std_dev = round(math.sqrt(vari),1)
std_dev


# In[60]:

print("\n")

print('*' * 50)
print("A반 성적 분석 결과")
print('*' * 50)
print("A반의 평균은 {0}점이고 분산은 {1}이며, 따라서 표준편차는 {2}이다".format(avrg, vari, std_dev))
print('*' * 50)
print("A반 종합 평가")
print('*' * 50)

print('\n')
evaluateClass(avrg, std_dev)

# f.close()  -> 위로 올리자 (왜냐하면 메모리를 많이 잡아먹기때문에? 파일이 끝나면 닫아주는 것이 좋음 -> 다시 듣기)


# In[17]:

# 위에서 items에 할당된 key값을 빼고 value 값만을 빼오기 위한 과정을 이해하기 위한 예)

dic = dict(one = 1, two =2, three =3)


# In[18]:

dic


# In[19]:

dic.values()


# In[20]:

for value in dic.values():
    print(value)


# In[23]:

dic = dict(one = 1, two = 2, three =3)
dic


# In[24]:

for one in dic.items():
    print(one)                  # 튜플로 받는다.


# In[27]:

for key, value in dic.items():
    print(one)


# In[47]:

a = 12
b = "abc"
print("{}는 재밌어, {}는 싫어".format(a, b))
age = 10
name = "greg"
print("내 이름은 {n}이고, 나이는 {a}인데 그 나이 {a}는 사실 거짓말이야.".format(n = name, a = age))
print(age, end = '   ')
print(name)
print(age, name)


# In[ ]:



