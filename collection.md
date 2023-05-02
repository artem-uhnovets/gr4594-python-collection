# КОЛЛЕКЦИЯ МЕТОДОВ И ФУНКЦИЙ **Python**

## [ОГЛАВЛЕНИЕ](#оглавление) 

<details>
<summary>click to open </summary>

* [Тернарный оператор](#тернарный-оператор)
* [Моржовый оператор](#моржовый-оператор)
* [Оператор вывода данных](#оператор-вывода-данных)
* [Объявление переменной](#объявление-переменной)
* [Как сделать комментарий?](#как-сделать-комментарий)
* [Команды для работы со строками](#команды-для-работы-со-строками)
* [Срезы строк](#срезы-строк)
* [Интерполяция](#интерполяция)
* [Округление числа](#округление-числа)
* [Таблица списки кортежи множества словари](#таблица-списки-кортежи-множества-словари)
* [Списки](#списки)
* [Генерация списка - примеры](#генерация-списка-примеры-записи)
* [Методы списка](#методы-списка)
* [Срез списка](#срез-списка)
* [Кортежи](#кортежи)
* [Словари](#словари)
* [Множества](#множества)
* [Рекурсия](#рекурсия)
* [Функции all() any() zip() enumerate() filter() map()](#функции-all-any-zip-enumerate-filter-map)
    * [map (function, iterable)](#mapfunction-iterable)
    * [filter (function, iterable)](#filterfunction-iterable)
    * [all (iterable)](#alliterable)
    * [any (iterable)](#anyiterable)
    * [zip (interable1, interable2, interable3, …)](#zipinterable1-interable2-interable3)
    * [enumerate (iterable, start=0)](#enumerateiterable-start0)
</details>

___
### [Тернарный оператор](#тернарный-оператор)
##### [оглавление](#оглавление)
```python
res = 'Yes' if ((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0) else 'No'

print('yes' if (k < m * n) and (k >= m or k >= n) and (k % m == 0 or k % n == 0) else 'no')

countMin = count_1 if count_1 < count_0 else count_0
```
___
### [Моржовый оператор](#моржовый-оператор)
##### [оглавление](#оглавление)
* Оператор `морж` записывается так **`:=`** и представлен в Python 3.8.
* Используется только для присваивания переменных внутри других выражений.
* Можно использовать везде — от циклов до функций генераторов списка или операторов if для обходного присваивания переменных.
```python
# пример в цикле WHILE
list = []
number = None
while number != 0:
    number = int(input("Введите число: "))
    list.append(number)
# можно записать как
while (number := int(input("Введите число: "))) != 0:   # моржовый оператор
    list.append(number)


```
___
### [Оператор вывода данных](#оператор-вывода-данных)
##### [оглавление](#оглавление)
```Python
print(var1, var2, var3)
print(var1)
```
Печать без новой строки
```Python
print(value1, value2, sep='', end='')
sep='' # разделитель для значений
end='' # аргумент по умолчанию явл чимволом новой строки
       # Способ печати без новой строки-установить end в виде пустой строки
print("I am a sentence", "I am also a sentence", sep="; ", end="")
       # I am a sentence; I am also a sentence

```

___
### [Объявление переменной](#объявление-переменной)
##### [оглавление](#оглавление)

```python
a = 1
b = 2
a, b, c = 1, "python", [1,2,3]
print(a, b, c) 

s = 'hello,'
w = "world" 
print(s, w)

```
___
### [Как сделать комментарий?](#как-сделать-комментарий)
##### [оглавление](#оглавление)
<kbd> `Ctrl` </kbd> + <kbd> `/` </kbd>
```python
# print(1)
```
<kbd> `Alt` </kbd> + <kbd> `Shift` </kbd> + <kbd> `A` </kbd>
```python
'''print(1)
print(1)
print(1)
print(1)'''
```
___
### [Команды для работы со строками](#команды-для-работы-со-строками)
##### [оглавление](#оглавление)
Возникают ситуации, когда в некоторых задачах необходимо поработать со строкой, которую ввел пользователь. Например: необходимо сделать все буквы маленькими, или поменять все буквы "ё" на "е".

```Python
text = 'СъЕШЬ ещё этих МяГкИх французских булок'
print(len(text))     # 39 Определить количество символов в строке
print('ещё' in text) # True Проверить наличие символа в строке (in)
print(text.lower())  # съешь ещё этих мягких французских булок
print(text.upper())  # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок
```
* `string.join(iterable)`

Строковый метод `join()` возвращает строку, объединяя все элементы итерации,
разделенные разделителем строк.

Метод предоставляет гибкий способ создания строк из повторяемых объектов. Он объединяет каждый элемент итерируемого объекта (например, список, строку и кортеж) с помощью разделителя строк
и возвращает объединенную строку.

```python
str_1 = "съешь ещё этих мягких французских булок, да выпей чаю"
l_str = str_1.split()
print(l_str)
# ['съешь', 'ещё', 'этих', 'мягких', 'французских', 'булок,', 'да', 'выпей', 'чаю']
string = " ".join(l_str)
print(string)
# съешь ещё этих мягких французских булок, да выпей чаю

# 2 вариант
str_empty = " "
string = str_empty.join(l_str)
print(string)
# съешь ещё этих мягких французских булок, да выпей чаю
```
### [Срезы строк](#срезы-строк)
##### [оглавление](#оглавление)
```Python
text = 'съешь ещё этих мягких французских булок'
text[startIndex, endIndex, step]
text[startIndex, endIndex]
text[index]
```
Строка представляется в виде массива символов. Значит мы можем обращаться к элементам по индексам.

Отрицательное число в индексе — счёт идет с конца строки.
```Python
text = 'съешь ещё этих мягких французских булок'
print(text[0])              # c
print(text[1])              # ъ
print(text[len(text)-1])    # к
print(text[-5])             # б
print(text[:])              # съешь ещё этих мягких французских булок
print(text[:2])             # съ
print(text[len(text)-2:])   # ок
print(text[2:9])            # ешь ещё
print(text[6:-18])          # ещё этих мягких
print(text[0:len(text):6])  # сеикакл
print(text[::6])            # сеикакл
text = text[2:9] + text[-5] + text[:2]
print(text)                 # ешь ещёбсъ
```
___
### [Интерполяция](#интерполяция)
##### [оглавление](#оглавление)

```python
a, b, s = 3, 11 ,2022
print(a, b, s)                                 # 3 11 2022
print(a, '-', b, '-', s)                       # 3 - 11 - 2022
print('{} - {} - {}'.format(a, b, s))          # 3 - 11 - 2022
print(f'first - {a} second - {b} third - {s}') # first - 3 second - 11 third - 2022
```
___
### [Округление числа](#округление-числа)
##### [оглавление](#оглавление)
`round(number, ndigits)`
— округляет число `number` до `ndigits` знаков после запятой.

По умолчанию операция проводится до нуля знаков — до ближайшего целого числа. 
```python
round(3.5)      # 4
round(3.75, 1)  # 3.8
```
Если дробная часть равна 0,5, то округляют до ближайшего четного значения.
```python
round(3.5)  # 4
round(4.5)  # 4
```
Так же можно использовать `int`
```python
int(5.9)    # 5
int(-5.77)  # -5
```
**ОКРУГЛЕНИЕ из БИБЛИОТЕКИ MATH**
Для обработки алгоритмов сначала проводят импорт модуля.
```python
import math
```
```python
math.ceil(3.25)     #  4
math.ceil(-3.25)    # -3
# Функция преобразовывает значение в большую сторону (вверх).
```
```python
math.floor(3.9)     #  3
math.floor(-2.1)    # -3
# Округление происходит в меньшую сторону (вниз).
```
```python
math.trunc(7.11)    #  7
math.trunc(-2.1)    # -2
# Функция характеризуется отбрасыванием дробной части.
```
___
### [Таблица списки кортежи множества словари](#таблица-списки-кортежи-множества-словари)
##### [оглавление](#оглавление)
|Тип коллекции|Изменяемость|Индексированность|Уникальность|Создание|
|-------------|:----------:|:---------------:|:----------:|:------:|
| [список](#списки) `list`| + | + | - | [ ], list()|
| [кортеж](#кортежи) `tuple`| - | + | - | ( ), tuple()|
| [множество](#множества) `set`| + | - | + | {elm1, elm2}, set()|
| неизменное множество `frozenset`| - | - | + | frozenset()|
| [словарь](#словари) `dict`| +элементы___ -ключи_______ +значения____ | - | +элементы___ +ключи_______ -значения____ | { }, {key: value,}, dict()|

___
### [Списки](#списки)
##### [оглавление](#оглавление)

```python
list_1 = []          # Создание пустого списка
list_2 = list()      # Создание пустого списка
list_1 = [7, 9, 11, 13, 15, 17]
```
```python
list_1 = [7, 9, 11, 13, 15, 17]
print(list_1[0])     # 7
```
```python
list_1 = list()          # создание пустого списка
for i in range(5):       # цикл выполнится 5 раз
    n = int(input())     # пользователь вводит целое число
    list_1.append(n)     # сохранение элемента в конец списка
# 1-я итерация цикла(повторение 1): n = 12, list_1 = [12]
# 2-я итерация цикла(повторение 2): n = 7,  list_1 = [12, 7]
# 3-я итерация цикла(повторение 3): n = -1, list_1 = [12, 7, -1]
# 4-я итерация цикла(повторение 4): n = 21, list_1 = [12, 7, -1, 21]
# 5-я итерация цикла(повторение 5): n = 0,  list_1 = [12, 7, -1, 21, 0]
print(list_1) # [12, 7, -1, 21, 0]
```
```python
list_1 = [7, 9, 11, 13, 15, 17]
print(len(list_1))   # 6
```
Взаимодействие цикла `for` со списком:

```python
list_1 = [12, 7, -1, 21, 0]
for i in list_1:
    print(i)             # вывод каждого элемента списка
# 1-я итерация цикла(повторение 1): i = 12
# 2-я итерация цикла(повторение 2): i = 7
# 3-я итерация цикла(повторение 3): i = -1
# 4-я итерация цикла(повторение 4): i = 21
# 5-я итерация цикла(повторение 5): i = 0
```
```python
list_1 = [12, 7, -1, 21, 0]
for i in range(len(list_1)):
    print(list_1[i])     # вывод каждого элемента списка
# 1-я итерация цикла(повторение 1): list_1[0] = 12
# 2-я итерация цикла(повторение 2): list_1[1] = 7
# 3-я итерация цикла(повторение 3): list_1[2] = -1
# 4-я итерация цикла(повторение 4): list_1[3] = 21
# 5-я итерация цикла(повторение 5): list_1[4] = 0
```
### [Генерация списка-примеры записи](#генерация-списка-примеры-записи)
##### [оглавление](#оглавление)

```python
list = []

# создаст 10 элементов со значением 0
list = [0] * 10

# создаст с 0-ми значениями в количестве введенным пользователем
list = [0] * int(input('Enter a number: '))
for i in range(len(list)):
    list[i] = random.randint(0, 9) # присвоит случайное число от 0 до 9

# с использванием моржового оператора
for i in range(len(list := [0] * int(input('Enter a number: ')))):
    list[i] = random.randint(0, 9)

# генератор списков
list = [random.randint(0, 9) for i in range(int(input('Enter a number: ')))]

# можно и так
list = [i for i in range(int(input('Enter a number: ')))]
list = [i for i in range(number)]
# возможна и более сложная конструкция
list = [i * 2 for i in range(11) if i % 2 == 0] # [0, 4, 8, 12, 16, 20]

list = [c * 3 for c in 'list' if c != 'i']      # ['lll', 'sss', 'ttt']

list = [c + d for c in 'list' if c != 'i' for d in 'spam' if d != 'a'] # ['ls', 'lp', 'lm', 'ss', 'sp', 'sm', 'ts', 'tp', 'tm']
```
___
Метод **`pop`** удаляет последний элемент из списка:
```python
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop())  # 0
print(list_1)        # [12, 7, -1, 21]
print(list_1.pop())  # 21
print(list_1)        # [12, 7, -1]
print(list_1.pop())  # -1
print(list_1)        # [12, 7]
```
Удаление конкретного элемента из списка. 

Надо указать значение индекса в качестве аргумента функции **`pop`**:
```python
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(0)) # 12
print(list_1)        # [7, -1, 21, 0] 
```
Функция `insert` - добавление элемента на нужную позицию.
```python
list_1 = [12, 7, -1, 21, 0]
print(list1.insert(2, 11))
print(list1) # [12, 7, 11, -1, 21, 0] 
```
___
### [Методы списка](#методы-списка)
##### [оглавление](#оглавление)
* `append()`: Добавляет элемент в конец списка
       
    ```python
    odd = [1, 3, 5]
    odd.append(7)
    print(odd)       # [1, 3, 5, 7]
    ```
* `extend()`: Добавляет все элементы списка в другой список
       
    ```python
    odd = [1, 3, 5]
    odd.extend([9, 11, 13])
    print(odd)       # [1, 3, 5, 9, 11, 13]
    ```
* `конкатенация` -  также можем использовать оператор **`+`** для объединения списков
    ```python
    odd = [1, 3, 5]
    print(odd + [9, 7, 5])  # [1, 3, 5, 9, 7, 5]
    print(["re"] * 3)       # ["re", "re", "re"]
    ```
* `insert()`: Вставить элемент по указанному индексу
    ```python
    odd = [1, 9]
    odd.insert(1,3)
    print(odd)       # [1, 3, 9] 
    odd[2:2] = [5, 7]
    print(odd)       # [1, 3, 5, 7, 9]
    ```
* `remove()`: Удаляет элемент из списка  
    ```python
    my_list = ['p','r','o','b','l','e','m']
    my_list.remove('p')
    print(my_list)   # ['r', 'o', 'b', 'l', 'e', 'm']
    ```
* `pop()`: Удаляет и возвращает элемент по указанному индексу 
    ```python
    my_list = ['p','r','o','b','l','e','m']
    print(my_list.pop(1))   # 'r'  
    print(my_list)          # ['p', 'o', 'b', 'l', 'e', 'm']    
    print(my_list.pop())    # 'm' без индекса удаляет последний элемент списка
    ```
* `del` - ключевое слово, может удалить один или несколько элементов, или полностью весь список
    ```python
    my_list = ['p','r','o','b','l','e','m']
    del my_list[2]   # Удаляем один элемент
    print(my_list)   # ['p', 'r', 'b', 'l', 'e', 'm']

    del my_list[1:5] # Удаляем несколько элементов
    print(my_list)   # ['p', 'm']

    del my_list      # Удаляем весь список
    print(my_list)   # # Ошибка: список не определен
    ```
* `[]` также можно удалить элементы в списке, назначив пустой список фрагменту элементов
    ```python
    my_list = ['p','r','o','b','l','e','m']

    my_list[2:3] = []       # ['p', 'r', 'b', 'l', 'e', 'm']
    print(my_list)

    my_list[2:5] = []
    print(my_list)          # ['p', 'r', 'm']
    ```
* `clear()`: Удаляет все элементы из списка 
    ```python
    my_list = ['p','r','o','b','l','e','m']
    my_list.clear()   
    print(my_list)   # []
    ```
* `index()`: Возвращает индекс первого соответствующего элемента   
    ```python
    my_list = [3, 8, 1, 6, 0, 8, 4]
    print(my_list.index(8)) # 1
    ```
* `count()`: Возвращает количество элементов, переданных в качестве аргумента
    ```python
    my_list = [3, 8, 1, 6, 0, 8, 4]
    print(my_list.count(8)) # 2
    ```
* `sort()`: Сортировка элементов в списке в порядке возрастания 
    ```python
    my_list = [3, 8, 1, 6, 0, 8, 4]
    my_list.sort()
    print(my_list)   # [0, 1, 3, 4, 6, 8, 8]
    ```
* `reverse()`: Обратный порядок элементов в списке 
    ```python
    my_list = [3, 8, 1, 6, 0, 8, 4]
    my_list.reverse()
    print(my_list)   # [8, 8, 6, 4, 3, 1, 0]
    ```
* `copy()`: Возвращает поверхностную копию списка  
    ```python
    my_list = [3, 8, 1, 6, 0, 8, 4]
    list = []
    print(list)      # []
    list = my_list.copy()
    print(list)      # [3, 8, 1, 6, 0, 8, 4]
    ```
___
### [Срез списка](#срез-списка)
##### [оглавление](#оглавление)

```python
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0])               # 1
print(list_1[1])               # 2
print(list_1[len(list_1)-1])   # 10
print(list_1[-5])              # 6
print(list_1[:])               # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2])              # [1, 2]
print(list_1[len(list_1)-2:])  # [9, 10]
print(list_1[2:9])             # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18])           # []
print(list_1[0:len(list_1):6]) # [1, 7]
print(list_1[::6])             # [1, 7]
```
___
### [Кортежи](#кортежи)
##### [оглавление](#оглавление)
Кортеж — это неизменяемый список.
Кортеж нужен, если:
* необходима защита каких-либо данных от изменений (намеренных или случайных).
* занимает меньше места в памяти и работают быстрее, по сравнению со списками

```python
t = ()               # создание пустого кортежа
print(type(t))       # <class 'tuple'>
t = (1,)
print(type(t))       # <class 'tuple'>
t = (1)
print(type(t))       # <class 'int'>
t = (28, 9, 1990)    
print(type(t))       # <class 'tuple'>
```
Можно распаковать кортеж в независимые переменные:
```python
t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue

```
___
### [Словари](#словари)
##### [оглавление](#оглавление)
**`Словари`** — неупорядоченные коллекции произвольных объектов с доступом по ключу.

В `списках` в качестве ключа используется индекс элемента.

В `словаре` для определения
элемента используется значение ключа (строка, число).

```python
dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary)         # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ← типы ключей могут отличаться
print(dictionary['up'])   # ↑ типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
print(dictionary['type']) # KeyError: 'type'
del dictionary['left']    # удаление элемента
```
___
### [Множества](#множества)
##### [оглавление](#оглавление)
Одно множество может содержать значения любых типов.

Если у Вас есть два множества, можн совершать над ними любые стандартные операции, например:
* объединение
* пересечение
* разность

```python
colors = {'red', 'green', 'blue'}
print(colors)         # {'red', 'green', 'blue'}
colors.add('red')
print(colors)         # {'red', 'green', 'blue'}
colors.add('gray')
print(colors)         # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors)         # {'green', 'blue','gray'}
colors.remove('red')  # KeyError: 'red'
colors.discard('red') # ok
```
```python
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()                                     # c = {1, 2, 3, 5, 8}
u = a.union(b)                                   # u = {1, 2, 3, 5, 8, 13,
i = a.intersection(b)                            # i = {8, 2, 5}
dl = a.difference(b)                             # dl = {1, 3}
dr = b.difference(a)                             # dr = {13, 21}
q = a.union(b).difference(a.intersection(b))     # q = {1, 21, 3, 13}
```
**`frozenset`** - неизменяемое или замороженное множество, с которым не будут
работать методы удаления и добавления.
```python
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b)             # frozenset({1, 2, 3, 5, 8})
```
___
### [Рекурсия](#рекурсия)
##### [оглавление](#оглавление)
`Рекурсия` — это функция, вызывающая сама себя.

При описании рекурсии важно указать, когда функции надо остановиться и
перестать вызывать саму себя. По-другому говоря, необходимо указать базис
рекурсии.

ПРИМЕРЫ
```python
# Последовательность Фибоначчи
def fibo_recur(number):
    while number >= 2:
        return fibo_recur(number - 1) + fibo_recur(number - 2)
    else:
        return 1
```
```python
def swap (list):
    for i in range(list.count(max(list))):
        list[list.index(max(list))] = min(list)
    return list
```
```python
# Выводит последововательность в обратном порядке
def rev_inp(input_number):
    if input_number == 1:
        value = input()
        return value
    value = input()
    return rev_inp(input_number - 1) + ' ' + value
```
```python
def num_degree(number, degree):
    result = number
    while degree > 0:
        # result = result * num_degree(number, degree - 1)
        return result * num_degree(number, degree - 1)
    return 1
```
```python
def summ_digits(num_1, num_2):
    if num_2 == 0:
        return num_1
    return summ_digits(num_1 + 1, num_2 - 1)
```
```python
# Быстрая сортировка по возрастанию
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
# по убыванию нужно поменять лишь одну строку
    return quicksort(greater) + [pivot] + quicksort(less)
```
___
### [Функции all() any() zip() enumerate() filter() map()](#функции-all-any-zip-enumerate-filter-map)
##### [оглавление](#оглавление)
* #### [map(function, iterable)](#mapfunction-iterable)
    ##### [оглавление](#оглавление)
Функция `map()` — обрабатывает итерабельные объекты.

`map()` принимает еще одну функцию, с помощью которой перебираются все элементы по очереди.

`map()` возвращает специальный объект `map`, в дальнейшем преобразовываемый в список или кортеж. 

примеры:
```python
def times_10(num):
    return num * 10
nums = [1, 2, 3, 4, 5]
nums = list(map(times_10, nums))
print(nums)     # [10, 20, 30, 40, 50]

# вместо функции можно написать лямбда-выражение.
times_10 = lambda num: num * 10
nums = [1, 2, 3, 4, 5]
nums = list(map(times_10, nums))
print(nums)     # [10, 20, 30, 40, 50]
```
```python
list_1 = [1, 2, 3, 4]   # type значений <class 'int'>
list_2 = list(map(lambda x: x ** 2, list_1))
print(list_2)           # [1, 4, 9, 16]

list_3 = list(map(str, list_1))
print(list_3)           # ['1', '2', '3', '4'] - type значений <class 'str'>
```
```python
# map() возвращает список с суммами чисел из разных коллекций по общим индексам
def add(n1, n2, n3):
    return n1 + n2 + n3
nums1 = [1, 3, 5, 7, 9]
nums2 = [2, 4, 6, 8, 10]
nums3 = [11, 12, 13, 14, 15]
sums = list(map(add, nums1, nums2, nums3))
print(sums)     # [14, 19, 24, 29, 34]
```
* #### [filter(function, iterable)](#filterfunction-iterable)
    ##### [оглавление](#оглавление)
`filter()` применяется для простой фильтрации итерабельного объекта без необходимости создания собственного цикла или дополнительных переменных.

`filter()` возвращает либо `True`, либо `False`, в зависимости от условия.

Если возвращает `False`, то элемент будет удален из итерабельного объекта, если `True` — останется.

`filter()` также возвращает специальный объект `filter`, который затем преобразовывается в список или кортеж.
```python
people = [
    ('Johnny', 22),
    ('Adam', 18),
    ('Mark', 12),
    ('Jack', 14),
    ('Sam', 20)]
def is_adult(person):       # person --> (name, age)
    return person[1] >= 18
adults = filter(is_adult, people)
print(list(adults))         # [('Johnny', 22), ('Adam', 18), ('Sam', 20)]

# лямбда-выражение вместо функции
is_adult = lambda person: person[1] >= 18
adults = filter(is_adult, people)
print(list(adults))         # [('Johnny', 22), ('Adam', 18), ('Sam', 20)]
```
* #### [all(iterable)](#alliterable)
    ##### [оглавление](#оглавление)
`all()` принимает в качестве параметра любой итерабельный объект: список, кортеж, множество словарь или диапазон.

Функция возвращает `True`, если все элементы итерируемого объекта равняются `True`, а в противном случае — `False`.

Любой числовой тип данных, кроме нуля, равняется `True`, а любая строка, содержащая более одного символа, также равняется `True`.
```python
color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]
print(all(c =='green' for c in color1))     # False
print(all(c =='green' for c in color2))     # True 
```
```python
all([True, True, True])             # True
all([True, True, 0])                # False
all(("", True, 5))                  # False
all((True, 1.75, "Hello"))          # True
all({False, "World", True})         # False
all({"Hi", -0.5, True})             # True
all({0: "Hello", 1: "World"})       # False
all({"Hello World": -1.75, 5: 6})   # True
```
* #### [any(iterable)](#anyiterable)
    ##### [оглавление](#оглавление)
`any()` похожа на функцию `all()`.

Она также принимает в качестве параметра итерабельный объект, но возвращает `True`, если хотя бы один из элементов итерабельного объекта равен `True`, в противном случае — `False`.

Для различных типов данных действуют одни и те же правила оценки объекта как равного `True` или `False`.
```python
color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]
print(any(c =='green' for c in color1))     # True  
print(any(c =='green' for c in color2))     # True
```
```python
any([False, False, False])      # False
any([7.5, False, 0])            # True
any(("", 0, "Hi"))              # True
any((0, '', ""))                # False
any({0, "World", False})        # True
any({'', -0.5, 0})              # True
any({'': False, 1.5: False})    # True
any({"": True, False: 6})       # False
```
* #### [zip(interable1, interable2, interable3, …)](#zipinterable1-interable2-interable3)
    ##### [оглавление](#оглавление)
`zip()` принимает любое количество итерабельных объектов.

При обработке словаря функция просматривает только ключ, но не значения.

`zip()` попарно объединяет элементы переданных коллекций по их индексу и возвращает специальный объект `zip`, который можно преобразовать в список или кортеж, состоящий из кортежей.

`zip()` обычно применяется для одновременного перебора нескольких списков.
```python
names = ["Johnny", "Adam", "Mark"]
ages = [14, 16, 17]
people = list(zip(names, ages))
print(people)   # [('Johnny', 14), ('Adam', 16), ('Mark', 17)]
```
Объект `zip` можно обойти в цикле следующим образом:
```python
names = ["Johnny", "Adam", "Mark"]
ages = [14, 16, 17]
for name, age in zip(names, ages):
    print(name, age)
```
* #### [enumerate(iterable, start=0)](#enumerateiterable-start0)
    ##### [оглавление](#оглавление)
`enumerate()` чаще всего применяется для циклического просмотра списка.

После передачи итерабельного объекта в качестве параметра функция возвращает список из кортежей, где каждый кортеж содержит индекс элемента и сам элемент.

Функция возвращает специальный объект enumerate, поэтому впоследствии придется преобразовать его в список или кортеж.
```python
names = ["Johnny", "Adam", "Mark"]
enum_names = list(enumerate(names))
print(enum_names)
# [(0, 'Johnny'), (1, 'Adam'), (2, 'Mark')]
```
Параметр `start` указывает функции `enumerate()`, с какого числа начинать отсчет индексов.
```python
names = ["Johnny", "Adam", "Mark"]
enum_names = list(enumerate(names, start=2))
print(enum_names)
# [(2, 'Johnny'), (3, 'Adam'), (4, 'Mark')]
```
Объект `enumerate` можно обойти в цикле следующим образом:
```python
names = ["Johnny", "Adam", "Mark"]
for i, name in enumerate(names):
    print(i, name)
# 0 Johnny
# 1 Adam
# 2 Mark
```
___
