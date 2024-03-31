def solution(s):
    stack = []

    # ( 가 나올 경우에 리스트에 넣는다 ) 만날 경우 리스트를 팝하면서 리스트가 비었는지 확인한다.
    # 처음 시작이 )일 경우 바로 False 반환
    for i in s:
        if i == '(':
            stack.append(s)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    
    return stack == []