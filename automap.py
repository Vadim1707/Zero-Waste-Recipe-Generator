from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, inspect, text

from pprint import pprint

Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
engine = create_engine("postgresql+psycopg2://postgres:Hardpassword0@localhost:5432/recipes_db")

# reflect the tables
Base.prepare(engine, reflect=True, schema='Recipe')


# View details of columns of Table 
European = Base.classes.European

european_info = inspect(European)

# pprint(list(european_info.columns))

# Querying data (2-4 ingredients - ideas for recipes)
Session = sessionmaker(bind=engine)
session = Session()

ingredients = ['egg', 'chicken']

def create_text(ingr_list):
    res = '''
    SELECT title FROM "Recipe"."European"
    WHERE '''
    for i, ingr in enumerate(ingr_list):
        res += " ingredients LIKE '%{}%' ".format(ingr)
        if i != ingr_list.__len__() - 1:
            res += " and "
    return res

# print("\nQuery :\n", create_text(ingredients), "\n")

q = session.execute(text(create_text(ingredients))).all()

# pprint(q)