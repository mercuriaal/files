def turn_into_dict():
    list_of_recipes = []
    cook_book = {}
    with open('Задача №1 + №2/recipes', encoding='utf-8') as recipe:
        text = recipe.read().split('\n')
    element = ''
    for string in text:
        if string != '':
            element += string + '\n'
            if string == text[-1]:
                list_of_recipes.append(element)
        else:
            list_of_recipes.append(element)
            element = ''
    for recipe in list_of_recipes:
        splited_recipe = recipe.split('\n')
        cook_book[splited_recipe[0]] = []
        count = int(splited_recipe[1])
        list_of_ingredients = splited_recipe[2:count + 2]
        for ingredient in list_of_ingredients:
            ingredient_description = ingredient.split('|')
            cook_book[splited_recipe[0]].append(dict(ingredient_name=ingredient_description[0].strip(),
            quantity=int(ingredient_description[1]), measure=ingredient_description[2].strip()))
    return cook_book


cook_book = turn_into_dict()


def get_shop_list_by_dishes(dishes, person_count):
    ingredient_name_list = []
    shop_list = {}
    for dish, list_of_ingredients in cook_book.items():
        if dish in dishes:
            for ingredient_descriptions in list_of_ingredients:
                ingredient_value = ingredient_descriptions.get('ingredient_name')
                quantity_value = ingredient_descriptions.get('quantity')
                ingredient_name_list.append(ingredient_value)
                count = ingredient_name_list.count(ingredient_value)
                del ingredient_descriptions['ingredient_name']
                if count == 1:
                    shop_list[ingredient_value] = ingredient_descriptions
                else:
                    shop_list[ingredient_value]['quantity'] += quantity_value
    for key, value in shop_list.items():
        value['quantity'] = value['quantity'] * person_count
    return shop_list


print(get_shop_list_by_dishes(['Омлет','Фахитос'], 2))









