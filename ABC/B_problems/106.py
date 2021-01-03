# 約数のカウント
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort() # 昇順
    return divisors

n = int(input())
ans = 0
#print(make_divisors(n))

for i in range(1,n+1):
  if i%2 == 1:
    if len(make_divisors(i)) == 8:
      ans += 1

print(ans)