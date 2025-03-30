# 5. Question: Write a function to flatten a nested list.

from collections.abc import Iterable

def add_items(item):
    global out_list
    if isinstance(item, Iterable):
        for each in item:
            add_items(each)
    else:
        out_list.append(item)
    return out_list


my_list = [1, 5, [2, [3, 7, 9]], (89, 12)]
out_list = []

for item in my_list:
    add_items(item)
# print(type(item))

print(out_list)