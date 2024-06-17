import numpy as np
import re
from itertools import groupby
from math import sqrt

# Task 1: Interpolate Missing Values
def interpolate_missing(nums):
    interpolated = []
    for i, num in enumerate(nums):
        if num is None:
            left = nums[i - 1] if i > 0 else None
            right = nums[i + 1] if i < len(nums) - 1 else None
            if left is not None and right is not None:
                interpolated.append((left + right) / 2)
            elif left is not None:
                interpolated.append(left)
            elif right is not None:
                interpolated.append(right)
        else:
            interpolated.append(num)
    return interpolated

# Task 2: Fibonacci Series Generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Task 3: Batch Data Processing
def process_batches(nums, batch_size):
    return [max(nums[i:i+batch_size]) for i in range(0, len(nums), batch_size)]

# Task 4: Encode and Decode Strings
def encode_string(s):
    return ''.join(str(len(list(group))) + key for key, group in groupby(s))

def decode_string(s):
    return ''.join(s[i] * int(s[i-1]) for i in range(1, len(s), 2))

# Task 5: Matrix Rotation
def rotate_matrix(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

# Task 6: Regular Expression Search
def regex_search(strings, pattern):
    return [string for string in strings if re.match(pattern, string)]

# Task 7: Merge Sorted Arrays
def merge_sorted_arrays(arr1, arr2):
    return sorted(arr1 + arr2)

# Task 8: Prime Number Checker
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Task 9: Group by Key
def group_by_key(data, key):
    grouped = {}
    for item in data:
        grouped.setdefault(item[key], []).append(item['value'])
    return grouped

# Task 10: Remove Outliers
def remove_outliers(nums):
    mean = np.mean(nums)
    std_dev = np.std(nums)
    return [num for num in nums if abs(num - mean) <= 2 * std_dev]

