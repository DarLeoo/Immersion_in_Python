"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]
"""
nums = [1, 2, 3, 1, 2, 4, 5]
nums_1 = []
for num in nums:
    if nums.count(num) > 1:
        nums_1.append(num)

print(list(set(nums_1)))