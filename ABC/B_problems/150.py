# 自分の回答（なぜかRE）
# N = int(input())
# S = input()

# count = 0
# for i in range(N):
#   if S[i] == 'A':
#     if S[i+1] == 'B':
#       if S[i+2] == 'C':
#         count += 1

# print(count)

# 他人の模範回答
N = int(input())
S = input()
t = 'ABC'

count = 0
for i in range(N-2):
  if S[i:i+3] == t:
    count += 1

print(count)