N = int(input())
d = [int(input()) for _ in range(N)]
d.sort(reverse = True)

count = 0
tmp = 0
for i in d:
  if i != tmp:
    count += 1

  tmp = i

print(count)