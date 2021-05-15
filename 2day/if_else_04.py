year = int(input('계산할 년도를 입력:'))

if year % 4 != 0 :
  print(year, ': 평년')
elif year % 100 != 0 :
  print(year, ': 윤년')
elif year % 400 != 0 :
  print(year, ': 평년')
else :
  print(year, ': 윤년')