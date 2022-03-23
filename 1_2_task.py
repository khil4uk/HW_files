# Задание 1.

# создадим функцию, формирующую словарь cook book
def get_cook_book(file_path):
    cook_book = {}  # создадим пустой словарь
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            dish = line[:-1] # наименование блюда в cook book
            counter = f.readline().strip() # количество ингредиентов. Требуется привести к integer типу
            ingredients_list = [] # создаем список из ингредиентов в блюде
            for i in range(int(counter)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure']) #создаем вложенный словарь
                ingridient = f.readline().strip().split(' | ')
                for item in ingridient:
                    dish_items['ingredient_name'] = ingridient[0]
                    dish_items['quantity'] = int(ingridient[1])
                    dish_items['measure'] = ingridient[2]
                ingredients_list.append(dish_items)
                reciept = {dish: ingredients_list}
                cook_book.update(reciept)
            f.readline()

    return(cook_book)

#print(get_cook_book('recipes.txt'))

file_path = 'recipes.txt'
cook_book = get_cook_book(file_path)
#print (cook_book)

# Задание 2.

# напишем функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {} # создадим еще один пустой словарь для списка покупок
    for dish_name in dishes: # в цикле проходимся по указанным блюдам и ингредиентам внутри нее
        if dish_name in cook_book:
            items = cook_book[dish_name]
            for item in items:
                if item['ingredient_name'] in shop_list:
                    shop_list[item['ingredient_name']]['quantity'] += item['quantity'] * person_count
                else:
                    shop_list.update({item['ingredient_name']: {
                        "measure": item['measure'],
                        'quantity': item['quantity'] * person_count}})
        else:
            print("Блюдо не найдено в книге рецептов")
    return shop_list

print(get_shop_list_by_dishes(['Утка по-пекински', 'Фахитос'], 2))