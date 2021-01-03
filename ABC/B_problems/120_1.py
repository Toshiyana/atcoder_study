# 約数のカウント
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort(reverse=True) # 降順
    return divisors

a,b,k = map(int, input().split())
a_divs = make_divisors(a)
b_divs = make_divisors(b)
num = 0
flag = False
# print(a_divs)
# print(b_divs)

for i in a_divs:
  for j in b_divs:
    # print(i,j)
    if i == j:
      num += 1
      # print(num)
    if num == k:
      flag = True
      print(i)
      break # １回のbreakでは内側のループからしか抜け出せない

  if flag == True:
    break