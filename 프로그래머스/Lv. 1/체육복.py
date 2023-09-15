def solution(n, lost, reserve):
    save_lost = sorted([i for i in lost if i not in reserve])
    save_reserve = sorted([i for i in reserve if i not in lost])

    for i in save_reserve:
        if i - 1 in save_lost:
            save_lost.remove(i - 1)
        elif i + 1 in save_lost:
            save_lost.remove(i + 1)
    return n - len(save_lost)


print(solution(5, [4, 2], [3, 4, 5]))

"""
1. 여벌이 있는 학생이 도난 당했을 수도 있으니 그걸 제외한 real_lost real_reserve를 저장
2. 만약 lost의 각 요소 +- 1 값이 reserve에 있을 경우 lost와 reserve를 지운다
3. 전체 n 에서 잃어버린 수를 지움

아쉬운 점
1. sorted를 했어야 했다.
2. - 1의 경우 부터 해야한다. -> + 1부터 하면 경우의 수가 줄어들기 때문...!! 이거
>> 이거 때문에 시간을 많이 잡아먹음.........
"""