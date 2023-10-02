#!/usr/bin/python3
from regexpackage.Ingredients_Regex import IngredientRegex

data = "Ingredients: butter, sugar, brown sugar, eggs, vanilla extract, flour, baking soda, chocolate chips. Instructions: Preheat oven to 350°F. Cream together butter, sugar, and brown sugar"

IngredientRegex(data)
