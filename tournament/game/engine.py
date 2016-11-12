from __future__ import division
import pandas as pd
import numpy as np
from game.models import *

def populate_database(path_to_dir):
    # Create pandas dataframe
    df = pd.read_csv(path_to_dir)
    # Iterate through dataframe
    for index, row in df.iterrows():
        target_serving_size = int(row["target_serving_size"])
        this_serving_size = int(row["serving_size"])
        target_to_this_ratio = target_serving_size / this_serving_size
        i = Item(name = row["name"],
                description = row["description"],
                photo_url = row["photo_url"],
                group = row["group"],
                matches_played = int(row["matches_played"]),
                matches_won = int(row["matches_won"]),
                price_per_serving = round(np.multiply(row["price_per_serving"], target_to_this_ratio), 2),
                serving_size = target_serving_size,
                calories = round(np.multiply(row["calories"], target_to_this_ratio), 2),
                fat = round(np.multiply(row["fat"], target_to_this_ratio), 2),
                cholesterol = round(np.multiply(row["cholesterol"], target_to_this_ratio), 2),
                sodium = round(np.multiply(row["sodium"], target_to_this_ratio)),
                carbohydrates = round(np.multiply(row["carbohydrates"], target_to_this_ratio), 2),
                sugar = round(np.multiply(row["sugar"], target_to_this_ratio), 2),
                protein = round(np.multiply(row["protein"], target_to_this_ratio), 2),
                vitA = round(np.multiply(row["vitA"], target_to_this_ratio)),
                vitC = round(np.multiply(row["vitC"], target_to_this_ratio)),
                calcium = round(np.multiply(row["calcium"], target_to_this_ratio)),
                iron = round(np.multiply(row["iron"], target_to_this_ratio)),
                fiber = round(np.multiply(row["fiber"], target_to_this_ratio), 2),
                vegetarian = int(row["vegetarian"]) == 1,
                vegan = int(row["vegan"]) == 1,
                organic = int(row["organic"]) == 1,
                gluten_free = int(row["gluten-free"]) == 1,
                nut_free = int(row["nut-free"]) == 1,
                lactose_free = int(row["lactose-free"]) == 1)
        i.save()
