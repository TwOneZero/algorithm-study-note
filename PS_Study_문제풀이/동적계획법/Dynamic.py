
# Top-down / Bottom-up

# Memoization
# -> 부분 문제들의 답을 한 번 구했으면 또 구하지 않도록 (중복연산 방지)
# Cache 에 저장해두고 사용
# 필요한 부분 문제들만 구함 -> lazy Evaluation
# Top-down 방식에서 사용


# Tabulation
# 부분 문제들의 답을 미리 다 구해두자
# 테이블을 다 채워 놓음 -> Eager Evaluation
# Bottom-up 방식에서 사용

#-----------------
# 이항 계수 nCr
# bino(n,0) = 1
# bino(n ,n ) = 1
# bino(n, r) = bino(n-1, r-1) + bino(n-1, r)