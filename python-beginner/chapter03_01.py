# Chapter03-01
# 숫자형

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집함
dict : 사전
"""

# 데이터 타입
str1 = "Python"
bool1 = True
str2 = 'Anaconda'
float1 = 10.0  # 10 != 10.0
int1 = 7
list1 = [str1, str2]
dict1 = {
    "name": "Machine Learning",
    "version": 2.0
}
tuple1 = (7, 8, 9)
set1 = {3, 5, 7}

# 데이터 타입 출력
print(type(str1))
print(type(bool1))
print(type(str2))
print(type(float1))
print(type(int1))
print(type(list1))
print(type(dict1))
print(type(tuple1))
print(type(set1))
print()

# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) : x의 y제곱
x ** y : x의 y제곱
"""

# 정수 선언
i = 77
i2 = -14
big_int = 7777777777777777777777777779999999999999

# 정수 출력
print(i)
print(i2)
print(big_int)
print()

# 실수 선언
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

# 실수 출력
print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산
i1 = 39
i2 = 939
big_int1 = 7777777777777777777777777777777779999999999999323434
big_int2 = 3432383482378429398238492384928349124981289419824819
f1 = 1.234
f2 = 3.939

print(">>>>>+")
print("i1 + i2 = ", i1 + i2)
print("f1 + f2 = ", f1 + f2)
print("big_int1 + big_int2 = ", big_int1 + big_int2)

print(">>>>>*")
print("i1 * i2 = ", i1 * i2)
print("f1 * f2 = ", f1 * f2)
print("big_int1 * big_int2 = ", big_int1 * big_int2)
