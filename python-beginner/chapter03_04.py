# Chapter03-04
# 튜플
# 리스트와 비교
# 순서 o, 중복 o, 수정 x, 삭제 x -> 불변(immutable)

# 선언
a = ()
b = (1,)  # 원소가 하나인 경우 콤마를 찍지 않으면 int
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Cap')
e = (100, 1000, ('Ace', 'Base', 'Cap'))

# 인덱싱
print(">>>>>")
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))  # list 형변환 -> tuple의 불변성 사라진다.
print()

# 수정 x
# d[0] = 1500

# 슬라이싱
print(">>>>>")
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])
print()

# 튜플 연산
print(">>>>>")
print('c + d', c + d)
print('c * 3', c * 3)
print()

# 튜플 함수
print(">>>>>")
f = (5, 2, 3, 1, 4)
print('f - ', f)
print('f - ', f.index(3))
print('f - ', f.count(2))
print()

# Packing
print(">>>>>")
t = ('foo', 'bar', 'baz', 'qux')
print(t)
print(t[0])
print(t[-1])
print()

# Unpacking 1
(x1, x2, x3, x4) = t
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)
print()

# Packing & Unpacking
t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6
print(type(t2), t2)
print(type(t3), t3)
print(x1, x2, x3)
print(x4, x5, x6)
