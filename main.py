import uvicorn
from typing import List #, Dict
from fastapi import FastAPI
from models import Recipe
from uuid import uuid4, UUID

app = FastAPI()

db: List[Recipe] = [
    Recipe(
        id=UUID("6b4dbab4-b529-40bf-acfc-89b35a111783"), 
        name = "omelette with cheese",
        ingredients = ["egg", "cheese", "olive oil"],
        description = """ Ingredients:
        2 large free-range eggs
        olive oil
        10 g Cheddar cheese

        Method
        Crack the eggs into a mixing bowl, season with a pinch of sea salt and black pepper, then beat well with a fork until fully combined.
        Place a small non-stick frying pan on a low heat to warm up.
        Grate the cheese onto a board and set aside.
        Add ½ tablespoon of oil to the hot pan, then carefully pour in the eggs.
        Tilt the pan to spread them out evenly, using a fork to swirl the eggs around the pan a little.
        When the omelette begins to cook and firm up, but still has a little raw egg on top, sprinkle over the cheese.
        Using a spatula, ease around the edges of the omelette, then fold it over in half.
        When it starts to turn golden brown underneath, remove the pan from the heat and slide the omelette onto a plate. Delicious with a tomato salad and wholemeal bread.
        """
    ),
    Recipe(
        id=UUID("5632753b-d5d2-4aa6-9c7d-44e7a272b146"), 
        name = "yogurt",
        ingredients = ["milk", "heavy cream", "starter for yogurt"],
        description = """Ingredients:
        2 quarts whole milk, the fresher the better
        1/4 cup heavy cream (optional)
        3 to 4 tablespoons plain whole milk yogurt with live and active cultures

        PREPARATION
        Rub an ice cube over the inside bottom of a heavy pot to prevent scorching (or rinse the inside of the pot with cold water). Add milk and cream, if using, and bring to a bare simmer, until bubbles form around the edges, 180 to 200 degrees. Stir the milk occasionally as it heats.
        Remove pot from heat and let cool until it feels pleasantly warm when you stick your pinkie in the milk for 10 seconds, 110 to 120 degrees. (If you think you’ll need to use the pot for something else, transfer the milk to a glass or ceramic bowl, or else you can let it sit in the pot.) If you’re in a hurry, you can fill your sink with ice water and let the pot of milk cool in the ice bath, stirring the milk frequently so it cools evenly.
        Transfer 1/2 cup of warm milk to a small bowl and whisk in yogurt until smooth. Stir yogurt-milk mixture back into remaining pot of warm milk. Cover pot with a large lid. Keep pot warm by wrapping it in a large towel, or setting it on a heating pad, or moving to a warm place, such as your oven with the oven light turned on. Or just set it on top of your refrigerator, which tends to be both warm and out of the way.
        Let yogurt sit for 6 to 12 hours, until the yogurt is thick and tangy; the longer it sits, the thicker and tangier it will become. (I usually let it sit for the full 12 hours.) Transfer the pot to the refrigerator and chill for at least another 4 hours; it will continue to thicken as it chills.
        """
    )
]

@app.get("/")
async def root():
    return {"Hello": "Cook!"}

@app.get("/api/v1/recipes")
async def fetch_recipes():
    return db

@app.post("/api/v1/recipes")
async def add_recipe(recipe: Recipe):
    db.append(recipe)
    return {"id": recipe.id}

@app.post("/api/v1/generate")
async def generate_recipes(ingr: List[str]):
    results = []
    for recipe in db:
        if list_contains(recipe.ingredients, ingr):
            results.append(recipe.name)
    return results

def list_contains(List1, List2): 
  
    set1 = set(List1) 
    set2 = set(List2) 
    if set1.intersection(set2): 
        return True 
    else: 
        return False