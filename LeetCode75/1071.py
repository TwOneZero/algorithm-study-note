from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+ str2 != str2 +str1:
            return ""
        # 순서를 바꿔 합쳐도 대칭이 되면 gcd 를 뽑을 수 있음.
        return str1[:gcd(len(str1), len(str2))]