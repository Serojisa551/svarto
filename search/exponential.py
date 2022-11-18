from binary import binary

def exponential(iter, key):
    border = 1
    while border <= len(iter) - 1:
        if iter[border] == key:
            return True
        elif key > iter[border]:
            border *= 2
        else:
            return binary(iter[border//2: border],key)

if __name__ == "__main__":
    print(exponential([-2, 0, 3, 5, 7, 9, 11, 15, 18], 18))