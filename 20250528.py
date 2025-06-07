# x = lambda i: i * i
#
# print(x(2))
#
def log_value(func):
    def wrapper(*args):
        print(f"wrapper {args}")
        res = func(*args)
        print(f"Square Done {res}")
        return res
    return wrapper

@log_value
def square(x):
    return x*x


# lst = [x for x in range(10)]
# lst1 = map(square, lst)
# print(type(lst1))


# def example(x):
#     for i in range(1, x):
#         yield i*i




if __name__ == '__main__':
#     lst = [1, 2, 3, 4]
#     a, b, c = [lst[x] for x in range(3)]
#     print(f'{a}, {c}')
        square(2)
#     # ex = example(10)
    # print(ex.__next__())
    # print(ex.__next__())
    # print(ex.__next__())
    # print(ex.__next__())
