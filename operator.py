# 산술연산자
# + , - , *, / 

print(1+1)
print(3-2)
print(5*2)
print(6/3) # 대신 이건 2.0으로 실수!

print(2**3) # 거듭제곱 8
print(5%3)  # 나머지 즉 2
print(10%3) # 1
print(5//3) # 몫 즉 1
print(10//3) # 3

# 비교연산자
print(10 > 3) # true
print(4 >= 7) # false
print(10 < 3) # false
print(5 <= 5) #true

print(5 == 7) # false 앞 뒤가 같은지 비교
print(7 != 5) # true 앞 뒤가 다른지 비교

# 논리연산자
print(not(1 != 3)) # false
print((3 > 0) and (3 < 5)) # true (둘 다 true여야 true)
print((3 > 0) & (3 < 5)) # true (and == &)

print((3 > 0) or (3 > 5)) # true (둘 중 하나만 참이어도 true)
print((3 > 0) | (3 > 5)) # true (or == |)

# 단축 평가
print(5 > 4 > 3) # true
print(5 < 6 < 3) # false(이를 단축평가로 표현함, 앞만 봐도 이미 false)

# 문제
print(5 + 3) # 8
print(6 / 3) # 2.0
print(5 % 3) # 2
print(5 < 3 | 7 < 3) # false  

# 연산자의 우선순위
num = 2 + 3 * 4 # 14
num = num + 2 
num += 2 # 위와 동일!
print(num) # 18
num *= 2 # 36
print(num)
num /= 2 # 18.0
print(num)
num -= 2
print(num) # 16.0
num %= 5 # 1.0
print(num)

# 함수로 연산하기
print(abs(-5)) # 절대값 5
print(pow(4, 2)) # 4^2 = 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) # 3
print(round(4.132, 2)) # 소수점 두번쨰 자리 이하에서(세번째 자리) 반올림, 4.13

# math 모듈
from math import * # math 모듈에 있는걸 다 가져오겠다~
floorNum = floor(4.99) 
print(floorNum) # 내림, 4
ceilNum = ceil(3.14)
print(ceilNum) # 올림, 4
sqrtNum = sqrt(16)
print(sqrtNum) # 제곱근, 4

# 모듈은 이렇게 가져와서 써도된다
import math

result = math.floor(4.56) 
print(result) # 4
result = math.ceil(5.44)
print(result) # 5
result = math.sqrt(36)
print(result) # 6.0

# random 모듈
from random import *
print(random()) # 0.0 이상 ~ 1.0 미만 임의의 값 생성 
print(random() * 10) # 0.0 이상 ~ 10.0 미만 임의의 값 생성 
print(int(random() * 45 + 1)) # 1 이상 46 미만 정수난수 뽑고 싶다면?

# 주어진 범위 안에서 정수인 난수 생성(끝 숫자 미포함)
print(randrange(1,46)) # 1 이상 46 미만
print(randint(1,45)) # 1 이상 45 이하

# 문제 풀이
print(round(0.1357, 2)) # 0.14

# 스터디 날짜 정하기
'''
1. 날짜를 무작위로 뽑는다.
2. 28일까지만 날짜 선정
3. 매월 1~3일은 스터디 준비하니까 제외
4. 형태는 "오프라인 스터디 모임 날짜는 매월 18일로 선정됐습니다"
'''
from random import *
result = randint(4,28) # 4일부터 28일이하
print(f'오프라인 스터디 모임 날짜는 매월 {result}일로 선정됐습니다')

# 온도 단위를 변환하는 프로그램 만들기
'''
1. 온도 저장 변수 만들기
2. 화씨온도 변환하고 새로운 변수저장
3. 출력
'''
temp = 30
hwatemp = (temp * 9 / 5) + 32
print('섭씨온도 :'+str(temp))
print('화씨온도 :'+str(hwatemp))

temp = 10
hwatemp = (temp * 9 / 5) + 32
print('섭씨온도 :'+str(temp))
print('화씨온도 :'+str(hwatemp))