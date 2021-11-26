"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

DATAS =   [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def main():
  item_sold_global_summ = 0
  for d in DATAS:
    item_sold_summ = 0
    for s in d['items_sold']:
      item_sold_summ += s
    average_sold = item_sold_summ/len(d['items_sold'])
    product_name = d['product']
    print(f'всего {product_name} было продано {item_sold_summ}')
    print(f'Среднее количество продаж {product_name}: {average_sold}')
    item_sold_global_summ += item_sold_summ
  global_average = item_sold_global_summ/36
  print(f'Суммарно было продано {item_sold_global_summ} товаров')
  print(f'В среднем проадавалось {global_average} товаров')
    
if __name__ == "__main__":
    main()
