def solution(today, terms, privacies):

    answer = []
    now_days = int(today[0:4]) * 12 * 28 + int(today[5:7]) * 28 + int(today[8:])
    
    terms_dict = {term[0] : int(term[2:]) for term in terms}
    
    for i, privacy in enumerate(privacies, start=1):
        date, type = privacy.split()
        all = int(date[:4]) * 12 * 28 + int(date[5:7]) * 28 + int(date[8:10])
        result = all + terms_dict[type] * 28
    
        if result <= now_days:
            answer.append(i)
    
    return answer