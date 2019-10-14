#!/usr/bin/python

import math
# takes in recipe as a dictionary, and ingredients as a dictionary.
# Compares the two, and tells you how many batches you can make based on the calls in recipe and the amount of stuff you have
# in ingredients.
# Compare each item in the recipe to each item in the ingredients
# subtract those two items until one of them reaches 0 , that's the # of batches you can make


def recipe_batches(recipe, ingredients):
    # recipe_values = recipe.values()
    # ingredients_values = ingredients.values()
    recipe_keys = recipe.keys()
    ingredients_keys = ingredients.keys()

    # * set default value for batches to be 0
    batches = 0

    # * if the keys don't match between dictionaries, you can't make any of what it wants
    if ingredients_keys != recipe_keys:
        # can't make any
        batches = 0
    # * if it passes into else, that means that the keys match up
    else:
      # *loop through ingredients
        for i in ingredients:
            # print(i)
            # print(recipe[i], ingredients[i])
            # * if ingredients[i] is bigger than recipe[i], then we can make some batches of stuff
            if ingredients[i] >= recipe[i]:
                # print('greater')
                # *if the current amount of batches is greater than the quotient, then we can't make any more. If it's less, then we can
                # * also, if batches is 0, that just means it's the first iteration so go for it
                # * this also takes the lowest amount of the result of each division, because batches must be > the result of divison
                # * in order to run the if logic
                if batches > ingredients[i] // recipe[i] or batches == 0:
                    # * if it gets to this point, then the quotient of ingredients/recipe is how many batches can be made
                    batches = ingredients[i] // recipe[i]
                    # print(batches, 'batches under div')
            # *if ingredients is < recipe, you can't make any
            else:
                batches = 0

    print(batches, 'total')
    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
recipe = {'milk': 100, 'butter': 50, 'flour': 5}
ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
recipe1 = {'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}
ingredients1 = {'milk': 1288, 'flour': 9, 'sugar': 95}
recipe2 = {'milk': 100, 'butter': 50, 'cheese': 10}
ingredients2 = {'milk': 198, 'butter': 52, 'cheese': 10}
recipe3 = {'milk': 2, 'sugar': 40, 'butter': 20}
ingredients3 = {'milk': 5, 'sugar': 120, 'butter': 500}
# recipe_batches(recipe, ingredients)
# recipe_batches(recipe1, ingredients1)
# recipe_batches(recipe2, ingredients2)
recipe_batches(recipe3, ingredients3)
