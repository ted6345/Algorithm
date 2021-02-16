'''
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
'''


def solution(a, b):
    # 파이썬에서는 다음과 같이 한 줄로 두 값을 바꿔치기할 수 있습니다.
    if (b > a):
        a, b = b, a

    return (a + b) * (a - b + 1) / 2


def adder(a, b):
    # 함수를 완성하세요
    return sum(range(min(a, b), max(a, b) + 1))