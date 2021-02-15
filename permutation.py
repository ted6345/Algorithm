'''
정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
'''


def solution(numbers):
    n = len(numbers)
    answer = []

    print("n", n)
    # permutation
    for i in range(0, n - 1):
        print("i", i)
        for j in range(i + 1, n):
            print("j", j)
            k = numbers[i] + numbers[j]
            answer.append(k)

    answer = sorted(list(set(answer)))
    return answer