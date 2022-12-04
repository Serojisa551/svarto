def binary(ite, key):
    length = len(ite)
    index = len(ite) - 1
    bottom_line = 0
    middle = (bottom_line + index) // 2
    while length > 0:
        if length == 1:
            if ite[middle] == key:
                return True
            else:
                return False
        elif ite[middle] == key:
            return True
        else:
            if ite[middle] > key:
                index = middle - 1
            elif ite[middle] < key:
                bottom_line = middle + 1
        middle = (bottom_line + index) // 2
        length //= 2


def exponential(iter, key):
    border = 1
    while border <= len(iter) - 1:
        if iter[border] == key:
            return True
        elif key > iter[border]:
            border *= 2
        else:
            return binary(iter[border // 2 : border], key)
    else:
        return False


def interpolation(iter, key):
    l = 0
    r = len(iter) - 1
    while iter[l] < key and iter[r] > key:
        if iter[r] == iter[l]:
            break
        index = (key - iter[l]) * (l - r) // (iter[l] - iter[r]) + l
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


def jump(iter, jump_quntity, key):
    for i in range(jump_quntity - 1, len(iter), jump_quntity):
        if iter[i] == key:
            return True
        elif iter[i] > key:
            return linear(iter[i - jump_quntity : i], key)
    else:
        return linear(iter[i:], key)


def linear(ite, key):
    for element in ite:
        if key == element:
            return True
    else:
        return False


def ternary(iter, key):
    l = 0
    r = len(iter) - 1
    while l < r:
        h = r - l // 3
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
