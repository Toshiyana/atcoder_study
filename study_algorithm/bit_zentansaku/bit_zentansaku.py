# 参考: https://note.nkmk.me/python-bit-operation/
# <<：左シフト演算子
# >>：右シフト演算子

N = 4

# print(1<<4) # 16
# print(bin(1<<4))
# print('')

for i in range(1<<N): # 0~15
  # print(i)
  # print(bin(i))
  cond = [0]*N
  #print(cond)
  for j in range(N):
    # print(i, j, bin(i>>j))
    # print(1 & (i>>j)) # 2^0の位が0か１か判定
    if 1 & (i>>j):
      cond[j] = 1

  print(cond)