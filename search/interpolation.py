def interpolation(iter, key):
    l = 0
    r = len(iter) - 1
    while iter[l] < key and iter[r] > key:
        if iter[r] == iter[l]:
            break
        index = (key - iter[l])*(l - r)//(iter[l] - iter[r]) + l
        if iter[index] > key:
            r = index - 1
        elif iter[index] < key:
            l = index + 1
        else:
            return True
    if iter[l] == key:
        return True
    if iter[r] == key:
        return True
    return False

if __name__ == "__main__":
    print(interpolation([-2, 0, 3, 5, 7, 9, 11, 15, 18], -9))
