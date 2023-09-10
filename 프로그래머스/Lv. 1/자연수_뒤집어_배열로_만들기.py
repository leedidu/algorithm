def solution(n):
    n_list = list(map(int, str(n))) # n을 str로 변환 -> map을 이용하여 각 문자를 정수로 변환 -> list로 변환
    answer = list(reversed(n_list))
    return answer

"""
아쉬운 점
 1. 자릿수 쪼개는 걸 처음 해보는 것 같아서 당황..
 2. 슬라이싱을 이용하는 방식 [::-1] 을 사용 했어도 좋았을 것 같음
"""