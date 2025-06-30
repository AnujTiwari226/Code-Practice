import random
from itertools import accumulate


def random_walk_faster(n=1000):
    # Only available from Python 3.6
    steps = random.choices([-1,+1], k=n)
    print(steps)
    return [0]+list(accumulate(steps))

walk = random_walk_faster(1000)
print(walk)