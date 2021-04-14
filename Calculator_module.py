import Calculator as grrcackcack

print(grrcackcack.add(2, 5))
print(grrcackcack.multiply(3, 4))

import Calculator 
print(Calculator.add(2, 5))
print(Calculator.multiply(3, 4))

from Calculator import add, multiply, subtract 
## 특정 함수만 호출 
## *를 사용할 경우 함수 전체를 불러오지만 데이터 처리 측면에서 별로 함수들의 출처도 불분명해짐 
## 가독성 측면에서 이게 제일 좋은 듯
print(Calculator.add(2, 5))
print(Calculator.multiply(3, 4))




