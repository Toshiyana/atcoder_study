# 参考：https://qiita.com/junkls/items/10384950963056cc8e08
# itertools.product：直積

import itertools
import time

def other_ans():
  N = 4

  # print(list(itertools.product((0,1), repeat = N)))
  # print(list(itertools.product((1,0), repeat = N)))
  # print(list(itertools.product(('a','b'), repeat = N)))

  for p in itertools.product((0,1), repeat = N):
    print(p)

if __name__ == '__main__':
    start = time.time()
    other_ans()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    # 0.03s
