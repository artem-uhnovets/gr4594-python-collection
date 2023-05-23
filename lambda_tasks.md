___
Напишите программу на Python для создания функции, которая принимает один аргумент, и этот аргумент будет умножен на неизвестное заданное число.
Принимаемый аргумент должен быть один, поэтому лучше использовать функцию в функции.

<details>
<summary>SPOILER! </summary>

```python
def func_compute(n):
    return lambda x : x * n
result = func_compute(3)
print(result(15))

```

</details>

___
Напишите программу на Python для сортировки списка кортежей с помощью лямбды.

```python
# Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

```
<details>
<summary>SPOILER! </summary>

```python
def sort_list(my_list):
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            cur_val = my_list[i]
            next_val = my_list[j]
            if cur_val[1] > next_val[1]:
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
    return my_list

def sort_tuple_in_list(sour_list):
    list_num = list(map(lambda num: num[1], sour_list))
    list_sub = list(map(lambda num: num[0], sour_list))
    list_sub2 = [list_sub[list_num.index(sorted(list_num)[i])] for i in range(len(list_sub))]
    return list(zip(list_sub2, sorted(list_num)))

tuple_1 = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(sort_tuple_in_list(tuple_1))
print(datetime.datetime.today())

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
subject_marks.sort(key = lambda x: x[1])
print(subject_marks)

```

</details>

___
Напишите программу на Python для сортировки списка словарей с помощью лямбда-выражения.

```python
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
```

<details>
<summary>SPOILER! </summary>

```python
list_dict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
             {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
             {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}]

list_dict.sort(key = lambda x: x['make'])
print(list_dict)


Write a Python program to filter a list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]

list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 0, list_num)))
print(list(filter(lambda x: x % 2 != 0, list_num)))
print([i for i in list_num if i % 2 == 0])
print([i for i in list_num if i % 2 != 0])
```
</details>

___
Напишите программу на Python, чтобы определить, начинается ли данная строка с заданного символа, используя Лямбда.

Пример вывода:

True

False

<details>
<summary>SPOILER! </summary>

```python
starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Python'))
starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Java'))
```
</details>

___
Напишите программу на Python для извлечения года, месяца, даты и времени с помощью лямбды.

```python
# Sample Output:
# 2020-01-15 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178
```
<details>
<summary>SPOILER! </summary>

```python
import datetime
now = datetime.datetime.now()
print(now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))
```

</details>

___
Напишите программу на Python, чтобы проверить, является ли данная строка числом или нет, используя Лямбда.

<details>
<summary>SPOILER! </summary>

```python
is_num = lambda q: q.replace('.','',1).isdigit()
print(is_num('26587'))
print(is_num('4.2365'))
print(is_num('-12547'))
print(is_num('00'))
print(is_num('A001'))
print(is_num('001'))
print("\nPrint checking numbers:")
is_num1 = lambda r: is_num(r[1:]) if r[0]=='-' else is_num(r)
print(is_num1('-16.4'))
print(is_num1('-24587.11'))
```

</details>

___
Напишите программу на Python для создания рядов Фибоначчи до n с использованием Лямбды.
```python
Fibonacci series upto 2:
[0, 1]
Fibonacci series upto 5:
[0, 1, 1, 2, 3]
Fibonacci series upto 6:
[0, 1, 1, 2, 3, 5]
Fibonacci series upto 9:
[0, 1, 1, 2, 3, 5, 8, 13, 21]
```
<details>
<summary>SPOILER! </summary>

```python
def fibo_func(num):
    if num == 2:
        return 1
    if num <= 1:
        return 0
    return fibo_func(num - 1) + fibo_func(num - 2)

# 1
fibo_list_lambda_1 = lambda len: [fibo_func(i) for i in range(1, len + 1)]
print(fibo_list_lambda_1(9))
# 2
fibo_list_lambda_2 = lambda len: list(map(fibo_func, range(1, len + 1)))
print(fibo_list_lambda_2(9))
# 3
range_list = lambda len: [i for i in range(1, len + 1)]
fibo_list_lambda_3 = lambda len: [fibo_func(i) for i in range_list(len)]
print(fibo_list_lambda_3(9))

fibo_list_lambda_4 = lambda len: list(map(fibo_func, range_list(len)))
print(fibo_list_lambda_4(9))

# 4
from functools import reduce
 
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
 
print("Fibonacci series upto 2:")
print(fib_series(2))
print("\nFibonacci series upto 5:")
print(fib_series(5))
print("\nFibonacci series upto 6:")
print(fib_series(6))
print("\nFibonacci series upto 9:")
print(fib_series(9))
```
</details>

___
Напишите программу на Python, чтобы найти пересечение двух заданных массивов с помощью лямбды.
```python
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
[1, 2, 4, 8, 9]
Intersection of the said arrays: [1, 2, 8, 9]
```
<details>
<summary>SPOILER! </summary>

```python
list_1 = [1, 2, 3, 5, 7, 8, 9, 10]
list_2 = [1, 2, 4, 8, 9]
list_intersec_lambda = lambda x, y: list(set(x).intersection(set(y)))
print(list_intersec_lambda(list_1, list_2))
```
</details>

