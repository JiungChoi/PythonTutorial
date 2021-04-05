##실습 1. greetings 리스트의 원소를 모두 출력하는 프로그램을 작성해 보세요. while문과 리스트의 개념을 활용하시면 됩니다.##

greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]

i = 0
while i < len(greetings):
    print(greetings[i])
    i += 1


##실습2. 화씨 온도를 섭씨 온도로 변환해 주는 함수 fahrenheit_to_celsius를 써 보세요. 이 함수를 파라미터로 화씨 온도 fahrenheit를 받고, 변환된 섭씨 온도를 리턴합니다.##

# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    return round(((fahrenheit - 32) * 5 / 9), 1) #소수점 한 자리에서 반 올림

temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

j = 0
while j < len(temperature_list):
    temperature_list[j] = fahrenheit_to_celsius(temperature_list[j])
    j += 1
print("섭씨 온도 리스트: " + str(temperature_list))  # 섭씨 온도 출력


##실습3. 원화를 달러와 엔화로 변환시켜주는 코드를 구하세요.##

def krw_to_usd(krw):
    return round(krw / 1000, 1)
    

def usd_to_jpy(usd):
    return round(usd*1000 / 8, 1)
    

prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))
 

count_money = 0
while count_money < len(prices):
    prices[count_money] = krw_to_usd(prices[count_money])
    count_money += 1
    

print("미국 화폐: " + str(prices))


count_money = 0
while count_money < len(prices):
    prices[count_money] = usd_to_jpy(prices[count_money])
    count_money += 1

print("일본 화폐: " + str(prices))

#실습4. numbers라는 빈 리스트를 만들고 리스트를 출력한다.
        #append를 이용해서 numbers에 1, 7, 3, 6, 5, 2, 13, 14를 순서대로 추가한다. 그 후 리스트를 출력한다.
        #numbers 리스트의 원소들 중 홀수는 모두 제거한다. 그 후 다시 리스트를 출력한다.
        #numbers 리스트의 인덱스 0 자리에 20이라는 수를 삽입한 후 출력한다.
        #numbers 리스트를 정렬한 후 출력한다.

numbers = []
print(numbers)

numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)

count_numbers = len(numbers) - 1
while count_numbers >= 0 :
    if numbers[count_numbers] % 2 == 1:
        del numbers[count_numbers]
    count_numbers -= 1
print(numbers)

numbers.insert(0,20)
print(numbers)

print(sorted(numbers))