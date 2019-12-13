#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_batches = 0

  max_arr = []

  for rec_item, rec_amount in recipe.items():
    print(rec_item, rec_amount)

    if rec_item in ingredients:
      print(f'rec_item: {rec_item}: {ingredients[rec_item]}')
      max_arr.append(ingredients[rec_item] / rec_amount)

    else: 
      max_arr.append(0)


      # if rec_amount > ingredients[rec_item]:
      #   print("yes")

    # for ing_item, ing_amount in ingredients.items():
    #   print(ing_item, ing_amount)
    #   if ingredients.includes()

  print(f'MAX_ARR: {max_arr}')
  print(int(min(max_arr)))

  # for k, v in ingredients.items():
  #   print(k, v)

  # return f'MAX_BATCH: {max_batches}'

  return int(min(max_arr))


print(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 }))
print(recipe_batches({ 'milk': 100, 'butter': 50, 'cheese': 10 }, { 'milk': 198, 'butter': 52, 'cheese': 10 }))
print(recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }))
print(recipe_batches({ 'milk': 2 }, { 'milk': 200}))

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))