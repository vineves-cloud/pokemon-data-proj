import json
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite://pokemon.db")

with open("data/raw/pokemon.json") as f:
    data = json.load(f)

df = pd.json_normalize(data)

df.to_sql("raw_pokemons", engine, if_exists="replace", index=False)

print("Dados carregados com sucesso!")