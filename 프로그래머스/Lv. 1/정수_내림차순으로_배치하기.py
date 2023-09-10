def solution(n):
    answer = ""
    n_list  = list(map(str, str(n)))
    n_list = reversed(sorted(n_list))
    for i in n_list:
        answer += i
    return int(answer)

"""
아쉬운 점
 1. .join 쓰는 방식이 있었다... 몰라서 못쓰다니
 2. sorted하면 리스트로 반환해서 나오기 때문에 list로 감싸지 않아도 된다는 댓글을 봄
"""