from linear import my_print, linear


def jump(iter, quntity, key):
    for i in range(quntity - 1, len(iter), quntity):
        if iter[i] == key:
            return True
        elif iter[i] > key:
            return linear(iter[i-quntity: i], key)
    else:
        my_print(linear(iter[i:], key))


if __name__ == "__main__":
    my_print(jump([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
