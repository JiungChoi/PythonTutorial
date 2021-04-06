#실습1 함수 sum_digit은 파라미터로 정수형 num을 받고, num의 각 자릿수를 더한 값을 리턴합니다.
#예를 들어서 12의 각 자릿수는 1, 2이니까 sum_digit(12)는 3(1 + 2)을 리턴합니다.
#마찬가지로 486의 각 자릿수는 4, 8, 6이니까 sum_digit(486)은 18(4 + 8 + 6)을 리턴하는 거죠.

def sum_digit(num):
    num_list = str(num)
    
    output = 0
    for i in num_list:
        output += int(i)

    return output

result = 0
for i in range(1001):
    result += sum_digit(i)

print(result)

#실습2 주민등록번호 YYMMDD-abcdefg는 총 열세 자리인데요. 앞의 여섯 자리 YYMMDD는 생년월일을 의미합니다.
#YY → 연
#MM → 월
#DD → 일
#뒤의 일곱 자리 abcdefg는 살짝 복잡합니다.
#a → 성별
#bc → 출생등록지에 해당하는 지방자치단체의 고유번호
#defg → 임의의 번호
#보시다시피 많은 부분은 특정 규칙대로 정해져 있는데요. 여러분에 대한 몇 가지 정보만 알면, 마지막 네 개 숫자 defg를 제외한 앞의 아홉 자리는 쉽게 알 수 있다는 거죠.
#그래서 저희는 주민등록번호의 마지막 네 자리 defg만 가려 주는 보안 프로그램을 만들려고 합니다.
#mask_security_number라는 함수를 정의하려고 하는데요. 이 함수는 파라미터로 문자열 security_number를 받고, security_number의 마지막 네 글자를 '*'로 대체한 새 문자열을 리턴합니다.
#참고로 파라미터 security_number에는 작대기 기호(-)가 포함될 수도 있고, 포함되지 않을 수도 있는데요.  작대기 포함 여부와 상관 없이, 마지막 네 글자가 '*'로 대체되어야 합니다!


def mask_security_number(security_number):
    change_number = ''
    count_num = 0
    for number in security_number:
        if '-' in security_number:
            if count_num >= 10:
                 change_number += '*'
            else:
                 change_number += number                
        else:
            if count_num >= 9:
                change_number += '*' 
            else:
                change_number += number
        count_num += 1
    return change_number


print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))

#실습3 "토마토"나 "기러기"처럼 거꾸로 읽어도 똑같은 단어를 '팰린드롬(palindrome)'이라고 부릅니다.
#팰린드롬 여부를 확인하는 함수 is_palindrome을 작성하려고 하는데요. is_palindrome은 파라미터 word가 팰린드롬이면 True를 리턴하고 팰린드롬이 아니면 False를 리턴합니다.
#예를 들어서 "racecar"과 "토마토"는 거꾸로 읽어도 똑같기 때문에 True가 출력되어야 합니다. 그리고 "hello"는 거꾸로 읽으면 "olleh"가 되기 때문에 False가 나와야 하는 거죠.

def is_palindrome(word):
    T_F= True
    for i in range(int(len(word) / 2)):
        if word[i] != word[(len(word) - 1) - i]:
            T_F = False
    
    return T_F




print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))