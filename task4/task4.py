
import math
import sys

nums = []
file_name = sys.argv[1]
with open(file_name) as f:
    for line in f:
        sep = line.strip()
        x = int(sep)
        nums.append(x)
f.close()

result_digit = round(sum(nums)//len(nums))
count = 0
for id, i in enumerate(nums):
    while i != result_digit:
        if i < result_digit:
            i += 1
            count += 1
        elif i > result_digit:
             i -= 1
             count += 1
print(count)
