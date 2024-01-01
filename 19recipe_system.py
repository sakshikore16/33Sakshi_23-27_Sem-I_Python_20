# 19. Design a recipe management system with classes for recipes, 
# ingredients, and users. Implement methods for adding recipes, 
# searching by ingredients.

class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def contains_ingredient(self, ingredient_name):
        return any(ingredient.lower() == ingredient_name.lower() for ingredient in self.ingredients)

class User:
    def __init__(self, username):
        self.username = username
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

def main():
    users = []

    while True:
        print("\nRecipe Management System")
        print("1. Add User")
        print("2. Add Recipe")
        print("3. Search Recipes by Ingredient")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            username = input("Enter username: ")
            users.append(User(username))
            print(f"User '{username}' added successfully!")

        elif choice == "2":
            if not users:
                print("Please add a user first.")
                continue

            username = input("Enter your username: ")
            user = next((u for u in users if u.username.lower() == username.lower()), None)

            if user:
                recipe_name = input("Enter recipe name: ")
                ingredient_names = input("Enter ingredients (comma-separated): ").split(',')
                instructions = input("Enter instructions: ")

                ingredients = [name.strip() for name in ingredient_names]
                recipe = Recipe(recipe_name, ingredients, instructions)
                user.add_recipe(recipe)

                print(f"Recipe '{recipe_name}' added successfully!")

            else:
                print(f"User '{username}' not found. Please add a user first.")

        elif choice == "3":
            if not users:
                print("Please add a user first.")
                continue

            ingredient_name = input("Enter ingredient to search for: ")
            found_recipes = []

            for user in users:
                for recipe in user.recipes:
                    if recipe.contains_ingredient(ingredient_name):
                        found_recipes.append(recipe)

            if found_recipes:
                print("\nFound Recipes:")
                for recipe in found_recipes:
                    print(f"\nRecipe: {recipe.name}")
                    print("Ingredients:", ', '.join(recipe.ingredients))
                    print("Instructions:", recipe.instructions)

            else:
                print(f"No recipes found with the ingredient '{ingredient_name}'.")

        elif choice == "4":
            print("Exiting Recipe Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
