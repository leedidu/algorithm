def solution(N, stages):
    answer = []
    N_stages = [0 for i in range(N+1)]
    failure_rate = {}
    for i in range(len(stages)):
        N_stages[stages[i]-1] += 1

    len_stages = len(stages)
    for i in range(len(N_stages)):
        if(len_stages != 0):
              failure_rate[i+1] = N_stages[i] / len_stages
              len_stages -= N_stages[i]
        else:
            failure_rate[i+1] = 0
    
    failure_rate.pop(N+1)
    print(failure_rate)
    failure_rate = sorted(failure_rate.items(), key=lambda x:x[1], reverse=True)

    for i in range(len(failure_rate)):
        answer.append(failure_rate[i][0])
    return answer

"""
1. 각 스테이지에 도전 중인 사용자의 수를 각각 저장
2. 사용자를 줄여나가면서 계산
3. N+1도 리스트에 들어가니 지워줌
4. 딕셔너리를 value값으로 정렬
5. key값만 answer에 추가해줌
"""