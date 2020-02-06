#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  min_batches = -1
  for ingredient in recipe:
    if ingredient in ingredients:
      if recipe[ingredient] <= ingredients[ingredient]:
        possible_batches = ingredients[ingredient] // recipe[ingredient]
        if possible_batches < min_batches or min_batches == -1:
          min_batches = possible_batches
      else:
        min_batches = 0
        break
    else:
      min_batches = 0
  return min_batches



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))