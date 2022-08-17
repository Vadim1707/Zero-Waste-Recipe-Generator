from automap import engine, Base
from sqlalchemy import inspect, text
import pandas as pd

from pprint import pprint

df = pd.read_sql_table(table_name='Ingredients', con=engine, schema='Recipe')

df['recipe_id'] = df['recipe_id'].astype(int)
# print(df[:29])

df2 = df.groupby(by='recipe_id').count()
df2.rename(columns={'index':'total_ingred'}, inplace=True)
df2 = df2['total_ingred']
# print(df2[:29])


df2.to_sql(name='Total', con=engine, schema='Recipe', if_exists='replace')






"""
print(nq2[2][2])
for ind in range(23,30):
    print(df['raw_ingredient'][ind], has_ingredient(df['raw_ingredient'][ind], nq2[2][2]))"""

def has_ingredient(ing1, ing2):
    if ing1.lower() in ing2.lower():
        return True
    return False
