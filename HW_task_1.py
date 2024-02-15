"""
 Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
 В результирующем списке не должно быть дубликатов.
"""
my_list = [3, 34, 23, 3, 3454, 5, 1, 3, 2, 1, 5]
new_list = []
for item in my_list:
    if item not in new_list:
        if my_list.count(item) > 1:
            new_list.append(item)
print(new_list)
