N,Y = map(int, input().split())

flag = 0
for x in range(N+1):
  for y in range(N-x+1):
    z = N-x-y
    if 10000*x + 5000*y + 1000*z == Y:
      flag = 1
      print(x,y,z)
      break
  if flag == 1:
    break

if flag == 0:
  print(-1,-1,-1)