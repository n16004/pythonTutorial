""""n, m, l = [int(i) for i in input().split()]

A = []
B = []
C = []

for ni in range(n):
    A.append([int(i) for i in input().split()])

for mi in range(m):
    B.append([int(i) for i in input().split()])

for i in range(n):
    C.append([])
    for j in range(l):
        C[i].append(0)
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]
for ni in range(l):
    print(" ".join([str(s) for s in C[ni]))
"""""
"""while True:
    data = input()
    if data == '0':
        break
    print(sum([int(i) for i in data]))
"""
"""
while True:
    data = input()
    if data == '0':
        break

    print(sum([int(i) for i in data]))
"""
"""import string

count = {x: 0 for x in string.ascii_lowercase}
lines = ""

while True:
    try:
        lines += input().lower()
    except EOFError:
        break

for c in lines:
    if 'a' <= c <= 'z':
        count[c] += 1

for key in string.ascii_lowercase:
    print("{0} : {1}".format(key, count[key]))
"""

"""W = input()
count = 0
while True:
    line = input()
    if line == 'END_OF_TEXT':
        break

    for s in line.lower.split():
        if s == W:
            count += 1
print(count)
"""
"""while True:
    s = input()

    if s == '-':
        break

    m = int(input())
    for mi in range(m):
        h = int(input())
        s = s[h:] + s[:h]

    print(s)
"""
"""
n = int(input())

taro = 0
hanako = 0
for ni in range(n):
    t, h = input().split()
    if t < h:
        hanako += 3
    elif t > h:
        taro += 3
    else:
        hanako += 1
        taro += 1

print(taro, hanako)
"""
"""
s = input()
q = input()

for qi in range(q):
    command = input().split()
    a = int(command[1])
    b = int(command[2])
    if command[0] == 'print':
        print(s[a:b + 1])
    elif command[0] == 'reverse':
        s = s[:a] + s[a:b + 1][::-1] + s[b + 1:]
    else:
        p = command[3]
        s = s[:a] + p + s[b + 1:]
"""
HANDS = ('グー', 'チョキ', 'パー')
import random

def select_hand():
    HANDS_choice = random.choice(HANDS)
    return HANDS_choice

    """
    コンピュータの手をランダムに決める
    :return: HANDSの中のいずれか。
    """


def judgement(player,  computer):
    if player == 'グー' and computer == 'チョキ':
        return 1
    if player == 'チョキ'  and computer == 'パー':
        return 1
    if  player == 'パー' and computer == 'グー':
        return 1

    elif player == computer:
        return 0
    else:
        return -1



def save_score(result):
    if result == -1:
        return "'lose:y'"
    elif result == 0:
        return "'draw:z'"
    else:
        return "'win:x'"
    return None


    """

    :param result:
    :return:
    """
"""
    b = [{'win':'x', 'lose':'y', 'draw':'z'}]
    f = open("score.py","w")
    ff = b[result]
    f.write(ff)
    f.close

    'score.txt'に戦績を保存。
    win:x lose:y draw:zのディクショナリデータを保存する。
    :param result:
    :return: Non
"""


if __name__ == '__main__':
    player = HANDS[int(input('グー(0)/チョキ(1/パー(2)を選んでください(数字): '))]
    computer = select_hand()
    result = judgement(player, computer)
    score = save_score(result)
    # コンピュータの手と勝敗の結果を表示


    print(result)
    print(player, computer)
    score
    f = open("score.txt", "a")
    f.write(score)
    f.close
