def arr_item_sum(arr: list, left: int = 0, right: int = None) -> int:
    if not right:
        right = len(arr)

    if left >= right:
        return 0
    elif (right - left) == 1:
        return arr[left]
    elif (right - left) == 2:
        return arr[left] + arr[left+1]
    else:
        mid = (left + right) // 2
        return arr_item_sum(arr, left, mid) + arr[mid] + arr_item_sum(arr, mid+1, right)
