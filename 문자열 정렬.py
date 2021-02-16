'''
1. sort
원본을 변형시켜 정렬한다. '변수. sort( )' 형태로 사용.

2. sorted
정렬된 결과를 반환. 원형을 변형시키지 않는다. 괄호( ) 안에 반복 가능한 iterable 자료형을 입력하여 사용한다. 정렬 기준은 문자열은 알파벳, 가나다순이고 숫자는 오름차순이 기본값이다.

3. Parameter
sort, sorted 모두 key, reverse 매개변수를 갖고 있다.

3-1. reverse

bool값을 넣는다. 기본값은 reverse=False(오름차순)이다.

reverse=True를 매개변수로 입력하면 내림차순으로 정렬할 수 있다.

>>> num_list = [15, 22, 8, 79, 10]
>>> num_list.sort(reverse=True)
>>> print(sorted(list, reverse=True))

3-2. key

정렬을 목적으로 하는 함수를 값으로 넣는다. lambda를 이용할 수 있다.

key 값을 기준으로 정렬되고 기본값은 오름차순이다.

>>> str_list = ['좋은하루','good_morning','굿모닝','niceday']
>>> print(sorted(str_list, key=len))  # 함수
['굿모닝', '좋은하루', 'niceday', 'good_morning']

>>> print(sorted(str_list, key=lambda x : x[1]))  # 람다
['niceday', 'good_morning', '굿모닝', '좋은하루']
'''

'''문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다.
 예를 들어 strings가 [sun, bed, car]이고 n이 1이면 각 단어의 인덱스 1의 문자 u, e, a로 strings를 정렬합니다.'''


def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])

    answer = []
    _answer = []
    for j in strings:
        answer.append(j[n] + j)
    answer.sort()
    for i in answer:
        _answer.append(i[1:])

    return _answer
