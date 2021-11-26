"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def get_info(age: int):
  if age < 7:
    return 'Детский сад'
  elif age < 18:
    return 'Школа'
  elif age < 23:
    return 'ВУЗ'
  else:
    return 'Работа'


def main():
  age = input('Введите возраст: ')
  age = int(age)
  status = get_info(age)
  print(status)

if __name__ == "__main__":
    main()
