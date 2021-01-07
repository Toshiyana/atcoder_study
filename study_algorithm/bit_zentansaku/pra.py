N = 4
# print(1<<4) # 16
# print(range(1<<4)) # range(0,16)

for i in range(1<<N): # range(0,16)
  # print(i)
  # print(bin(i))
  cond = [0]*N
  for j in range(N):
    if 1 & (i>>j):
      cond[j] = 1

  print(cond)