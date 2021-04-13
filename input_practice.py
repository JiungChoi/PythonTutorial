import random
ans = random.randint(1,20)
tryy = 0

for tryy in range(0,5):
    chance = 4 - tryy
    if chance == 0:
        print(f'아쉽습니다. 정답은{ans}입니다.')
        break
    input_ans = int(input(f'기회가 총 {chance}번 남았습니다. 1 - 20 사이의 숫자를 맞혀 보세요.:'))
    if ans > input_ans:
        print(f'{input_ans}Up')
    elif ans < input_ans:
        print(f'{input_ans}down')
    elif ans == input_ans:
        print(f'축하합니다. {tryy}번 만에 숫자를 맞히셨습니다.')
        break