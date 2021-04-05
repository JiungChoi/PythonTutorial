#리스트
numbers = [2, 3, 5, 7, 11, 13]
names = ["윤수", "혜린", "태호", "영훈"]

#인덱싱 (indexing)
print(names[1] + names[0])
print(names[-1] + names[-4])

print(numbers[0:4])
print(numbers[2:4] + numbers[0:2])

#리스트 함수 (list function) : append(), len(), del @[], insert(a, b)
print(numbers)
numbers.append(5)
print(numbers)

print(len(numbers))

del numbers[4]
print(numbers)

numbers.insert(4, 37)
print(numbers)

#리스트 정렬 : sorted(), sort()
new_list = sorted(numbers, reverse = True) #sorted는 return은 받지만 리스트 자체의 변환은 없다.
print(new_list)
print(numbers)

new_list = numbers.sort
print(new_list) 
numbers.sort()     #sort는 return 값이 없고 리스트 자체를 변환시킨다.
print(numbers)    

