n = 20
e = 3

i = 0
sum_num = 0

while i <= n:
    i += 1
    if i % e == 0 or i % 2 != 0:
        continue
    sum_num += i

print(sum_num)