# dictionary - key, value 한쌍으로 이뤄져 있음! (키는 중복 허용 안함)
cabinet = {
    1 : "mia",
    3 : "lena"
}
print(cabinet)

# 값을 가져오는 방법1 - key값으로
print(cabinet[1])

# 값을 가져오는 방법2 - get()
print(cabinet.get(3))

'''
참고용으로 알아두자!
- 만약 없는 키값으로 print를 하려고 시도했을때 
key값으로, get()함수를 사용해서 가져왔을때 
함수는 반환값이 존재하지 않으므로 "None"을 도출하면서 만약 뒤의 코드가 존재해도 읽지만
없는 key값으로 조회하려고 하면 에러남! 뒤의 코드 읽지않음~!
'''

# 없는 키값 이용해서 활용해보자?
print(cabinet.get(5, "사용가능")) # 5번이 없다면 사용가능이라고 뜸

# 키값이 있는지 확인해보자?
print(3 in cabinet) # t / f 로 확인가능

# 새로운 key, value 넣고 싶다면?
cabinet[4] = 'dinah'
# 키를 재할당 한다면 대체됨~!
print(cabinet)

# dictionary 값을 지우고 싶다면?
del cabinet[4]
print(cabinet)

# key들만 출력? - keys()
print(cabinet.keys())

# values 출력? - values()
print(cabinet.values())

# key, value 쌍으로 출력? - items()
print(cabinet.items())

# 전체 dictionary 삭제? - clear()
cabinet.clear()
print(cabinet)