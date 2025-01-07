import functools
import time


def log_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"function {func.__name__} executed in {end_time - start_time} time")
        return result
    return wrapper


@log_time
def calculate1(n):
    return sum(range(n))


print(calculate1(1000))


def list_comp(x, y, z, n):
    mylist = []
    for i in range(x+1):

        for j in range(y + 1):
            for k in range(z + 1):
                books = [('Python Crash Course', 50), ('Clean Code', 40), ('Fluent Python', 60)]

def check():
    books = [2, 4, 5, 6, 3, 2, 1]

    # Using lambda to sort by price
    sorted_books = sorted(books, key=mysort)
    print(sorted_books)

def mysort(it):
    print("inside mysort")
    return it+10


check()