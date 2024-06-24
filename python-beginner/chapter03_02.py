# Chapter03-02
# 문자형

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))
print()

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))
print()

# Escape 문자
print('I\'m Boy')
print('a \t b')
print('a \n b')
print('a \"\" b')
print()

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)
print()

# 탭, 줄바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"
print(t_s1)
print(t_s2)
print()

# Raw String
raw_s = r'D:\python\test'
print(raw_s)
print()

# 멀티 라인 입력
multi_str = \
"""
문자열
멀티 라인 입력
테스트
"""

print(multi_str)
print()

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('z' in str_o1)
print('P' not in str_o2)
print()

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))
print()

# 문자열 함수(upper, isalnum, startswith, count, endswith, isal, ...)
print("Capitalize: ", str_o1.capitalize())  # 첫 글자를 대문자로
print("endswith?: ", str_o2.endswith("e"))
print("replace", str_o1.replace("thon", "Good"))
print("sorted: ", sorted(str_o1))
print("split: ", str_o4.split(" "))
print()

# 반복(시퀀스)
im_str = "Good Boy!"
print(dir(im_str))

for i in im_str:
    print(i)

print()

# 슬라이싱
str_sl = "Nice Python"
print(str_sl[0:3])  # 0 ~ 2 까지
print(str_sl[5:11])
print(str_sl[5:])
print(str_sl[:len(str_sl)])
print(str_sl[1:9:2])
print(str_sl[-5:])
print(str_sl[1:-2])
print(str_sl[::2])
print(str_sl[::-1])
print()

# 아스키 코드
a = 'z'
print(ord(a))  # 문자 -> 아스키 코드
print(chr(122))  # 아스키 코드 -> 문자
