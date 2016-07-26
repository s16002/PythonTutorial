HANDS = ('グー', 'チョキ', 'パー')


def selectHand():
    import random
    b = random.randint(0, 2)
    return b


def judgement( x, a):
    if x == a:
        return 0
    elif (x == 0 and a == 1) or (x == 1 and a == 2) or (x == 2 and a == 0):
        return 1
    else:
        return -1


def saveScore(result):
    pass


if __name__ == '__main__':
    x = int(input('グー(0),チョキ(1),パー(2):'))
    a = selectHand()
    result = judgement(x, a)

    print("computer:", HANDS[a])
    print("player:", HANDS[x])
    print(result)
