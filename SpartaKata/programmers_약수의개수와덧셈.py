# 문제 설명
# 두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# 1 ≤ left ≤ right ≤ 1,000


# 완전 제곱수인지를 판별하는 것이 포인또

def solution(left, right):
    result = 0
    for num in range(left, right + 1):
        # 약수의 개수가 홀수인 경우 - 완전 제곱수
        if int(num ** 0.5) ** 2 == num:
            result -= num
        else:
            result += num
    return result
