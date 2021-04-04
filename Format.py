year = 2021
month = 4
day = 4

# .format
#print("오늘은" + str(year) + "년 "+ str(month) + "월" + str(day) + "일입니다.")
#print("오늘은 {}년 {}월 {}일 입니다.". format(year, month, day ))

data_string = "오늘은 {0}년 {1}월 {2}일 입니다."
print(data_string. format(year, month, day ))

print("{}나누기 {}는 {:.2f} 입니다.".format(year, month, year / month))
print(f"오늘 날짜는 {year}.{month}.{day}입니다.")



wage = 5  # 시급 (1시간에 5달러)
exchange_rate = 1142.16  # 환율 (1달러에 1142.16원)

# "1시간에 5달러 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(1, wage * 1, "달러"))

# "5시간에 25달러 벌었습니다." 출력
print(f"5시간에 {wage * 5}달러 벌었습니다.")  # 코드를 채워 넣으세요.

# "1시간에 5710.8원 벌었습니다." 출력
print(f"1시간에 {wage * exchange_rate}원 벌었습니다.")  # 코드를 채워 넣으세요.

# "5시간에 28554.0원 벌었습니다." 출력
print("{1}시간에 {0:.1f}원 벌었습니다.".format(wage * wage * exchange_rate, wage))