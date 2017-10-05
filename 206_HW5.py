import re

list = []
file = open("HW5_data.txt", "r")
sum = 0
for line in file:
    num = re.findall("[0-9]+", line)
    if (num != []):
        list.extend(num)
for num in list:
    sum += int(num)

print (sum)
