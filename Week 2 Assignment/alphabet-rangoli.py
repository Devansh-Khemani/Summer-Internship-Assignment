import string
def print_rangoli(size):
    alpha = string.ascii_lowercase
    width = 4 * size - 3
    for i in range(size):
        left_part = alpha[size-1:size-1-i:-1]
        middle = alpha[size-1-i]
        right_part = alpha[size-i:size]
        row = '-'.join(left_part + middle + right_part)
        print(row.center(width, '-'))
    for i in range(size-2, -1, -1):
        left_part = alpha[size-1:size-1-i:-1]
        middle = alpha[size-1-i]
        right_part = alpha[size-i:size]
        row = '-'.join(left_part + middle + right_part)
        print(row.center(width, '-'))
