#실습1. 값 출력하기
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

j = 0
for i in numbers:
    print("{} {}".format(j, i))
    j += 1

#실습2. 2의 거듭제곱 만들기
for i in range(0, 11):
    print("2^{} = {}".format(i, 2 ** i))

#실습3. 구구단 만들기
for i in range(1, 10):
    for j in range(1, 10):
        print("{} * {} = {}".format(i, j, i * j))

#실습4. 피타고라스 삼조
result = 0
for a in range(1, 1000):
    for b in range(a, int((1000-a) / 2)):
        c = 1000 - (a+b)
        if ((a**2 + b**2) == c**2):
            print(f"{a} {b} {c}")
            result = a * b * c
print(result)

#실습5. 리스트 순서를 거꾸로 뒤집는 소스 만들기
numbers3 = [2, 3, 5, 7, 11, 13, 17, 19]
numbers3_r = []

for i in numbers3:
    numbers3_r.insert(0,i)
print(numbers3_r)

numbers3 = numbers3_r

print("뒤집어진 리스트: " + str(numbers3))