def merge_sort(ar):
    return merge_sort_recursion(ar, 0, len(ar) - 1)


def merge_sort_recursion(ar, start, end_inclusive):
    if start == end_inclusive:
        # that's why MEMORY complexity O(n)
        return [ar[start]]

    middle = start + (end_inclusive - start) // 2
    left = merge_sort_recursion(ar, start, middle)
    right = merge_sort_recursion(ar, middle + 1, end_inclusive)
    merged = merge_parts(left, right)
    return merged


def merge_parts(left, right):
    i = 0
    j = 0
    result = []

    while i < len(left) or j < len(right):
        if i == len(left):
            # only elements in the right array left
            while j < len(right):
                result.append(right[j])
                j = j + 1
            continue

        if j == len(right):
            # only elements in the left array left
            while i < len(left):
                result.append(left[i])
                i = i + 1
            continue

        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    return result


if __name__ == '__main__':
    print('hello')
    a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    b = [19, 12, 10, 0, 18, 1, 5, 9]

    a_sorted = merge_sort(a)
    print(a_sorted)
    b_sorted = merge_sort(b)
    print(b_sorted)
