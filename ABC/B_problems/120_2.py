a,b,k = map(int, input().split())
result = []
minmum = min(a,b)

# 公約数の取得
for i in range(1,minmum+1):
  if a%i == 0 and b%i == 0:
    result.append(i)

print(result[-k])