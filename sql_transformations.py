from automap import engine, Base
from sqlalchemy import text
from pprint import pprint
import pandas as pd


# importing raw data, transforming it into Ingredients table, to make work easier

query = engine.execute(text('''
    SELECT ingredients, "European"."Id" from "Recipe"."European"
    ''')).all()


total_ingr = []
for i in range(len(query)):
    arr = eval(query[i][0])
    ind = query[i][1]
    for elem in arr:
        total_ingr.append([elem, ind])

# making a dataframe with all ingredients

new_df = pd.DataFrame(total_ingr, columns=['raw_ingredient', 'recipe_id'])

d = {'raw_ingredient': new_df['raw_ingredient'], 'mapped_name': 'NA', 'was_mapped': 0, 'recipe_id': new_df['recipe_id'], 'ingredient_id': 0}
data = pd.DataFrame(d)


# function for mapping ingredients to simplified versions of themselves

def change_df(data, ingr, id):
    tmp = data["raw_ingredient"].copy()
    data["raw_ingredient"] = data["raw_ingredient"].str.lower()
    cont = data[data['raw_ingredient'].str.contains(ingr)]
    cont['mapped_name'] = ingr
    cont['was_mapped'] = 1
    cont['ingredient_id'] = id

    data.update(cont)
    data["raw_ingredient"] = tmp


# mapping of ingredients

