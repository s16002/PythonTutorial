from timer import Timer
import random
LOOP_COUNT = 10000000

with Timer(verbose=True) as t:
    date = (1,2,3,4,5,6,7,8,9,10)
    for c in range(LOOP_COUNT):
        hoge = random.choice(date)


with Timer(verbose=True) as u:
    for d in range(LOOP_COUNT):
        hoge = random.randint(1,10)

pass