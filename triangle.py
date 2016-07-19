#キーボードから数字入力
#その高さの三角形を＊で出力


"""

5
*
**
***
****
*****

"""
"""
for i in range(h)
    print( '*' * h)

print()
"""
"""
def pascal(h):
    if(x == 1 or x == y):
        return 1
    else:
        return pascal(x - 1, y - 1) + pascal(x, y - 1)

    def line(n):
        a = []
        for i in range(n):
            a.append(pascl(i, n))
            return a
    for i in range(10):
    print line(i + 1)
"""

h = int(input('高さを入力してください'))
"""
def f(h,L=()):
        L.append(h)
        return L
for i in range(h):
    print(f(* * h))

"""

for i in range(1,h+1):
    print('*' * i)
"""
h = int(input'高さを入力してください'))

for horizontal in range(h + 1)
    for vertical in range(horizontal):
        print('*', end='')

    print()


for vertical in range(h + 1):
    for horizontal in range(vertical):
        if horizontal == 0 or horizontal == vertical - 1:
            print('*', end='')
        else:
            print('+', end='')

    print()
"""
