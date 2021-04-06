#실습1 태호는 미국 다트머스 대학교 컴퓨터 과학과에 지원하려고 합니다. 컴퓨터 과학 전공으로 미국 유학을 가고 싶기 때문에, 코딩 공부와 영어 공부를 모두 해야 하는 상황인데요. 
# 그 둘을 동시에 하기 위해서 파이썬으로 단어장 프로그램을 만들기로 합니다.

vocab = {
    'sanitizer' : '살균제',
    'ambition' : '야망',
    'conscience' : '양심',
    'civilization' : '문명'
}
print(vocab)

vocab['privilege'] = '특권'
vocab['principle'] = '원칙'

print(vocab)
print('특권' in vocab.values())
print('privilege' in vocab.keys())


for key, value in vocab.items():
    print(key, value)



#실습2 (실습1번과 연계)태호는 영어 단어 공부를 위해서 단어장 프로그램을 만들었습니다.
#  하지만 이번에는 영-한으로 공부하는 것이 아니라, 한-영으로 공부를 해 보고 싶습니다.
#사전의 key와 value를 뒤집어 주는 함수 reverse_dict를 작성해 주세요. 
# reverse_dict는 파라미터로 사전 dict를 받고, key와 value가 뒤집힌 새로운 사전을 리턴합니다.

def reverse_dict(dict):
    new_dict = {}
    for key, value in dict.items():
        new_dict[value] = key
    return new_dict
print(reverse_dict(vocab))

#실습3 효신이는 매년 국회의원 선거 때마다, 성북구에서 집계 도우미 봉사를 하는데요. 
# 작년까지는 표를 손수 세다가, 올해부터는 IT 시대에 더 적합한 솔루션을 개발하려고 합니다.
#파이썬 리스트 votes에는 성북구민들의 투표 결과가 저장되어 있습니다. 
# 리스트 votes의 정보를 토대로, 사전 vote_counter에 후보별 득표수를 정리하는 것이 목표입니다.
#예를 들어서 votes가 ['허유나', '서혜선', '허유나']라고 가정하면, vote_counter는 {'허유나': 2, '서혜선': 1}이 되어야 하는 거죠.

votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', 
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', 
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

vote_counter = {}

for name in votes:
    if name in vote_counter.keys():
        vote_counter[name] += 1
    else :
        vote_counter[name] = 1

print(vote_counter)