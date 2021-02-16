'''자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.'''

def solution(n):
    answer = 0
    l = []

    while True:
        if (n < 3):
            l.insert(0, n)
            break;
        tmp = n
        mod = tmp % 3
        l.insert(0, mod)
        n = int(tmp / 3)
    #pow : 지수승 구하는 함수
    for i, j in enumerate(l):
        answer += j * pow(3, i)

    return answer