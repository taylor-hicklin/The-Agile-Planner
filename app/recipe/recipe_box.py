"""recipe_box module for RecipeBox class. Ensure that RecipeBox only has one instance by importing singleton.
Implement singleton.Singleton as metaclass for RecipeBox"""

from app import singleton


class RecipeBox(metaclass=singleton.Singleton):  # RecipeBox is an instance of Singleton due to use of metaclass
    def __init__(self):
        self.recipe_obj_list = []

    @classmethod
    def create_recipe_box(cls):
        return cls()

    @staticmethod
    def add_recipe_to_box(recipe_box_obj, recipe_obj):
        recipe_box_obj.recipe_obj_list.append(recipe_obj)
        return recipe_box_obj
