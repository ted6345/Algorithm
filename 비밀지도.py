def invertbin(n, v):
    l = []
    while (v >= 1):
        x, y = divmod(v, 2)
        l.append(y)
        v = x
    while len(l) < n:
        l.append(0)
    l.reverse()
    return l


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp1 = invertbin(n, arr1[i])
        tmp2 = invertbin(n, arr2[i])
        result = ''.join(['#' if x + y > 0 else ' ' for x, y in zip(tmp1, tmp2)])
        answer.append(result)

    return answer


# 추천풀이
def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        # bin(x)
        # 정수를 《0b》 가 앞에 붙은 이진 문자열로 변환합니다. 결과는 올바른 파이썬 표현식입니다
        a12 = str(bin(i | j)[2:])
        # rjust (채울 수, 매꿀문자)오른쪽으로 정렬하도록 도와준다.
        a12 = a12.rjust(n, '0')
        # replace
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer