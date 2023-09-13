def solution(a, b):
    answer = ''
    month = [30, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    if a == 1:
        answer = day[(5 + (b-1))%7]
    else:
        day_sum = 0
        for i in range(a-1):
            day_sum += month[i]
        answer = day[(5 + (day_sum + b)) % 7]
    return answer

"""
생각한 방식
 1. (입력한 달의 직전달까지의 일수 총합 + 일수) % 7 하면 나머지가 나온다.
 2. 금요일 인덱스인 5를 기준으로 점프하면 해당 요일이 나온다.
 3. 7로 나눈 나머지를 이용해서 인덱스를 구해서 해당 요일의 인덱스를 출력하면 된다.

아쉬운 점
 1. sum[:a-1] >> 이용했다면 조금 더 깔끔했을 것 같다
"""