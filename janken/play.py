HANDS = ('グー', 'チョキ', 'パー')
RESULTS = ('勝ち!', '負け!', '引き分け!')



def selectHand():
    import random
    y = random.randint(0, 2)
    return y


def judgement(c, d):
    if c == d:
        return 0
    elif (c == 0 and d == 1) or (c == 1 and d == 2) or (c == 2 and d == 0):
        return 1
    else:
        return -1


def saveScore(e):
    if e == 0:
        f = open('draw.txt', 'a')
        f.write('0')
    elif e == 1:
        f = open('won.txt', 'a')
        f.write('0')
    else:
        f = open('lost.txt', 'a')
        f.write('0')


def issue(g):
    if g ==1:
        return 0
    elif g == -1:
        return 1
    else:
        return 2


def past():
    k = open('won.txt', 'rb+')
    u = k.seek(0,2)
    print("勝ち：", u, "回", '  ', end='')
    k.close()

    k = open('lost.txt', 'rb+')
    u = k.seek(0, 2)
    print("負け:", u, "回",'  ', end='')
    k.close()


    k = open('draw.txt', 'rb+')
    u = k.seek(0,2)
    print("引き分け:", u, "回")


def score():
    m = open('score.text','w')
    m.write('')
    m.close()
    m = open('won.txt', 'rb+')
    v = m.seek(0,2)
    q = repr(v)
    m.close()
    m = open('score.text', 'a')
    m.write("勝ち:")
    m.write(q)
    m.write("回")
    m.write('   ')
    m.close()

    m = open('lost.txt', 'a')
    v = m.seek(0, 2)
    q = repr(v)
    m.close()
    m = open('score.text', 'a')
    m.write("負け:")
    m.write(q)
    m.write("回")
    m.write('   ')

    m = open('draw.txt', 'a')
    v = m.seek(0, 2)
    q = repr(v)
    m.close()
    m = open('score.text', 'a')
    m.write("引き分け:")
    m.write(q)
    m.write("回")





if __name__ == '__main__':
    x = int(input('グー(0),チョキ(1),パー(2):'))
    a = selectHand()
    result = judgement(x, a)
    saveScore(result)
    g = issue(result)
    score()



    print("computer:", HANDS[a])
    print("player:", HANDS[x])
    print()
    print('          ', RESULTS[g])
    print()
    past()



