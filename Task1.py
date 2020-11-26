class Cookbook():
    def turn_into_dict(self):
        list_of_recipes = []
        cook_book = {}
        with open('recipes', encoding='utf-8') as recipe:
            text = recipe.read().split('\n')
        element = ''
        for string in text:
            if string != '':
                element += string + '\n'
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
                quantity=ingredient_description[1].strip(), measure=ingredient_description[2].strip()))
        return cook_book


recipes = Cookbook()
print(recipes.turn_into_dict())










