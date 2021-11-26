"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def check_string(first, second):
  if isinstance(first, str) and isinstance(second, str):
    if first == second:
      return 1
    else:
      if len(first) > len(second):
        return 2
      if second == 'learn':
        return 3
  else:
    return 0


DATAS = {
  1: 'learn',
  'first1': 'first1',
  'first': 'second',
  'second': 'first',
  'fir': 'learn'
}


def main():
  for d in DATAS:
    print(f'Первое значение: {d}, Второе значение: {DATAS[d]}')
    print(f'Результат: {check_string(d, DATAS[d])}')
    
if __name__ == "__main__":
    main()
