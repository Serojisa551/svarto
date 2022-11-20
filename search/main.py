import search_algorithms as search


if __name__ == "__main__":
    print(search.binary([1, 2, 3, 5], 4))
    print(search.exponential([1, 2, 3, 5], 1))
    print(search.interpolation([1, 2, 3, 5], 4))
    print(search.jump([1, 2, 3, 5], 2, 4))
    print(search.linear([1, 2, 3, 5], 4))
    print(search.ternary([1, 2, 3, 5], 5))
