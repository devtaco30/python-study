# 다음과 같은 복리 계산 공식을 이용하면 됩니다.

# P′=P(1+rn)nt
# P′ : 원리금
# P : 원금
# r : 연이율
# t : 기간
# n : 복리 횟수

def compound_interest_amout(p , r, t, n) :
    return p * ( 1 + r / n ) ** (n * t)

print(compound_interest_amout(1500000, 0.043,6,4))