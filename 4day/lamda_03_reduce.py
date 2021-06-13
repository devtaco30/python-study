# reduce(함수, 순서형 자료)
# 누적 연산 reduce

from functools import reduce

reduce(lambda x,y : x+y, [0,1,2,3,4])

print(reduce(lambda x,y : x+y, [0,1,2,3,4]))


reduce(lambda x,y : x+y, 'abcde')

print(reduce(lambda x,y : y+x, 'abcde'))