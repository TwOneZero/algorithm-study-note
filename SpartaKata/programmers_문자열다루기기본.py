# 문제 설명
# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
#
# 제한 사항
# s는 길이 1 이상, 길이 8 이하인 문자열입니다.
# s는 영문 알파벳 대소문자 또는 0부터 9까지 숫자로 이루어져 있습니다.

# 아스키 코드이용해서 풀기
# def solution(s):
#     # 문자열의 길이가 4 또는 6인지 확인
#     if len(s) != 4 and len(s) != 6:
#         return False
#
#     # 모든 문자가 숫자인지 확인
#     for char in s:
#         if ord(char) < 48 or ord(char) > 57:
#             return False
#
#     return True

# 내장 함수 이용 isdigit
def solution(s):
    answer = False

    if len(s) == 4 or len(s) == 6:
        answer = s.isdigit()

    return answer

