import itertools
import math

# Task 1: Number Generator
def generate_numbers(numbers):
    for num in numbers:
        yield num

# Task 2: Even Number Generator
def generate_even_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num

# Task 3: Odd Number Generator
def generate_odd_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            yield num

# Task 4: Fibonacci Generator
def generate_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Task 5: Prime Number Generator
def generate_primes(limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

# Task 6: Pre-order Traversal of a Binary Tree
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def traverse_pre_order(root):
    if root:
        yield root.value
        yield from traverse_pre_order(root.left)
        yield from traverse_pre_order(root.right)

# Task 7: In-order Traversal of a Binary Tree
def traverse_in_order(root):
    if root:
        yield from traverse_in_order(root.left)
        yield root.value
        yield from traverse_in_order(root.right)

# Task 8: Post-order Traversal of a Binary Tree
def traverse_post_order(root):
    if root:
        yield from traverse_post_order(root.left)
        yield from traverse_post_order(root.right)
        yield root.value

# Task 9: DFS Traversal of a Graph
def traverse_dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            yield node
            visited.add(node)
            stack.extend(reversed(graph[node]))

# Task 10: BFS Traversal of a Graph
def traverse_bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            yield node
            visited.add(node)
            queue.extend(graph[node])

# Task 11: Dictionary Keys Generator
def generate_dict_keys(d):
    for key in d.keys():
        yield key

# Task 12: Dictionary Values Generator
def generate_dict_values(d):
    for value in d.values():
        yield value

# Task 13: Dictionary Items Generator
def generate_dict_items(d):
    for item in d.items():
        yield item

# Task 14: File Lines Generator
def generate_file_lines(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Task 15: File Words Generator
def generate_file_words(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                yield word

# Task 16: String Characters Generator
def generate_string_chars(s):
    for char in s:
        yield char

# Task 17: Unique Elements Generator
def generate_unique_elements(lst):
    seen = set()
    for elem in lst:
        if elem not in seen:
            seen.add(elem)
            yield elem

# Task 18: Reverse List Generator
def generate_reversed_list(lst):
    for elem in reversed(lst):
        yield elem

# Task 19: Cartesian Product Generator
def generate_cartesian_product(lst1, lst2):
    for elem1 in lst1:
        for elem2 in lst2:
            yield (elem1, elem2)

# Task 20: Permutations Generator
def generate_permutations(lst):
    for perm in itertools.permutations(lst):
        yield perm

# Task 21: Combinations Generator
def generate_combinations(lst):
    for r in range(1, len(lst) + 1):
        for comb in itertools.combinations(lst, r):
            yield comb

# Task 22: Tuple List Generator
def generate_tuple_list(lst):
    for tup in lst:
        yield tup

# Task 23: Parallel Lists Generator
def generate_parallel_lists(*lists):
    for elems in zip(*lists):
        yield elems

# Task 24: Flatten List Generator
def generate_flatten_list(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from generate_flatten_list(item)
        else:
            yield item

# Task 25: Nested Dictionary Generator
def generate_nested_dict(d):
    for key, value in d.items():
        if isinstance(value, dict):
            yield from generate_nested_dict(value)
        else:
            yield (key, value)

# Task 26: Powers of Two Generator
def generate_powers_of_two(n):
    for i in range(n + 1):
        yield 2 ** i

# Task 27: Powers of Base Generator
def generate_powers_of_base(base, limit):
    power = 1
    while power <= limit:
        yield power
        power *= base

# Task 28: Squares Generator
def generate_squares(start, end):
    for num in range(start, end + 1):
        yield num ** 2

# Task 29: Cubes Generator
def generate_cubes(start, end):
    for num in range(start, end + 1):
        yield num ** 3

# Task 30: Factorials Generator
def generate_factorials(n):
    for i in range(n + 1):
        yield math.factorial(i)

# Task 31: Collatz Sequence Generator
def generate_collatz_sequence(n):
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    yield 1

# Task 32: Geometric Progression Generator
def generate_geometric_progression(initial, ratio, limit):
    term = initial
    while term <= limit:
        yield term
        term *= ratio

# Task 33: Arithmetic Progression Generator
def generate_arithmetic_progression(initial, difference, limit):
    term = initial
    while term <= limit:
        yield term
        term += difference

# Task 34: Running Sum Generator
def generate_running_sum(numbers):
    total = 0
    for number in numbers:
        total += number
        yield total

# Task 35: Running Product Generator
def generate_running_product(numbers):
    product = 1
    for number in numbers:
        product *= number
        yield product
