num = int(input('input:'))

L = list(range(1,num+1))

for i in range(4, num + 1):
  if i % 2 == 0 :
    L.remove(i)
  elif i % 3 == 0 :
    L.remove(i)

print(L)
