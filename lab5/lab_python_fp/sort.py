data = [4, -30, 100, -100, 123, 1, 0, -1, -4]


def sort_abs(list_f: list) -> list:
    return sorted(list_f, key=lambda x: abs(x), reverse=True)

def sort_abs1(list_f: list) -> list:
    return sorted(data, key=abs, reverse=True)

if __name__ == '__main__':
    result = sorted(data, key=lambda x: abs(x), reverse=True)
    print(result)

    result_with_lambda = sorted(data, key=abs, reverse=True)
    print(result_with_lambda)