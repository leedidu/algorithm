def solution(s):
    answer = ''
    s_list = list(s)
    if(len(s_list) % 2 == 1): #길이가 홀수인 경우
        answer += s_list[int(len(s_list) / 2)]
    else: #길이가 짝수인 경우
        answer += (s_list[int(len(s_list) / 2) - 1] + s_list[int(len(s_list) / 2)])
    print(answer)
    return answer

"""
아쉬운 점
 1. 슬라이싱할 때 [1:2]면 2는 포함하지 않는다... 기본적인걸 또 ......... .. . . ..
"""