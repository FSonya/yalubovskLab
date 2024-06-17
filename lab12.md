Звіт за лабораторну роботу №12: Робота з матрицями у Python

Мета роботи:
Ознайомитися з поняттям матриці та її представленням у вигляді двовимірного списку в Python. Навчитися створювати об'єкти класу Matrix для роботи з матрицями. Реалізувати методи для додавання елементів, транспонування, множення, перевірки симетричності, обертання, перетворення в список та інших операцій над матрицями.

Опис завдання:
Створення класу Matrix:

Конструктор __init__(self, rows, columns): ініціалізує матрицю розміром rows x columns, заповнену нулями.
Додавання елементів: метод add_element(self, row, col, value) додає елемент value у позицію (row, col). Виняток IndexError генерується, якщо індекси виходять за межі матриці.
Сума рядків: метод sum_of_rows(self) повертає список, що містить суми елементів кожного рядка матриці.
Транспонування матриці: метод transpose(self) повертає новий об'єкт Matrix, який є транспонованою матрицею (рядки та стовпці поміняні місцями).
Множення матриць: метод multiply_by(self, other_matrix) приймає інший об'єкт Matrix і повертає новий об'єкт Matrix, який є результатом їх множення. Виняток ValueError генерується, якщо матриці несумісні для множення.
Перевірка симетричності: метод is_symmetric(self) перевіряє, чи є матриця квадратною та симетричною відносно головної діагоналі.
Обертання матриці: метод rotate_right(self) обертає матрицю на 90 градусів за годинниковою стрілкою.
Перетворення в список: метод flatten(self) повертає одновимірний список, що містить усі елементи матриці.
Створення матриці зі списку списків: статичний метод from_list(list_of_lists) створює об'єкт Matrix з переданого списку списків.
Вилучення діагоналі: метод diagonal(self) повертає список елементів головної діагоналі квадратної матриці.
Виконання роботи:
Створення об'єктів класу Matrix:
Створено об'єкти matrix, matrix1, matrix2, matrix3, matrix4, matrix5, matrix6 різних розмірів.

Додавання елементів:
Використано метод add_element для додавання елементів у матриці.

Сума рядків:
Використано метод sum_of_rows для обчислення суми елементів кожного рядка.

Транспонування:
Використано метод transpose для отримання транспонованої матриці.

Множення матриць:
Використано метод multiply_by для множення матриць.

Перевірка симетричності:
Використано метод is_symmetric для перевірки симетричності матриці.

Обертання матриці:
Використано метод rotate_right для обертання матриці.

Перетворення в список:
Використано метод flatten для перетворення матриці в список.

Створення матриці зі списку списків:
Використано статичний метод from_list для створення матриці зі списку списків.

Вилучення діагоналі:
Використано метод diagonal для отримання діагоналі квадратної матриці.

Результати:
В результаті виконання коду отримано очікувані результати для всіх операцій над матрицями: додавання елементів, транспонування, множення, перевірка симетричності, обертання, перетворення в список, створення зі списку списків та вилучення діагоналі.

Висновки:
У цій лабораторній роботі ми успішно реалізували клас Matrix для роботи з матрицями в Python. Ми ознайомились з основними операціями над матрицями, такими як додавання елементів, транспонування, множення матриць та іншими операціями, що дозволяють ефективно працювати з двовимірними даними. Реалізація таких функцій не лише полегшує обробку матричних даних, а й забезпечує їхню швидкість та надійність у різних завданнях обчислень та моделювання.