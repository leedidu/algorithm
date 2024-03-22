import math

def solution(numbers, hand):
    answer = ''
    
    keypad = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        "*": [3, 0], 0: [3, 1], "#": [3, 2]
    }

    left = keypad["*"]
    right = keypad["#"]

    for i in numbers:
        if(i in [1,4,7]):
            answer+="L"
            left = keypad[i] # 왼쪽 손으로 변경
        if(i in [3,6,9]):
            answer+="R"
            right = keypad[i] # 오른쪽 손으로 변경
        if(i in [2,5,8,0]):
            left_dis = dist(left, keypad[i])
            right_dis = dist(right, keypad[i])
            if(left_dis > right_dis):
                answer += "R"
                right = keypad[i]
            if(left_dis < right_dis):
                answer += "L"
                left = keypad[i]
            if(left_dis == right_dis):
                if(hand == "right"):
                    answer += "R"
                    right = keypad[i]
                else:
                    answer += "L"
                    left = keypad[i]
                    
    return answer

def dist(point1, point2):
    y1, x1 = point1
    y2, x2 = point2
    return abs(y2-y1) + abs(x2-x1)

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))