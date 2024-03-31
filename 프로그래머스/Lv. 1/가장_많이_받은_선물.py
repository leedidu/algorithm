def solution(friends, gifts):
    gift_matrix = [[0] * len(friends) for _ in range(len(friends))]  # 2차원 리스트 초기화
    gift_index_matrix = [[0] * 3 for _ in range(len(friends))]  # 2차원 리스트 초기화
    answer = [0] * len(friends)

    for gift in gifts:
        giver, receiver = gift.split(' ')
        gift_matrix[friends.index(giver)][friends.index(receiver)] += 1
        gift_index_matrix[friends.index(giver)][0] += 1
        gift_index_matrix[friends.index(receiver)][1] += 1
    
    for user in gift_index_matrix:
        user[2] = user[0] - user[1]
    
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            if(gift_matrix[i][j] > gift_matrix[j][i]):
                answer[i] += 1
            elif(gift_matrix[i][j] < gift_matrix[j][i]):
                answer[j] += 1
            elif(gift_matrix[i][j] == gift_matrix[j][i]):
                if gift_index_matrix[i][2] > gift_index_matrix[j][2]:
                    answer[i] += 1
                elif gift_index_matrix[i][2] < gift_index_matrix[j][2]:
                    answer[j] += 1
                else:
                    answer[j] += 0

    return max(answer)

print(solution(	["a", "b", "c"], 
["a b", "b a", "c a", "a c", "a c", "c a"]))