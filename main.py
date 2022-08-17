import uvicorn
from typing import List #, Dict
from automap import European
from outdated.models import Recipe
from fastapi import FastAPI
from automap import engine, European #recipes
from db_queries import select_ingredients, select_recipes, generate, update_db

app = FastAPI()

@app.post("/api/v1/recipes/new")
async def add_recipe(recipe: Recipe):
    if update_db(recipe):
        return 0
    else:
        return {'Unknown':'Error'}

@app.post("/api/v1/recipes/ingredients")
async def generate_recipes(ingr: List[str]):
    return generate(ingr)

@app.get("/api/v1/recipes/random")
async def get_ideas_for_recipes(n: int):
    return select_recipes(n)

@app.get("/api/v1/ingredients/all")
async def get_all_ingredients():
    return select_ingredients(engine)

def list_contains_all(List1, List2):
    # checks if first list completely contains second one
    # TODO: to lowercase all entries of list1, list2
    return set([elem for elem in List2 if elem in List1])==set(List2)


"""
def list_contains(List1, List2): 
    # checks if first list contains at least something from list 2
    set1 = set(List1) 
    set2 = set(List2) 
    if set1.intersection(set2): 
        return True 
    else: 
        return False"""

