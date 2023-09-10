def solution(phone_number):
    return "*"*len(phone_number[:-4]) + phone_number[-4:]

"""
아쉬운 점
 1. * 곱할 때 그냥 문자열길이 -4 만큼 해도 됐다...
"""