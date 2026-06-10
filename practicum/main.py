from typing import List

from practicum.bun import Bun
from practicum.burger import Burger
from practicum.database import Database
from practicum.ingredient import Ingredient


def main():
    # Initialise the database
    database: Database = Database()

    # Create a new burger
    burger: Burger = Burger()

    # Get available buns from the database
    buns: List[Bun] = database.available_buns()

    # Get available ingredients from the database
    ingredients: List[Ingredient] = database.available_ingredients()

    # Assemble the burger
    burger.set_buns(buns[0])

    burger.add_ingredient(ingredients[1])
    burger.add_ingredient(ingredients[4])
    burger.add_ingredient(ingredients[3])
    burger.add_ingredient(ingredients[5])

    # Move an ingredient to a new position
    burger.move_ingredient(2, 1)

    # Remove an ingredient
    burger.remove_ingredient(3)

    # Print the burger receipt
    print(burger.get_receipt())


if __name__ == "__main__":
    main()
