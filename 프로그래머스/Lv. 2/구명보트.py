from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))

    while len(people) > 1: #무인도에 남아 있을 경우
        if people[0] + people[-1] <= limit:
            answer += 1
            people.pop()
            people.popleft()
        else:
            answer += 1
            people.pop()

    if people: # 한명만 남은 경우
        answer += 1

    return answer

print(solution([70, 50, 80, 50], 100))