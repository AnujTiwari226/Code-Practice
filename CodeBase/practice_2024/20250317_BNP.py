# # a = {x : x**2 for x in range(10)}
# # b = {x : x**2 for x in range(10)}
# #
# # c = a
# #
# # *args = ()
# #
# # print(a is b)
# # print(a is c)
# # import time
# #
# #
# # def my_deco(func):
# #     def wrapper(*args):
# #         start_time = time.time()
# #         func(*args)
# #         end_time = time.time()
# #         print(f"total time taken is  - {end_time - start_time}")
# #     return wrapper
# #
# # @my_deco
# # def add(*args):
# #     a, b, c, d = args
# #     time.sleep(10)
# #     print("Hey Add")
# #
# # add(1, 2, 3, 4)
# import pandas as pd
#
# a = {f'col_{x}' : x**2 for x in range(10)}
# print(a)
# df = pd.DataFrame(data=a, columns=list(a.keys()), index=list(a.keys()))
#
#
# # print(df.loc['col_0']['col_1'])
# df.drop(columns=['col_0'], inplace=True)
#
# df['res'] = df[df['col_8']==64]['col_8']
# print(df)

# second largest ele -

def slargest(arr):
    maxl = float('-inf')
    secondm = float('-inf')

    for num in arr:
        if num >= maxl:
            maxl = num
        if num >= secondm and num != maxl:
                secondm = maxl
    return secondm if secondm != float('-inf') else -1


print(slargest([1, 1, 1,1, 1]))