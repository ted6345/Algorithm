def solution(seoul):
    answer = ''
    idx = str(seoul.index("Kim"))
    answer = "김서방은 " + idx + "에 있다"

    return answer


def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))