# 자료형 : number, string, boolean

# number
age = 23
print(age)

# string
name = '미아'
print(name)

# number + string
# f를 사용할 떄
print(f'{name}의 나이는 {age}야')
# +를 사용할 때(boolean, number는 둘다 str을 붙여야한다~!)
print(name+ '의 나이는' + str(age) + '야')
# ,를 사용할 때 (무조건 띄어쓰기를 포함한다)
print(name,'의 나이는',age,'야')

# boolean
is_adult = age > 20
print(f'{name}은 아무래도 어른일까요? -> {is_adult}')

# 형변환하기
# str()처럼 int(): 정수형태로 형변환, float(): 실수형태로 형변환

# 다음은 모두 3으로 출력됨 -> 오로지 숫자로 된 문자열만 출력 가능!
print(int("3"))
print(int(3.5))
# 다음은 소수점이 들어간 실수로 출력됨
print(float("3.5"))
print(float("3"))

# 주석 처리!
''' 작은 따옴표로 둘러싸면 한번에 주석처리'''

# 변수를 이용해서 다음 문장을 출력하시오
stations = ['사당', '신도림', '인천공항']
for station in stations:
    print(f'{station}행 열차가 들어오고 있습니다.')

# 자료형 확인할떄 type()
# 결과값은 <class 'int'> / <class 'str'> / <class 'float'> 이런식으로 출력됨
print(type(3))
