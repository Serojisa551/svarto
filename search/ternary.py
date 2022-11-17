def ternary(iter, key):
    l = 0
    r = len(iter) - 1
    while l < r:
        h = (r-l//3)
        m1 = l + h
        m2 = r - h
        if key == iter[m1]:
            return True
        if key == iter[m2]:
            return True
        if iter[m1] < key < iter[m2]:
            l = m1 + 1
            r = m2 - 1
        elif key < iter[m1]:
            r = m1 - 1
        else:
            l = m2 + 1
    return False


if __name__ == "__main__":
    print(ternary([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
