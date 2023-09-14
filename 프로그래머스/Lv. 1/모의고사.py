def solution(answers):
    answer = []
    ans_1 = [1, 2, 3, 4, 5]
    ans_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]

    for i in range(len(answers)):
        if(answers[i] == ans_1[(i + 1) % len(ans_1) - 1]):
            score[0] += 1
        if(answers[i] == ans_2[(i + 1) % len(ans_2) - 1]):
            score[1] += 1
        if(answers[i] == ans_3[(i + 1) % len(ans_3) - 1]):
            score[2] += 1
    
    max_score = max(score)
    for i in range(len(score)):
        if(max_score == score[i]):
            answer.append(i+1)
    return answer

"""
* 답안(answers)의 길이는 5 이상일 수도 있다는 점 고려
1. 0을 나눌 순 없으니 i + 1을 답안의 길이로 나눈다.
2. 인덱스는 0부터 시작이니 -1을 해줌
3. 답안과 해당 인덱스의 값이 같을 경우 score 인덱스를 +1 해줌
4. 가장 큰 값을 max_score에 저장 -> 최고점이 여러명일 수도 있음을 고려
5. 최고점과 score의 인덱스 값이 같을 경우 answer에 해당 학생을 추가
"""