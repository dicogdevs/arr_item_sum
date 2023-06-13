# Array Item Sum - Recursive Implementation
This project presents an optimized Python function that calculates the sum of all elements in a list using recursion. This approach demonstrates the concept of recursion in Python with a divide-and-conquer strategy. Due to Python's recursion limit, caution should be used when dealing with large lists.

## Function
Here's the core function of the project:

```python
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
```

## Usage
To use the function, simply call it with a list of numbers as the argument:

```python
numbers = [1, 2, 3, 4, 5]
print(arr_item_sum(numbers))  # Outputs: 15
```

## Limitations
This implementation uses recursion, and Python has a limit to the recursion depth (typically 1000). Therefore, this function may result in a RecursionError for larger lists.

For list lengths close to or exceeding this limit, it's recommended to use an iterative approach or Python libraries optimized for large computations, like numpy.

## Contributing
Feel free to fork this project and add your own features or improvements.