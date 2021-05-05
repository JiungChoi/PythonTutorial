english=[]
korean=[]
len_list = 0


while 1:
    pre_english = input("영어를 입력하세요: ")
    if (pre_english == 'q'):
        break
    elif(pre_english == 'g'):
        print("< 빠밤 단어 퀴즈입니다 ^^ >")
        for quiz in pre_eglish:
            print("quiz")            

    if pre_english in english:
        print("ㅃ삐")
        continue
    else:
        english.append(pre_english)

    korean.append(input("한국어 뜻을 입려하세요:"))
    len_list += 1


