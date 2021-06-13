num = 2
mul = 1

# while num <= 9 :
#   while mul <= 9 :
#     print ( num, ' * ', mul, ' = ', num*mul)
#     mul += 1
#   num += 1
#   mul = 1

# for i in range(num, 10) :
#   for j in range(1, 10) :
#     # print ( i , '*', j, '=', i*j)
#     print (f'{i} * {j} = {i*j}')

def multi(m) :
  for n in range(1,10) :
    print (f'{m} * {n} = {m*n}')

multi(3)