def k_return(_array, _com):
    # 종료인덱스의 원소는 포함되지 않고 바로 앞 원소까지만 포함됩니다. step은 생략됩니다.
    _array = _array[_com[0] - 1:_com[1]]
    _array.sort()
    return _array[_com[2] - 1]


def solution(array, commands):
    answer = []
    for i in commands:
        answer.append(k_return(array.copy(), i))


    return answer


print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]] ))