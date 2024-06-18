import re

def clean_data(data):
    if isinstance(data, str):
        data = data.split(',')
    cleaned_list = [item.strip().lower() for item in data]
    print("Task 1:", cleaned_list)
    return cleaned_list

def filter_emails(emails_string):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    valid_emails = [email for email in re.findall(email_pattern, emails_string) if email.count('@') == 1]
    print("Task 2:", valid_emails)
    return valid_emails

def extract_keywords(words, min_length):
    keywords = [word for word in words.split() if len(word) > min_length]
    print("Task 3:", keywords)
    return keywords

def process_text(text):
    processed_list = [item.strip().lower().strip('.?!') for item in text.split(',') if item.strip()]
    print("Task 4:", processed_list)
    return processed_list

def normalize_data(numbers):
    numbers_list = [float(num) for num in numbers.split(',')]
    max_num = max(numbers_list)
    normalized_list = [round(num / max_num, 3) for num in numbers_list]
    print("Task 5:", normalized_list)
    return normalized_list

def concatenate_strings(data, delimiter):
    concatenated_str = ''.join(data.split(delimiter))
    print("Task 6:", concatenated_str)
    return concatenated_str

def sum_numeric_strings(numbers):
    numeric_values = list(map(int, re.findall(r'\d+', numbers)))
    total_sum = sum(numeric_values)
    print("Task 7:", total_sum)
    return total_sum

def filter_numbers(input_string, threshold):
    numbers = list(map(int, re.findall(r'\d+', input_string)))
    filtered_numbers = [num for num in numbers if num > threshold]
    print("Task 8:", filtered_numbers)
    return filtered_numbers

def map_to_squares(numbers):
    squared_numbers = [int(num) ** 2 for num in numbers.split(',')]
    print("Task 9:", squared_numbers)
    return squared_numbers

def reverse_strings(words):
    reversed_list = [word[::-1] for word in words.split(',')]
    print("Task 10:", reversed_list)
    return reversed_list

# Test the functions
data = " Apple,  Banana , orange "
cleaned_data = clean_data(data)

emails = "mail us test@example.com and invalid-email.com.djwd with example@test.co"
valid_emails = filter_emails(emails)

words = "apple pear banana kiwi"
filtered_words = extract_keywords(words, 4)

texts = "Hello! , Yes? , No. , "
processed_texts = process_text(texts)

numbers = "10, 20, 30, 40, 50"
normalized_numbers = normalize_data(numbers)

data_to_concatenate = "Hello, World!, How, are, you?"
separator = ","
concatenated_data = concatenate_strings(data_to_concatenate, separator)

numeric_strings = "10, 20, abc, 30, def, 40"
sum_of_numeric_strings = sum_numeric_strings(numeric_strings)

numbers_to_filter = "10, 20, abc, 30, def, 40"
threshold = 25
filtered_numbers = filter_numbers(numbers_to_filter, threshold)

numbers_to_square = "1, 2, 3, 4, 5"
squared_numbers = map_to_squares(numbers_to_square)

strings_to_reverse = "apple, banana, orange, PEAR, kiwi"
reversed_strings = reverse_strings(strings_to_reverse)
