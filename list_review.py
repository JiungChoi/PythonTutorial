# list 복습 후 중복되는 숫자가 있을 경우 지우는 함수 만들어 보기

numbers = [1, 2]
numbers2 = [2, 3]
numbers3 = numbers + numbers2
numbers3 += numbers2

print(f"numbers3 = {numbers3}")



def list_converter(num_list):
    new_list = []
    for num in num_list:
        if num not in new_list:
            new_list.append(num) #new_list.insert(len(new_list),num)
    return new_list

print(list_converter(numbers3))
