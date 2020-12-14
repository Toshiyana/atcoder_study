import re
S = input()
'''
https://qiita.com/hiroyuki_mrp/items/29e87bf5fe46de62983c
https://qiita.com/hiroyuki_mrp/items/29e87bf5fe46de62983c
メタ文字：
^ = 文字列の先頭、
| = OR
+ = 直前のパターンを1回以上繰り返し、
$ = 文字列の末尾
. = なんでも良い一文字

\：エスケープ
'''
if re.match("^(dream|dreamer|erase|eraser)+$", S):
    print('YES')
else:
    print('NO')