def solution(arr):
    sum = 0
    for i in arr:
        sum += i

    answer = sum / len(arr)
    return answer

"""
아쉬운점
 1. 파이썬에 sum 함수가 있는걸 몰랐다
"""