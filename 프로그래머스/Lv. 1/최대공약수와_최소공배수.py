def solution(n, m):
    answer = []
    n_list = []
    m_list = []
    for i in range(1, n+1):
        if(n%i == 0):
            n_list.append(i)
    
    for j in range(1, m+1):
        if(m%j == 0):
            m_list.append(j)

    answer.append(max([x for i in n_list for x in m_list if i == x]))
    answer.append(n*m / answer[0])
    return answer
