import random

total_streaks = 0
current_streak = 0
flips = []

for i in range(10000):
    num = random.randint(0, 1)
    if num == 0:
        flips.append("H")
        current_streak += 1
        if current_streak >= 6:
            total_streaks += 1
    else:
        flips.append("T")
        current_streak = 0

print(total_streaks)
