"""

while True:
    try:
        x = int(input('数字を入れてくださいな: '))
        break
    except (ValueError, NameError, TypeError):
        print("数字じゃないのう")
"""