___
Напишите программу на Python для перестановки положительных и отрицательных чисел в заданном массиве с помощью лямбда-выражения.
```python
Original arrays:
[-1, 2, -3, 5, 7, 8, 9, -10]
Rearrange positive and negative numbers of the said array:
[2, 5, 7, 8, 9, -10, -3, -1]
```
<details>
<summary>SPOILER! </summary>

```python
my_list = [-1, 2, -3, 5, 7, 8, 9, -10]
positive_list = lambda array: sorted(list(filter(lambda num: num >= 0, array)))
negative_list = lambda array: sorted(list(filter(lambda num: num < 0, array)), reverse=False)
my_list = positive_list(my_list) + negative_list(my_list)
print(my_list)

array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)
print(result)
```

</details>

___
Напишите программу на Python для подсчета четных и нечетных чисел в заданном массиве целых чисел с использованием лямбды.
```python
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
Number of even numbers in the above array: 3
Number of odd numbers in the above array: 5
```
<details>
<summary>SPOILER! </summary>

```python
list_nums = [1, 2, 3, 5, 7, 8, 9, 10]
even_nums = lambda array: len(list(filter(lambda even: even % 2 == 0, array)))
print(even_nums(list_nums))
print(len(list_nums) - even_nums(list_nums))
```

</details>

___
Напишите программу на Python для фильтрации заданного списка, чтобы определить, имеют ли значения в списке длину 6, используя лямбда.
```python
# Sample Output:
# Monday
# Friday
# Sunday
```
<details>
<summary>SPOILER! </summary>

```python
days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
list_filter_1 = lambda l: list(filter(lambda val: len(val) <= l, days_list))
list_filter_2 = lambda l: [i for i in days_list if len(i) <= l]
print(*list_filter_1(7))
print(*list_filter_2(6))
```

</details>

___
Напишите программу на Python для суммирования двух заданных списков, используя map и lambda.
```python
Original list:
[1, 2, 3]
[4, 5, 6]
Result: after adding two list
[5, 7, 9]
```
<details>
<summary>SPOILER! </summary>

```python
def summ_lists(l_1, l_2):
    return l_1 + l_2

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = list(map(summ_lists, list_1, list_2))
list_4 = list(map(lambda a, b: a + b, list_1, list_2))
print(list_3)
print(list_4)
```

</details>

___
Напишите программу на Python, чтобы найти числа, кратные девятнадцати или тринадцати, из списка чисел, используя лямбду.
```python
Orginal list:
[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
Numbers of the above list divisible by nineteen or thirteen:
[19, 65, 57, 39, 152, 190]
```
<details>
<summary>SPOILER! </summary>

```python
origin_list = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
modif_list_1 = lambda array: [i for i in array if i % 13 == 0 or i % 19 == 0]
print(modif_list_1(origin_list))
modif_list_2 = list(filter(lambda x: (x % 13 == 0 or x % 19 == 0), origin_list))
print(modif_list_2)
```

</details>

___
Напишите программу на Python для поиска палиндромов в заданном списке строк с использованием лямбда-выражения.
```python
Orginal list of strings:
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
List of palindromes:
['php', 'aaa']
```
<details>
<summary>SPOILER! </summary>

```python
origin_list = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa', 'phhp']
modif_list = list(filter(lambda val: val[:len(val)//2] == (val[len(val)//2 + 1:] if len(val) % 2 != 0 else val[len(val)//2:]), origin_list))
print(modif_list)

texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
result = list(filter(lambda x: (x == "".join(reversed(x))), texts)) 
print(result)
```

</details>

___
Напишите программу на Python, чтобы найти числа в заданной строке и сохранить их в виде списка.
После этого отобразите числа, длина которых превышает длину списка, в отсортированном виде.
Используйте лямбда-функцию для решения проблемы.
```python
# Original string:
"sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
# Numbers in sorted form:
20 23 56
```
<details>
<summary>SPOILER! </summary>

```python
origin_str = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
num_list = list(filter(lambda val: val.isdigit(), origin_str.split(" ")))
print(*sorted(list(filter(lambda val: int(val) > len(num_list), num_list))))
```

</details>

___
Напишите программу на Python, которая суммирует длину списка имен после удаления
тех, которые начинаются со строчных букв. Используйте лямбда-функцию.
```python
# Result:
16
```
<details>
<summary>SPOILER! </summary>

```python
sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
filter_name_1 = list(filter(lambda val: val[0].isupper(), sample_names))
filter_name_2 = [len(x) for x in sample_names if x[0].isupper()]

print(len(''.join(filter_name_1)))
print(sum(filter_name_2))
```

</details>

___
Напишите программу на Python для вычисления суммы положительных и отрицательных чисел из заданного списка чисел, используя лямбда-функцию.
```python
Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
Sum of the positive numbers: -32
Sum of the negative numbers: 48
```
<details>
<summary>SPOILER! </summary>

```python
nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
total_negative_nums = list(filter(lambda nums: nums < 0,nums))
total_positive_nums = list(filter(lambda nums: nums > 0,nums))
print(sum(total_negative_nums))
print(sum(total_positive_nums))
```

</details>

___

