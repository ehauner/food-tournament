import pandas as pd
import numpy as np
from game.models import *

def populate_database(path_to_dir):
    # Create pandas dataframe
    df = pd.read_csv(path_to_dir)
    # Iterate through dataframe
    for index, row in df.iterrows():
        i = Item(name = row["name"],
                description = row["description"],
                photo_url = row["photo_url"],
                group = row["group"],
                matches_played = int(row["matches_played"]),
                matches_won = int(row["matches_won"]),
                price_per_serving = int(row["price_per_serving"]),
                serving_size = int(row["serving_size"]),
                calories = int(row["calories"]),
                fat = int(row["fat"]),
                cholesterol = int(row["cholesterol"]),
                sodium = int(row["sodium"]),
                carbohydrates = int(row["carbohydrates"]),
                sugar = int(row["sugar"]),
                protein = int(row["protein"]),
                vitA = int(row["vitA"]),
                vitC = int(row["vitC"]),
                calcium = int(row["calcium"]),
                iron = int(row["iron"]),
                fiber = int(row["fiber"]),
                vegetarian = int(row["vegetarian"]) == 1,
                vegan = int(row["vegan"]) == 1,
                organic = int(row["organic"]) == 1,
                gluten_free = int(row["gluten-free"]) == 1,
                nut_free = int(row["nut-free"]) == 1,
                lactose_free = int(row["lactose-free"]) == 1)
        i.save()