change_df(data, 'egg', 1)
change_df(data, 'sugar', 2)
change_df(data, 'potato', 3)
change_df(data, 'onion', 4)
change_df(data, 'bacon', 5)
change_df(data, 'flour', 6)
change_df(data, 'pepper', 7)
change_df(data, 'butter', 8)
change_df(data, 'oil', 9)
change_df(data, 'vinegar', 10)
change_df(data, 'cabbage', 11)
change_df(data, 'water', 12)
change_df(data, 'salt', 13)
change_df(data, 'cinnamon', 14)
change_df(data, 'apple', 15)
change_df(data, 'celery', 16)
change_df(data, 'vanilla', 17)
change_df(data, 'almond', 18)
change_df(data, 'soda', 19)
change_df(data, 'garlic', 20)
change_df(data, 'shrimp', 21)
change_df(data, 'paprika', 22)
change_df(data, 'parsley', 23)
change_df(data, 'beef', 24)
change_df(data, 'zucchini', 25)
change_df(data, 'sherry', 26)
change_df(data, 'olive', 27)
change_df(data, 'cheese', 28)
change_df(data, 'nutmeg', 29)
change_df(data, 'milk', 30)
change_df(data, 'bread', 31)
change_df(data, 'lemon', 32)
change_df(data, 'tomato', 33)
change_df(data, 'oregano', 34)
change_df(data, 'spaghetti', 35)
change_df(data, 'mushroom', 36)
change_df(data, 'dill', 37)
change_df(data, 'soy sauce', 38)
change_df(data, 'chicken', 39)
change_df(data, 'cream', 40)
change_df(data, 'cutlet', 41)
change_df(data, 'rice', 42)
change_df(data, 'pasta', 43)
change_df(data, 'sausage', 44)
change_df(data, 'rosemary', 45)
change_df(data, 'wine', 46)
change_df(data, 'pork', 47)
change_df(data, 'ketchup', 48)
change_df(data, 'walnut', 49)
change_df(data, 'basil', 50)
change_df(data, 'thyme', 51)
change_df(data, 'sauce', 52)
change_df(data, 'carrot', 53)
change_df(data, 'escarole', 54)
change_df(data, 'bean', 55)
change_df(data, 'fish', 56)
change_df(data, 'mustard', 57)
change_df(data, 'cumin', 58)
change_df(data, 'optional', 59)
change_df(data, 'spinach', 60)
change_df(data, 'lobster', 61)
change_df(data, 'italian', 62)
change_df(data, 'ham', 63)
change_df(data, 'shallot', 64)
change_df(data, 'herbes', 65)
change_df(data, 'beets', 66)
change_df(data, 'poppy', 67)
change_df(data, 'allspice', 68)
change_df(data, 'fennel', 69)
change_df(data, 'pine', 70)
change_df(data, 'honey', 71)
change_df(data, 'yeast', 72)
change_df(data, 'dough', 73)
change_df(data, 'marjoram', 74)
change_df(data, 'gelatin', 75)
change_df(data, 'artichoke', 76)
change_df(data, 'cucumber', 77)
change_df(data, 'noodle', 78)
change_df(data, 'coconut', 79)
change_df(data, 'chocolate', 80)
change_df(data, 'sage', 81)
change_df(data, 'prosciutto', 82)
change_df(data, 'mayonnaise', 83)
change_df(data, 'spice', 84)
change_df(data, 'bay', 85)
change_df(data, 'lentil', 86)
change_df(data, 'caper', 87)
change_df(data, 'lentil', 88)
change_df(data, 'raisins', 89)
change_df(data, 'turkey', 90)
change_df(data, 'sauerkraut', 91)
change_df(data, 'barley', 92)
change_df(data, 'leek', 93)
change_df(data, 'beer', 94)
change_df(data, 'tarragon', 95)
change_df(data, 'tilapia', 96)
change_df(data, 'pesto', 97)
change_df(data, 'lamb', 98)
change_df(data, 'cauliflower', 99)
change_df(data, 'cocoa', 100)
change_df(data, 'lard', 101)
change_df(data, 'cornmeal', 102)
change_df(data, 'turnip', 103)
change_df(data, 'baguette', 104)
change_df(data, 'margarine', 105)
change_df(data, 'cardamom', 106)
change_df(data, 'ginger', 107)
change_df(data, 'clove', 108)
change_df(data, 'anise', 109)
change_df(data, 'baking powder', 110)
change_df(data, 'mozzarella', 111)
change_df(data, 'cornstarch', 112)
change_df(data, 'molasses', 113)
change_df(data, 'shortening', 114)
change_df(data, 'rum', 115)
change_df(data, 'caraway', 116)
change_df(data, 'orange', 117)
change_df(data, 'duck', 118)
change_df(data, 'half-and-half', 119)
change_df(data, 'steak', 120)
change_df(data, 'herb', 121)
change_df(data, 'lavender', 122)
change_df(data, 'pea', 123)
change_df(data, 'mint', 124)
change_df(data, 'grape', 125)
change_df(data, 'veal', 126)
change_df(data, 'coriander', 127)
change_df(data, 'savory', 128)
change_df(data, 'kale', 129)
change_df(data, 'lime', 130)
change_df(data, 'trout', 131)
change_df(data, 'puff pastry', 132)
change_df(data, 'tofu', 133)
change_df(data, 'liver', 134)
change_df(data, 'chile', 135)
change_df(data, 'nut', 136)
change_df(data, 'pistachio', 137)
change_df(data, 'coffee', 138)
change_df(data, 'whiskey', 139)
change_df(data, 'pumpkin', 140)
change_df(data, 'currants', 141)
change_df(data, 'brandy', 142)
change_df(data, 'salmon', 143)
change_df(data, 'octopus', 144)
change_df(data, 'cilantro', 145)
change_df(data, 'yogurt', 146)
change_df(data, 'liqueur', 147)
change_df(data, 'lettuce', 148)
change_df(data, 'hummus', 149)
change_df(data, 'fig', 150)
change_df(data, 'pecan', 151)
change_df(data, 'vodka', 152)
change_df(data, 'citric acid', 153)
change_df(data, 'broccoli', 154)
change_df(data, 'parmesan', 155)
change_df(data, 'pickle', 156)
change_df(data, 'chili', 157)
change_df(data, 'pie crust', 158)
change_df(data, 'rabbit', 159)
change_df(data, 'saffron', 160)
change_df(data, 'eggplant', 161)


def show_ind(ind):
    # function for testing and checking data
    tmp = data[data['ingredient_id'] == ind]
    print(tmp[0:40], len(tmp))

# all no name ingredients are in other category now
mydf = data[data['was_mapped']==0]
mydf['mapped_name'] = 'other'
mydf['was_mapped'] = 1
data.update(mydf)


# importing all into sql
data.to_sql(name='Ingredients', con=engine, schema='Recipe', if_exists='replace')

