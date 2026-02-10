from datetime import datetime
import time
import random

odds = [1,3,5,7,9,11,13,15,17,19,21]

for i in range(3):
    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print("This min seems a little odd")
    else:
        print("Not an odd min")
    wait_time = random.randint(1,10)
    time.sleep(wait_time)