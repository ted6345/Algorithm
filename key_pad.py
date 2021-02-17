'''
문제: 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.
https://programmers.co.kr/learn/courses/30/lessons/67256


0 1  2
3 4  5
6 7  8
9 10 11
숫자패드의 숫자에 1씩 감소시키고 3으로 나누었을때
나머지,몫을 통해 각패드의 좌표를 계산할수있다.
'''


def solution(numbers, hand):
    answer = ''

    _numbers = [j - 1 for j in numbers]

    l_thumb = 9
    r_thumb = 11
    for i in _numbers:

        if (i < 0): i = 10

        m, n = divmod(i, 3)

        if n == 0:
            answer += 'L'
            l_thumb = i
        elif n == 2:
            answer += 'R'
            r_thumb = i
        else:
            l_m, l_n = divmod(l_thumb, 3)
            r_m, r_n = divmod(r_thumb, 3)
            l_dis = abs(m - l_m) + abs(n - l_n)
            r_dis = abs(m - r_m) + abs(n - r_n)

            if (l_dis < r_dis):
                answer += 'L'
                l_thumb = i
            elif (r_dis < l_dis):
                answer += 'R'
                r_thumb = i
            elif (hand == "left"):
                answer += 'L'
                l_thumb = i
            else:
                answer += 'R'
                r_thumb = i
    return answer



