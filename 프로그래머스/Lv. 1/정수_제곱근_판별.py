def solution(n):
    answer = 0
    n_sqrt = n**(1/2)
    if(n_sqrt == int(n_sqrt)):
        answer = (n_sqrt+1) ** 2
    else:
        answer = -1
    return answer

"""
아쉬운 점
 1. 제곱근 구하는 방식
 2. 문제 자꾸 제대로 안읽어서 시간 낭비함
"""