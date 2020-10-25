def quick_sort(ar, start, end_inclusive):
    if start == end_inclusive:
        # merge sort had a return value
        return

    p = start + (end_inclusive - start) // 2  # pivot

    i = start  # iterate over elements that should be smaller
    while i <= end_inclusive:
        if (ar[i] > ar[p] and i < p) or (ar[i] < ar[p] and i > p):
            if i < p:
                swap(ar, i, p)
                p = i
            else:
                # shift all elements to the right and swap it with the element at "i"
                tmp = ar[i]
                new_p = 0
                for j in range(i - p):
                    ar[i - j] = ar[i - j - 1]
                    new_p = i - j
                ar[p] = tmp
                p = new_p

        i = i + 1

    quick_sort(ar, start, p)  # sort smaller elements
    if p < end_inclusive:
        quick_sort(ar, p + 1, end_inclusive)  # sort bigger elements


def swap(ar, i, j):
    tmp = ar[i]
    ar[i] = ar[j]
    ar[j] = tmp


if __name__ == '__main__':
    print('hello')
    a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    b = [19, 12, 10, 0, 18, 1, 5, 9]
    c = [3, 7, 0, 5, 2, 1, 9]
    d = [19, 12, 10, 16, 18, 1, 5, 9]

    quick_sort(a, 0, len(a) - 1)
    print(a)
    quick_sort(b, 0, len(b) - 1)
    print(b)
    quick_sort(c, 0, len(c) - 1)
    print(c)
    quick_sort(d, 0, len(d) - 1)
    print(d)
