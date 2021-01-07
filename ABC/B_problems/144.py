# N = int(input())

# flag = 0
# for i in range(1,10):
#   for j in range(1,10):
#     if i*j == N:
#       flag = 1

# print('Yes' if flag==1 else 'No')

# 誤った場合を先に変数に入れておく書き方の方が良いかも
N = int(input())

ans = 'No'
for i in range(1,10):
  for j in range(1,10):
    if i*j == N:
      ans = 'Yes'

print(ans)