import datetime
#내 생일
pi_day = datetime.datetime(1999, 12, 2, 3, 6, 15)
print(pi_day)
print(type(pi_day))
#오늘의 날짜 알아보기
today = datetime.datetime.now()
print(today)
print(type(today))

## 두 날짜 사이의 차이 알아보기
print(today - pi_day)
print(type(today - pi_day)) ##data type 유의 >> datetime.dtimedelta

#날짜를 더해주기
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)

print(today)
print(today + my_timedelta)

#특정 '연도'나 '월' 같은 값들을 출력하기
print(today)  #오늘
print(today.year)  #연도
print(today.month)  #월
print(today.day)  #일
print(today.hour)  #시
print(today.minute) #분
print(today.second) #초
print(today.microsecond) #마이크로초

# strftime함수 사용해보기 
# datetime 포매팅

print(today.strftime("%A, %B %dth %Y"))