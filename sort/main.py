
flag_nums = True
while flag_nums:
    flag_nums = False
    nums = input('Введите последовательность целых чисел через пробел: ').split()
    try:
        for i in nums:
            if not i.isdigit():
                raise ValueError
    except Exception:
        print("Ошибка! На ввод принимаются только целые числа, введенные через пробел!")
        flag_nums = True
    else:
        array = list(map(int, nums))

flag_num = True
while flag_num:
    flag_num = False

    try:
        element = int(input('Введите любое целое число: '))

    except Exception:
        print("Ошибка! На ввод принимается только целое число")
        flag_num = True

def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return f'Индекс эллемента перед введенным числом: {middle - 1}'
    elif element < array[middle]:

        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


array.append(element)
qsort(array, 0, len(array) - 1)
print(array)
print(binary_search(array, element, 0, len(array) - 1))
