"""
✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются кратное двум число раз.
"""


nums = [1, 2, 1, 3, 2, 1, 1]

for num in nums:
    counter = nums.count(num)
    if nums.count(num) and counter % 2 == 0:
        for _ in range(counter):
            nums.remove(num)
print(nums)