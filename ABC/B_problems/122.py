s = input()
n = len(s)
ans = 0

#print('ACGT'.count(s))

for i in range(n):
  for j in range(i,n):
    # print(i, j+1)
    # print(j-i+1)
    # print(s[i:j+1])

      # for c in s[i:j+1]:
      #   print(c)
        # print('ACGT'.count(c) == 1)

    if all('ACGT'.count(c) == 1 for c in s[i:j+1]):
      ans = max(ans, j-i+1)
      #print(ans)

print(ans)