N,Y = map(int, input().split())

ans_x = ans_y = ans_z = -1
for x in range(N+1):
  for y in range(N-x+1):
    z = N-x-y
    if 10000*x + 5000*y + 1000*z == Y:
      ans_x = x
      ans_y = y
      ans_z = z

print(ans_x,ans_y,ans_z)