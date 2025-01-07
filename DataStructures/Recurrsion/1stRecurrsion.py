def print_numbers(i, n):
    if i > n:
        return
    print_numbers(i+1, n)
    print(i)

if __name__ == '__main__':
    print_numbers(1, 4)