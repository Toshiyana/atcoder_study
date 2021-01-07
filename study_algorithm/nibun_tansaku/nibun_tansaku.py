# 参考：https://qiita.com/T_Wakasugi/items/c979e977f56531942de4

# bisectを使うときは，listはソートしておく．
# でないと，間違った形で二分探索が行われる

# bisect_left: 探索した値の前に，値を挿入
# bisect_right: 探索した値の後ろに，値を挿入

import bisect

def search(t,i):
  """
  t: list 探索元の数列
  i: int 探索する値
  """
  ix = bisect.bisect_right(t,i)
  # ix = bisect.bisect_left(t,i)
  print(ix)
  if t[ix-1] != i:
    return False
  else:
    return True

t = [1,3,5,6,7,10]
i = 7

print(search(t, i))  # True