'''두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.'''


def solution(n, m):
    max_ = 1
    min_ = m * n
    for i in range(1, int(min(m, n) / 2) + 1):
        if (n % i) + (m % i) == 0:
            max_ = i
    if max(m, n) % min(m, n) == 0:
        max_ = min(m, n)
    min_ /= max_

    return [max_, min_]

'''유클리드 호제법 log(n)
1071과 1029의 최대공약수를 구하면,

1071은 1029로 나누어떨어지지 않기 때문에, 1071을 1029로 나눈 나머지를 구한다. ≫ 42
1029는 42로 나누어떨어지지 않기 때문에, 1029를 42로 나눈 나머지를 구한다. ≫ 21
42는 21로 나누어떨어진다.
따라서, 최대공약수는 21이다.'''

def gcdlcm(n, m):

    a,b = min(n,m),max(n,m)

    while b%a >0 :
        tmp = b%a
        b,a =  a,tmp

    return [a,m*n/a]






