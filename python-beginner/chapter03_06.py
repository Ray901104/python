# Chapter03-06
# 집합(Set)
# 순서 x, 중복 x, 수정 o, 삭제 o

# 선언
a = set()
b = set([1, 2, 3, 4, 4, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}  # key 없이 중괄호를 사용하면 Set 자료형
f = {42, 'foo', (1, 2, 3), 3.14159}

# 출력
print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

# 튜플 변환
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])
print()

# 리스트 변환
l = list(c)
l2 = list(e)
print('l - ', type(l), l)
print('l2 - ', type(l2), l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
s3 = set([1, 2, 3])
print('s1 & s2', s1 & s2)  # 교집합
print('s1.intersection(s2)', s1.intersection(s2))  # 교집합
print('s1 | s2', s1 | s2)  # 합집합
print('s1.union(s2)', s1.union(s2))  # 합집합
print('s1 - s2', s1 - s2)  # 차집합
print('s1.difference(s2)', s1.difference(s2))  # 차집합
print()

# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2))  # 교집합이 있으면 False
print()

# 부분 집합 확인
print('subset : ', s1.issubset(s2))
print('subset : ', s2.issubset(s1))
print('subset : ', s3.issubset(s1))
print('superset : ', s1.issuperset(s3))
print()

# 추가 & 제거
s1 = set([1, 2, 3, 4])

s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)

s1.discard(3)
print('s1 - ', s1)
s1.discard(7)  # 없는 값을 넣어도 예외 발생 x

s1.clear()
print('s1 - ', s1)  # 전부 삭제
