def calculate_change(payment, cost):
    # 코드를 작성하세요.
    payment -= cost
    
    print("50000원 지폐: {}장".format(int(payment / 50000)))
    payment %= 50000
    print("10000원 지폐: {}장".format(int(payment / 10000))) 
    payment %= 10000
    print("5000원 지폐: {}장".format(int(payment / 5000)))
    payment %= 5000
    print("1000원 지폐: {}장".format(int(payment / 1000)))
    #payment %= 1000
    #print("잔돈 : {}".format(payment))
    

# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)