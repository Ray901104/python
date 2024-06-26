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
