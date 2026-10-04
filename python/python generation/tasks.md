## Задача Иосифа Флавия

**Вариант 1**

```Python
n = int(input())
k = int(input())

circle = list(range(1, n + 1))
index = 0

while len(circle) > 1:
    index = (index + k - 1) % len(circle)
    circle.pop(index)
  
print(circle[0])
```



**Вариант 2**

```Python
n = int(input())
k = int(input())

survivor = 0
for i in range(2, n + 1):
  survivor = (survivor + k) % i

print(survivor + 1)
```


## Standard American Convention

На вход программе подается натуральное число. Напишите программу, которая вставляет в заданное число запятые в соответствии со стандартным американским соглашением о запятых в больших числах.

**Вариант 1 (f-строка)**

```Python
def format_number(number):
    return f"{number:,}"

print(format_number(3724650756252))
```



**Вариант 2 (format)**

```Python
def format_number(number):
    return format(number, ',')

print(format_number(1000000))
```


**Вариант 3 (ручной)**

```Python
def format_number(number):
    s = str(number)
    groups = []
  
    while s:
        groups.append(s[-3:])  # Добавляем 3 последних числа
        s = s[:-3]  # Удаляем 3 последних числа из s
    return ",".join(groups[::-1])

print(format_number(3724650756252))
```



**Моё решение**

```Python
def standardize_number(number):
    string_number = str(number)
    step = 3
    result = []

    for i in string_number:
        if len(result) == 0:  
            result.append(string_number[-3:])
          
        bit = string_number[-(step+3):-step]
      
        if bit == '':
            break
      
        result.append(bit)
        step += 3
      
    return ",".join(result[::-1])

print(
    standardize_number(3724650756252)
)
```



## Разворот числа

Дано пятизначное или шестизначное натуральное число. Напишите программу, которая изменит порядок его последних пяти цифр на обратный.

**Итоговый вариант**

```Python
def reverse_number(number):
  s = str(number)
  return int(s[:-5] + s[-5:][::-1])

print(reverse_number(int(input())))
```

**Моё решение**

```Python

def reverse_number(number):
    if number // 10000 <= 9:
        return str(number)[::-1].lstrip('0')
    else:
        return (str(number)[:1] + str(number)[1:][::-1]).lstrip('0')
  

print(reverse_number(int(input())))
```





## Определить знак зодиака по году

**Моё решение**

```Python
ANIMALS = (
    'Monkey', 
    'Rooster',
    'Dog',
    'Pig',
    'Rat',
    'Bull',
    'Tiger',
    'Rabbit',
    'Dragon',
    'Snake',
    'Horse',
    'Sheep',
)

def define_animal_year(year):
    CYCLE_LENGTH = 12
    return ANIMALS[year % CYCLE_LENGTH]
```



## Подсчёт слов в тексте

```Python
def count_words(text):
    """Count the number of words in a line."""
    return len(text.split())
  
print(count_words(input()))
```

## Стоимость строки

Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ (в том числе пробел) стоит **60** копеек.

**Вариант 1**

```Python
KOPECKS_PER_CHAR = 60

def calc_string_price(text):
  """Cost of a line: 60 kopecks for each character"""
  total_kopecks = len(text) * KOPECKS_PER_CHAR
  rubles, kopecks = divmod(total_kopeks, 100)
  return rubles, kopecks

rubles, kopecks = calc_string_price('Hello')
print(f'{rubles} р. {kopecks} коп.')
```



**Моё решение**

```Python
def calc_string_price(string):
    count = 0
  
    for i in string:
        count += 60
      
    rubles = count // 100
    kopecks = count % 100
  
    return rubles, kopecks


rubles, kopecks = calc_string_price('Я собираюсь сделать ему предложение, от которого он не сможет отказаться.')
print(f'{rubles} р. {kopecks} коп.')
```



## ИМТ

**Вариант 1 - С возвратом значения**

```Python
BMI_LOW = 18.5
BMI_HIGH = 25

def calc_imt(weight, height):
    """Calculation of BMI (body weight category)"""
    bmi = weight / height ** 2
  
    if bmi < BMI_LOW:
        category = 'Underweight'
    elif bmi > BMI_HIGH:
        category = 'Overweight'
    else:
        category = 'Normal weight'
    return bmi, category

bmi, label = calc_imt(56, 1.77)
print(f'bmi: {bmi:.1f} \nlabel: {label}')
```

`{bmi:.1f}` - спецификатор формата внутри f-строки:

* `:` - начало форматирования
* `.1` - один знак после запятой
* `f` - fixed-point (число с плавающей точкой в десятичном виде)

**Вариант 2 - Чистый и аккуратный**

```Python
def calc_imt(weight, height):
    """Calculation of BMI (body weight category)"""
    bmi = weight / height ** 2
    if bmi < 18.5:
        return 'Insufficient weight'
    if bmi > 25:
        return 'Excessive weight'
    return 'Optimal weight'
```

**Моё решение**

```Python
def calc_imt(weight, height):
    """Расчёт индекса массы тела"""
    calculation = weight / height**2
    low_limit = 18.5
    high_limit = 25
    result = None

    if low_limit <= calculation <= high_limit:
        result = 'Оптимальная масса'
    elif calculation > high_limit:
        result = 'Избыточная масса'
    else:
        result = 'Недостаточная масса'
    
    return result
  
print(
    calc_imt(
        58, 1.77
    )
)
```

## Расчёт корня без модуля math

Квадратный корень - возведение в степень 0.5

```Python
result = (2**10 + 8**10) ** 0.5 

# Тоже самое, что и:
math.sqrt(2**10, 8**10)
```
