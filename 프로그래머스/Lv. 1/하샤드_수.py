def solution(x):
    x_list = list(map(int, str(x)))
    sum = 0
    for i in x_list:
        sum += i
    if((x % sum) == 0):
        return True
    else:
        return False
    
"""
 1. n%sum(int(x) for x in str(n)) == 0 한줄로 정의한 코드가 있다...
    - str(n) : 문자열로 변환
    - x 를 int(x)로 형변환
    - n과 x들의 합을 나눈 나머지가 0인지 판별
"""