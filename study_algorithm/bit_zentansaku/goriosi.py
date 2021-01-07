import time

def goriosi():
  N = 4
  for i in range(2):
    cond = [0]*N
    for j in range(2):
      for k in range(2):
        for l in range(2):
          cond[0] = i
          cond[1] = j
          cond[2] = k
          cond[3] = l
          print(cond)

if __name__ == '__main__':
    start = time.time()
    goriosi()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    # 0.07s