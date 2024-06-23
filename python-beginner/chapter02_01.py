# Chapter02_01
# 파이썬 완전 기초
# Print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

# 기본 출력
print('Python Start!')  # 가장 많이 사용
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

print()

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='|')
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

# file 옵션
import sys

print('Learn Python', file=sys.stdout)

print()

# format 사용(d : 정수, s : 문자열, f : 실수)
print('%s %s' % ('one', 'two',))
print('{} {}'.format('one', 2))
print('{1} {0}'.format('one', 'two'))

print()

# %s
print('%10s' % 'nice')
print('{:>10}'.format('nice'))

print('%-10s' % 'nice')
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))  # 중앙 정렬

print('%.5s' % 'nice')
print('%.5s' % 'pythonstudy')  # 절삭
print('{:10.5}'.format('pythonstudy'))

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % 42)
print('{:4d}'.format(42))

print()

# %f
print('%f' % 3.143434343434)
print('{:f}'.format(3.143434343434))

print('%06.2f' % 3.141592653589793)
print('{:06.2f}'.format(3.141592653589793))
