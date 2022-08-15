from asyncio.windows_events import NULL
from os import TMP_MAX
from automap import European, engine, Base
from sqlalchemy import text
from pprint import pprint
import pandas as pd
from random import randint, sample

"""from sqlalchemy import create_engine, Column, String, Integer, text
# from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
#from local_settings import postgresql as settings

from pprint import pprint

def get_engine(user, passwd, host, port, db):
    url = f"postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine

engine = get_engine(settings['pguser'],
        settings['pgpassword'],
        settings['pghost'],
        settings['pgport'],
        settings['pgdb'])

print(engine.url)

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'test0'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ingredients = Column(String)
    description = Column(String)

    def __repr__(self):
        return f"recipe - {self.name}"

    #TODO ingredients: Dict[str, str] ingredient - amount, etc.

recipes = [
    Recipe(id=1, name="boiled egg", ingredients='egg',description="boil an egg" ),
    Recipe(id=2, name="raw egg", ingredients='egg', description="eat an egg")
    ]

# adding few entries to test table

def create_recipes():
    with SessionLocal() as session:
        for recipe in recipes:
            session.add(recipe)
        session.commit()

# create_recipes()

with SessionLocal() as session:
    recipe_records = session.query(Recipe).all()
    for recipe in recipe_records:
        print(recipe)
"""

# Getting schema names of recipe_db database
def get_schemas(engine):
    with engine.connect() as conn:
        result = conn.execute(
        text(
            """SELECT schema_name
            FROM information_schema.schemata;"""
        )
    )

    print(result.all())

# Getting all tables of recipe_db database with given schemaname
def get_tables(engine, schema_name):
    with engine.connect() as conn:
        result = conn.execute(
        text(
            """select * from information_schema.tables
               where table_schema = '{}'""".format(schema_name)
        )
    )

    pprint(result.all())

# get_schemas(engine=engine)
# get_tables(engine, 'Recipe')


def select_top(n):
    with engine.connect() as conn:
        result = conn.execute(
        text(
            """SELECT * FROM "Recipe"."European"
            ORDER BY "Id" ASC LIMIT {}""".format(n)
        )
    )
    pprint(result.all())

# select_top(4)

def select_ingredients(engine):
    with engine.connect() as conn:
        result = conn.execute(
        text(
            """SELECT distinct(mapped_name) FROM "Recipe"."Ingredients" """
        )
    )
    r = []
    for entry in result.all():
        r.append(entry[0])
    return r

def select_recipes(n):
    with engine.connect() as conn:
        len = conn.execute(
        text(
            """SELECT * FROM "Recipe"."European" 
               """
        )).all().__len__()
        print(len)

        rand_ind = tuple(sample(range(len), n))
        print(rand_ind)

        result = conn.execute(
        text(
            """SELECT * FROM "Recipe"."European" 
                WHERE "European"."Id" in {}""".format(rand_ind)
        )
    )
    return result.all()

# pprint(select_recipes(5))

example = ["broccoli",
  "octopus",
  "prosciutto",
  "rosemary",
  "ginger",
  "onion",
  "veal",
  "cocoa",
  "celery",
  "milk",
  "rabbit",
  "olive",
  "shallot",
  "pie crust",
  "turkey",
  "lime"]


def generate(ingredients):
    # ingredients.extend(["water", "salt", "pepper"])
    with engine.connect() as conn:
        result = conn.execute(
        text(
            """SELECT * FROM "Recipe"."Ingredients" 
                WHERE "Ingredients"."mapped_name" in {}""".format(tuple(ingredients))
        )).all()
    # table has amounts of occurrences in
    table = pd.DataFrame(result, index=range(1, len(result)+1))
    table = table.groupby('recipe_id').count()
    t = table['mapped_name']
    t = t.reset_index()
    t = t.set_index(t['recipe_id'].apply(int))
    #print('aaaa', t) 

    with engine.connect() as conn:
        var = conn.execute(
        text(
            """SELECT * FROM "Recipe"."Total" 
                """
        )).all()
    table2 = pd.DataFrame(var)
    #print('bbbb', table2)

    table3 = pd.concat([t,table2], axis=1)
    table3.rename(columns={'mapped_name':'ingred_given'}, inplace=True)
    #print(table3)
    mode = table3['ingred_given'].mode().values[0]
    table3['ingred_given'].fillna(value=mode, inplace=True)
    #print('cccc', table3)
    table3['ingred_given'] = table3['ingred_given'].fillna(0)
    table3['ingred_given'] = table3['ingred_given'].astype(int)
    table3['difference'] = table3['total_ingred'] - table3['ingred_given']

    #print('dddd', table3.sort_values(by='difference', ascending=True))
    res = table3[table3["difference"]==0]
    #print('ddee', res.sort_values(by='difference', ascending=True))
    res = tuple(list(res.index.dropna()))
    #print('eeee', res)
    
    with engine.connect() as conn:
        query = conn.execute(
        text(
            """SELECT * FROM "Recipe"."European" 
                Where "European"."Id" in {} """.format(res)
        ))

    rr = query.all()
    rrr = []
    for entry in rr:
        rrr.append(dict(entry))

    return rrr

e = [  "spaghetti",
  "trout",
  "yogurt",
  "duck",
  "fish",
  "ketchup",
  "butter",
  "vanilla",
  "broccoli",
  "octopus",
  "prosciutto",
  "rosemary",
  "ginger",
  "onion",
  "veal",
  "cocoa",
  "celery",
  "milk",
  "rabbit",
  "olive",
  "shallot",
  "pie crust",
  "turkey",
  "lime"]
pprint(generate(e))


def update_db(recipe):
    pass