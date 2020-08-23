def insert_sort(sort_list):
    """Сортировка списка вставками"""
    n = len(sort_list)
    for top in range(1, n):
        k = top
        while k > 0 and sort_list[k - 1] > sort_list[k]:
            sort_list[k], sort_list[k - 1] = sort_list[k - 1], sort_list[k]
            k -= 1


def choise_sort(sort_list):
    """Сортировка списка выбором"""

    n = len(sort_list)
    for pos in range(0, n - 1):
        for k in range(pos + 1, n):
            if sort_list[k] < sort_list[pos]:
                sort_list[k], sort_list[pos] = sort_list[pos], sort_list[k]


def bubble_sort(sort_list):
    """Сортировка списка методом пузырьков"""

    n = len(sort_list)
    for bypass in range(1, n):
        for k in range(0, n - bypass):
            if sort_list[k] > sort_list[k + 1]:
                sort_list[k], sort_list[k + 1] = sort_list[k + 1], sort_list[k]


def test_sort(sort_algorithm):
    print("#testcase #1: ", end='')
    array = [4, 2, 5, 1, 3]
    array_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(array)

    print('OK' if array == array_sorted else 'Fail')
    print(array)


def test_sort_2(sort_algorithm):
    print("#testcase #2: ", end='')
    array = list(range(10, 20)) + list(range(0, 10))
    array_sorted = list(range(20))
    sort_algorithm(array)

    print('OK' if array == array_sorted else 'Fail')
    print(array)


def test_sort_3(sort_algorithm):
    print("#testcase #3: ", end='')
    array = [4, 2, 5, 1, 4, 3]
    array_sorted = [1, 2, 3, 4, 4, 5]
    sort_algorithm(array)

    print('OK' if array == array_sorted else 'Fail')
    print(array)


if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort_2(choise_sort)
    test_sort_3(bubble_sort)
