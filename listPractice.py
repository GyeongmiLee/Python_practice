# list []
broj = ['mia', 'lena', 'dinah']
print(broj)
print(broj.index('mia'))

#append: list에 추가
broj.append('luke')
print(broj)

# list 중간에 넣고싶다면? 첫번째 파라미터는 넣고싶은 index
#  mia 뒤에 넣고싶다?
broj.insert(1, 'dido')
print(broj)

# 한명씩 뒤에서 꺼냄
print(broj.pop()) # 이렇게 하면 어떤 list 구성원을 꺼냈는지 알수있구~
print(broj) # 실제로 list 조회해보면 빠져나감을 알수있다!

# 같은 이름의 사람이 몇명 있는지 확인 count()
broj.append("mia")
broj.insert(2, "mia2")
print(broj.count("mia"))

# 정렬
numList = [4,3,6,1,2]
numList.sort() # 얘는 오름차순
numList.reverse() # 얘는 내림차순

# 모두지우기
numList.clear() 
print(numList)

# 리스트 정렬하면서 복사해서 새로운 리스트 생성
newList = ['가','다',str(1)]
print(newList)
sortedList = sorted(newList, reverse=True)
print(sortedList)

# 리스트 확장하기 extend()
aList = ['가', '나', '다']
bList = [1,2,3]
aList.extend(bList) # aList에 bList가 들어가는 형태임!
print(aList)
print(bList) # bList는 원본 배열 그대로임!

