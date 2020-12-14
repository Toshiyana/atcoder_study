N = int(input())
t = [0] * (N+1)
x = [0] * (N+1)
y = [0] * (N+1)

for i in range(N):
  t[i+1],x[i+1],y[i+1] = map(int, input().split())

flag = True
for i in range(N):
  dt = t[i+1] - t[i]
  dist = abs(x[i+1]-x[i]) + abs(y[i+1]-y[i])
  if dt < dist:
    flag = False
  if dist%2 != dt%2:
    flag = False

print('Yes' if flag else 'No')