import time
import random
from datetime import datetime

data = [4, 5, 6, 2, 1, 2, 34, 45, 54]
data_l = len(data) - 1
data.sort()
print(data)
count = 0
low = 0
target = int(input("Sonni kiriting: "))
print(datetime.now())
while True:
    time.sleep(1)
    count += 1
    middle = (data_l + low) // 2
    if data[middle] < target:
        low = middle + 1
    elif data[middle] == target:
        print(target)
        print(f"Count {count}")
        break
    else:
        data_l = middle

print(datetime.now())
