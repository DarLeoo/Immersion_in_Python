"""
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""

nums = [1, 2, 3, 4, 5, 6]

index_num_start = 0
index_num_end = 9


def sum_of_index(nums:list, num_start:int, num_end:int):
    start, end = sorted([num_start, num_end])
    start = max(0, 0 if start > len(nums) else start)
    end = min(len(nums), end)
    return sum(nums[start:end+1])


print(sum_of_index(nums, index_num_start, index_num_end))

