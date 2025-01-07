import pandas as pd

list1 = [1, 2, 3, 2, 3, 1]
list2 =[]
print(list(x for x in list1 if x not in list2))



# list2 = []
# for ele in list1:
#     if ele not in list2:
#         list2.append(ele)
# print(list2)