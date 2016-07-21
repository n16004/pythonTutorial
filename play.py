
HANDS = ("グー", "チョキ", "パー")

def selectHnad():
    """
    コンピュータの手をランダムに決める

    :return:　HANDSの中のいずれか。
    """
    import random
    i = random.randint(0, 3)
    return i

def judgement(player, computer):

    """
     じゃんけんの勝利を判定をする。
    :param player: HANDOSの中のどれか
    :param computer: HANDOSのなかのどれか
    :return: プレイヤーが勝ちの場合は１、あいこは０、負けは−１を返す
    """
    if player == computer:
        return 0
    elif player == 1:
        if computer == 3:
            return -1
        elif computer == 2:
            return 1

    elif player == 2:
        if computer == 1:
            return -1
        elif computer == 3:
            return 1

    elif player == 3:
        if computer == 1:
            return 1
        elif computer == 2:
            return -1





"""def save_score(result):

    'score.txt'に戦績を保存。
    win:x lose:y drew:z のディクショナリデータを保存する。

    :param result:
    :return: None
    """


if __name__ == '__main__':
    player = int(input('グー(1)/チョキ（２）/パー(3)を選んでください: '))
    computer = selectHnad()
    result = judgement(player, computer)
    #コンピュータの手と勝敗の結果を表示

    print("computer", HANDS[computer])
    print(result)
