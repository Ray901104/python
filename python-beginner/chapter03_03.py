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
