def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    times = {user: 0 for user in id_list}  # 사용자별 신고 횟수를 기록할 사전 초기화
    report = list(set(report))

    for rpt in report:
        reporter, reported_user = rpt.split()  # 신고한 사용자와 신고 대상 사용자 추출
        if reported_user in id_list:  # 신고 대상 사용자가 id_list에 포함된 사용자인지 확인
            times[reported_user] += 1  # 신고 대상 사용자의 신고 횟수 증가
        
    print(times)

    for rpt in report:
        reporter, reported_user = rpt.split()  # 신고한 사용자와 신고 대상 사용자 추출
        if times[reported_user] >= k and reported_user in id_list:
            answer[id_list.index(reporter)] += 1

    return answer


print(solution(["con", "ryan"]	, ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	, 3))
