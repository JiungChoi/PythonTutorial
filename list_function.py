#sort
numbers = [5, 3, 7, 1]
numbers.sort()
print(numbers)
# >> [1, 3, 5, 7]

#reverse
numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)
# >> [1, 7, 3, 5]

#index
members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))
print(members.index("태호"))
# >> 1 \n 2

#remove
fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론"]
fruits.remove("파인애플")
print(fruits)
# >> ['딸기', '당근', '수박', '참외', '메론']

#리스트 서치 1
def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        if some_list[i] == value:
            return True
        i = i + 1
    return False

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))
print(in_list(primes, 12))
# >> True \n False

# 리스트 서치 2
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)
print(12 in primes)
print(7 not in primes)
print(12 not in primes)
# >> True \n False \n False \n True