# tuple : 읽기 전용, 대신 list보다 읽는 속도가 빠르다!
menu = ("mia", "lena") # 괄호, 콤마
print(menu[0]) # 꺼내서 읽는건 동일하지만, add는 못함!
# menu[0] = 'aa' 이렇게도 불가능!

# 한줄에 여러 변수의 값 정의 가능
(name, age, hobby) = ("mia", 28, "coding") # 이 작업은 튜플이 아니라 변수의 재할당
print(name, age, hobby)
name = "lena"
print(name)
(departure, arrival) = ('김포', '제주')
print(departure, arrival)
(departure, arrival) = (arrival, departure) # 이 작업은 튜플의 언패킹을 이용해 변수의 값을 재할당(새로운 튜플을 생성해서 다시 변수에 대입한 것)
print(departure, arrival)

# 집합(set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set) # {1,2,3}

# set을 선언하는 방법
javascript = {'mia', 'lena', 'dinah'}
python = set(['mia', 'dido'])

# 교집합 ( & , .intersection )
print(javascript & python)
print(python.intersection(javascript))

# 합집합, 둘다 할수있는 ( |, .union) -> 근데 순서 보장 안됨 ~
print(javascript | python)
print(javascript.union(python))

# 차집합, javascript 할수있지만 python 할 줄 모르는 개발자 (-, .difference)
print(javascript - python)
print(javascript.difference(python))

# python 할줄 아는 사람이 늘어남! (.add)
python.add('luke')
print(python)

# javascript 까먹음 (.remove)
javascript.remove('dinah')
print(javascript)

# 자료구조의 변경 (list, set, tuple)
menu = {'coffee', 'milk', 'juice'} # set
print(menu, type(menu))

menu = list(menu) # list로 변환
print(menu, type(menu))

menu = tuple(menu) # tuple로 변환
print(menu, type(menu))

menu = set(menu)
print(type(menu))

# 문제 풀기
'''
댓글 작성자들 중에 추첨을 통해 1명 치킨, 3명은 커피 쿠폰 추첨 프로그램 작성

조건1. 20명이 작성, 아이디는 1-20
조건2. 무작위로 추첨, 중복 불가 (한명이 치킨 받았으면 커피는 못받음)
조건3. random 모듈의 shuffle, sample 활용
'''

from random import *
lst = []
print(lst)

for num in range(20):
 lst.append(num+1) 
print(lst)

## 나의 답 (반절만 맞음)
shuffle(lst) # 섞는 역할
print(lst)
chicken = sample(lst, 1)
print('치킨', chicken) # 치킨 1개
print('커피 쿠폰',sample(lst, 3)) # 치킨 1개

# 중복 방지를 위해 4명을 미리 뽑고 -> 1,3명을 주면 됨 ㅎㅎ
# 선생님의 답!
users = range(1,21) # 1~20까지 숫자 생성
users = list(users) # list형태로 바꿔야 random 내장함수 쓸수있음
print(users)

# shuffle
shuffle(users)

winners = sample(users, 4) # 4명 뽑음
print(winners)

print("-- 당첨자 발표 --")
print("-- 치킨 당첨자: {0}".format(winners[0]))
print("-- 커피 당첨자: {0}".format(winners[1:]))
print("-- 축하합니다 --")


# 또 다른 접근(차집합)
print(users)
chicken = sample(users, 1)
remain = set(users) - set(chicken)
print(list(remain))
coffee = sample(remain, 3)
print('chicken', chicken)
print('coffee', coffee)

# 셀프체크
'''
문제 : 수강신청중 일부 과목이 중복 신청되는 문제 발생. 중복 과목을 제거하는 프로그램 작성 

조건1 : 신청과목은 리스트로 관리된다
조건2 : 리스트에 같은 과목이 2번 이상 포함된 경우 1개만 남기고 나머지 삭제
조건3 : 출력시 신청 과목의 순서는 변경해도 괜찮다
'''

subjects = ['자료구조', '알고리즘', '자료구조', '운영체제']
subjects = set(subjects) # 중복 안되는 set으로 변경
print(subjects, type(subjects))

subjects = list(subjects)
print(subjects)
