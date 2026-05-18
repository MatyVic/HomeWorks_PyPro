
# Рядки
# Напишіть функцію, яка приймає рядок і повертає його довжину
def string_len(str):
    return len(str)


# Створіть функцію, яка приймає два рядки і повертає об'єднаний рядок
def string_add(str1, str2):
    return str1 + str2


# Числа
# Реалізуйте функцію, яка приймає число і повертає його квадрат.
def square_number(num):
    return num ** 2


# Створіть функцію, яка приймає два числа і повертає їхню суму.
def nums_add(num1, num2):
    return num1 + num2


# Створіть функцію яка приймає 2 числа типу int,
# виконує операцію ділення та повертає чілу частину і залишок.
def nums_div(num1, num2):
    whole_part = num1 // num2
    left_part = num1 % num2
    return whole_part, left_part


# Cписки
# Напишіть функцію для обчислення середнього значення списку чисел.
def average_list(nums):
    return sum(nums) / len(nums)


# Реалізуйте функцію, яка приймає два списки і повертає список, який містить
# спільні елементи обох списків.
def contains_list(nums1, nums2):
    return list(set(nums1) & set(nums2))


# Словники
# Створіть функцію, яка приймає словник і виводить всі ключі цього словника.
def get_dict_keys(dict):
    return list(dict.keys())


# Реалізуйте функцію, яка приймає два словники і повертає
# новий словник, який є об'єднанням обох словників.
def add_dict(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict


# Множини
# Напишіть функцію, яка приймає дві множини і повертає їхнє об'єднання.
def union_sets(set1, set2):
    return set1.union(set2)


# Створіть функцію, яка перевіряє, чи є одна множина підмножиною іншої.
def intersection_sets(set1, set2):
    return set1.issubset(set2)


# Умовні вирази та цикли
# Реалізуйте функцію, яка приймає число і виводить
# "Парне", якщо число парне, і "Непарне", якщо непарне
def check_num(num1):
    return "Парне" if num1 % 2 == 0 else "Непарне"


# Створіть функцію, яка приймає список чисел і повертає новий список,
# що містить тільки парні числа.
def get_new_lst(lst1):
    return [n for n in lst1 if n % 2 == 0]


# Рядки
print("Рядки")
print(string_len("Привіт"))
print(string_add("Hello, ", "World!"))

# Числа
print("Числа")
print(square_number(5))
print(nums_add(10, 15))
print(nums_div(17, 5))

# Списки
print("Списки")
print(average_list([1, 2, 3, 4, 5]))
print(contains_list([1, 2, 3], [2, 3, 4]))

# Словники
print("Словники")
print(get_dict_keys({"a": 1, "b": 2}))
print(add_dict({"x": 1}, {"y": 2}))

# Множини
print("Множини")
print(union_sets({1, 2}, {2, 3}))
print(intersection_sets({1, 2}, {1, 2, 3}))

# Умовні вирази та цикли
print("Умовні вирази та цикли")
print(check_num(4))
print(check_num(7))
print(get_new_lst([1, 2, 3, 4, 5, 6]))

# Лямбда вирази
# Написати лямбда-функцію визначальну парне/непарне

print("Лямбда вирази")
print((lambda n: "Парне" if n % 2 == 0 else "Непарне")(10))
print((lambda n: "Парне" if n % 2 == 0 else "Непарне")(11))
