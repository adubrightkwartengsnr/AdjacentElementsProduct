def solution(inputArray):
    answer = []
    for i in range(len(inputArray)-1):
        product = inputArray[i] * inputArray[i + 1]
        answer.append(product)
    answer.sort(reverse=True)
    return answer[0]


print(solution([3, 6, -2, -5, 7, 3]))
