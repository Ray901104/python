# Chapter03-03
# 리스트
# 순서 o, 중복 o, 수정 o, 삭제 o

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, "Ace", "Base", "Cap"]
e = [1000, 10000, ["Ace", "Base", "Cap"]]
f = [21.42, "foobar", 3, 4, False, 3.14159]

# 인덱싱
print(">>>>>")
print("d - ", type(d), d)
print("d - ", d[1])
print("d - ", d[0] + d[1] + d[1])
print("d - ", d[-1])
print("e - ", e[-1][1])
print("e - ", list(e[-1][1]))
print()

# 슬라이싱
print(">>>>>")
print("d - ", d[0:3])
print("d - ", d[2:])
print("e - ", e[-1][1:3])
print()

# 연산
print(">>>>>")
print("c + d", c + d)
print("c * 3", c * 3)
print("'Test' + c[0]", "Test" + str(c[0]))
print()

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

# Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정
print(">>>>>")
c[0] = 4
print("c - ", c)
c[1:2] = ['a', 'b', 'c']  # 슬라이싱 -> 리스트로 들어감
c[1] = ['a', 'b', 'c']  # 원소로 들어감
print("c - ", c)
print()

# 리스트 삭제
c[1:3] = []
print("c - ", c)
del c[2]
print("c - ", c)
print()

# 리스트 함수
a = [5, 2, 3, 1, 4]
print('a - ', a)
a.append(10)  # 마지막에 삽입
print('a - ', a)
a.sort()  # 오름차순 정렬
print('a - ', a)
a.reverse()  # 반대로 정렬
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2, 7)  # 중간 삽입
print('a - ', a)
a.reverse()
print('a - ', a)
a.remove(10)  # 해당 값 삭제
print('a - ', a)
print('a - ', a.pop())  # 마지막 원소 삭제
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4))
ex = [8, 9]
a.extend(ex)  # 마지막에 ex 리스트를 붙임
print('a - ', a)

# 반복문 활용
while a:
    data = a.pop()
    print(data)
print('a - ', a)
