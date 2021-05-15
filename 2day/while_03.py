meter = 100
base = 1
bounce = 3/5

while base <= 10 :
  meter *= bounce
  print(base, round(meter,4))
  base += 1