'''
문자 -> 아스키코드 : chr()

아스키코드 -> 문자 : ord()
'''


def solution(s, n):
    answer = ''

    print(ord(' '))
    for i in s:
        if (i == ' '):
            answer += ' '
            continue

        tmp = 0
        if (int(ord(i)) < 95):
            tmp = (ord(i) + n - 65) % 26 + 65
        else:
            tmp = (ord(i) + n - 97) % 26 + 97

        answer += chr(tmp)
    return answer