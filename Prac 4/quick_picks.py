import random

MIN_QUICK_PICK = 1
MAX_QUICK_PICK = 45
COLUMN = 6

no_of_quick_picks = int(input("How many quick picks? "))
quick_picks = []
for row in range(no_of_quick_picks):
    for column in range(COLUMN):
        quick_pick = random.randint(MIN_QUICK_PICK, MAX_QUICK_PICK)
        if quick_pick not in quick_picks:
            quick_picks.append(quick_pick)

        print("{:2}".format(quick_pick), end=' ')
    print()


