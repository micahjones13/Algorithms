#!/usr/bin/python

import math
# takes in recipe as a dictionary, and ingredients as a dictionary.
# Compares the two, and tells you how many batches you can make based on the calls in recipe and the amount of stuff you have
# in ingredients.
# Compare each item in the recipe to each item in the ingredients
# subtract those two items until one of them reaches 0 , that's the # of batches you can make


def recipe_batches(recipe, ingredients):
    recipe_info = recipe.values()
    print(recipe_info)


# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

recipe = {'milk': 100, 'butter': 50, 'flour': 5}
ingredients = {'milk': 132, 'butter': 48, 'flour': 51}


recipe_batches(recipe, ingredients)
