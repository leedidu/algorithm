def solution(s):
    return True if str.isdigit(s) and (len(s) == 4 or len(s) == 6)  else False

"""
아쉬운 점
 1. 자바랑 맨날 헷갈린다.. && || 이거...
 2. 굳이 True 안적어두고 불리언 값만 해도 됐을 것 같다
"""