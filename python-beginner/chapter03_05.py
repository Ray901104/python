# Chapter03-05
# dictionary
# 가장 많이 사용
# 순서 x, 키 중복 x, 수정 o, 삭제 o

# 선언
a = {'name': 'Kim', 'phone': '010-3333-7777', 'birth': '870514'}
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': True
}
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True),
])  # 잘 사용 하지 않는다.

f = dict(
    Name='Niceman',
    City='Seoul',
    Age=33,
    Grade='A',
    Status=True
)

# 출력
print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

print('a - ', a['name'])
print('a - ', a.get('name'))
# print('a - ', a['name1'])  # 키가 존재하지 않으면 에러 발생
print('a - ', a.get('name1'))  # 키가 존재하지 않으면 None 처리 -> get 함수 사용 권장
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))
print()

# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)
print()

# 길이
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))
print()

# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능
print(a.keys())
print(b.keys())
print(c.keys())
print(d.keys())

print('a - ', list(a.keys()))
print('b - ', list(b.keys()))
print()

print(a.values())
print(b.values())
print(c.values())
print('a - ', list(a.values()))
print('b - ', list(b.values()))
print()

print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())
print('a - ', list(a.items()))
print('b - ', list(b.items()))
print()

print('a - ', a.pop('name'))
print('a - ', a)
print('c - ', c.pop('arr'))
print('c - ', c)
print()

print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print()

print('a - ', 'birth' in a)
print('d - ', 'City' in d)
print()

# 수정
a['test'] = 'test_dict'
print('a - ', a)
a['address'] = 'daejeon'
print('a - ', a)

a.update(birth='910904')
print('a - ', a)

temp = {'address': 'Busan'}
a.update(temp)
print('a - ', a)
