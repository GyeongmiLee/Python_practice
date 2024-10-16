# 문자열(string), '' , ""
sentence3 = """
나는 미아고,
파이썬은 쉬워요

"""
print(sentence3)

# type 판단하기
photo = '사진'
print(type(photo))

# slicing
mia = "971023-2323232"
print("성별 식별번호:" + mia[7])
print("년도 :" + mia[0:2]) # 0부터 2직전까지
print("월 :" + mia[2:4]) # 2부터 4직전까지
print("일 :" + mia[4:6]) # 4부터 6직전까지
print("생년월일 :" + mia[0:6]) # 0부터 6직전까지
print("주민등록번호 뒷자리 :" + mia[7:]) # 7부터 끝까지
print("주민등록번호 뒷자리 :" + mia[-7:]) # 뒤에서 일곱번쨰부터 

# 문제
msg = '나도코딩'
print(msg[1]) # 도

print(msg[0:1]) # 나
print(msg[:2]) # 나도
print(msg[1]+ msg[2]) # 도코
print(msg[-2:]) # 코딩

fruit = 'apple'
print(fruit[:]) # apple
print(fruit[0:]) # apple
print(fruit[:5]) # apple
print(fruit[:-1]) # 처음부터 -1 직전까지 appl

# 함수로 문자열 처리하기, 

# 4.4 문자열 포맷팅
'''
- $d 정수
- $f 실수
- $c 문자(한 문자)
- $s 문자열 '''
print("나는 %d살입니다" % 20)
print("나는 %s을 좋아합니다" % "파이썬")
print("나는 %s을 좋아합니다" % 20)
print("나는 %s을(를) %s보다 더 좋아합니다" % ("리나", "다이나"))

# format 함수 사용하기
print("나는 {}살입니다" .format(20))

# 4.5 탈출 문자
# \n 
print("나는 지금 피곤해. \n자고싶어")

# \" , \' 문자열 안에서도 따옴표 사용하기
# \\ 문자열 안에서 역슬래시 사용하기

# 덮어쓰는 효과 \r
print("Red Apple\rPine")

# \b 앞글자 하나 삭제
print("Red\bApple")

# \t tab
print("hi my name is \t mia")

# 비밀번호 만들기
naverPw = 'http://naver.com'
daumPw = 'http://daum.com'
googlePw = 'http://google.com'
youtubePw = 'http://youtube.com'

# http:// 제외하기
naverPw = naverPw.replace("http://", "")
daumPw = daumPw.replace("http://", "")
googlePw = googlePw.replace("http://", "")
youtubePw = youtubePw.replace("http://", "")
print(naverPw)
# .이후 제외
naverPw = naverPw[:naverPw.index(".")]
naverPw = naverPw[:-4]
daumPw = daumPw[:-4]
googlePw = googlePw[:-4]
youtubePw = youtubePw[:-4]
print(naverPw)
# 처음 세자리, 글자개수, e의 개수, !
result1 = naverPw[:3] + str(len(naverPw)) + str(naverPw.count("e")) + "!"
result2 = daumPw[:3] + str(len(daumPw)) + str(daumPw.count("e")) + "!"
result3 = googlePw[:3] + str(len(googlePw)) + str(googlePw.count("e")) + "!"
result4 = youtubePw[:3] + str(len(youtubePw)) + str(youtubePw.count("e")) + "!"
print(f"{result1}{result2}{result3}{result4}")

# 첫번째 글자는 대문자로, 나머지 글자는 모두 소문자로 변환
first = "the early bird catches the worm."
firstChar = first[0].upper()
lastSetence = first[1:].lower()
print(firstChar+lastSetence)
# capitalize() 써도 된다
print(first.capitalize())