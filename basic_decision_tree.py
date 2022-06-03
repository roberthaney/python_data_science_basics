import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import itertools

recipes = pd.read_csv("recipes.csv")
print "Successfully read data into dataframe"

# update first coulm header
column_names = recipes.columns.values
column_names[0] = "cuisine"
recipes.columns = column_names

# filter cuisines with < 50 entries
recipe_counts = recipes["cuisine"].value_counts()
cuisine_counts = recipe_counts > 50

print "Retaining", len(cuisine_counts), "cuisines with more than 50 recipes"

# subset data based on filter and check
cuisines_to_keep = list(recipe_counts.index.values[cuisine_counts])
recipes.loc[recipes["cuisine"].isin(cuisines_to_keep)]
print recipes.head()

# select asian/south-asian subset of recipes
asian_recipes = recipes[recipes.cuisine.isin(["Asian", "korean", "India", "Indian", "Chinese", "Thai", "chinese", "Japan", "Vietnamese"])]
cuisines = asian_recipes["cuisine"]
ingredients = asian_recipes.iloc[:,1:]

asian_tree = tree.DecisionTreeClassifier(max_depth=3)
asian_tree.fit(ingredients, cuisines)

print "Saved decision tree model"



