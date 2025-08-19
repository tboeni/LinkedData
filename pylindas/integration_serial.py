import pandas as pd
import yaml
import os

from pylindas.pycube import Cube
from pylindas.lindas.namespaces import SCHEMA

ENVIRONMENT = os.getenv("CI_ENVIRONMENT_NAME")

letters = ["b"]

for letter in letters:

    # Load data and yaml
    #df = pd.read_csv(f"3_data_preparation/data_105_{letter}.csv", encoding="utf-8", sep=",")
    #with open(f"4_data_integration/description_105_{letter}.yaml", encoding="utf-8") as file:
    df = pd.read_csv(f"C:/Users/Bot3/OneDrive - Berner Fachhochschule/Files BAFU/FS/data_105_3/data_105_{letter}_1.csv", encoding="utf-8", sep=",")
    with open(f"C:/Users/Bot3/OneDrive - Berner Fachhochschule/Files BAFU/FS/description_data_105_{letter}.yaml", encoding="utf-8") as file:
        cube_yaml = yaml.safe_load(file)

    text_cols = ["Grössenklasse", "Steuerhoheit", "Kanton", "Forstzone", "Jahr"]
    for col in text_cols:
         df[col] = df[col].astype(str)

    cube = Cube(dataframe=df, cube_yaml=cube_yaml, environment=ENVIRONMENT, local=True)

    cube.prepare_data()
    cube.write_cube()
    cube.write_observations()
    cube.write_shape()
    # Create concepts

    #struct = pd.read_csv("3_data_preparation/structural_data.csv", encoding="utf-8", sep=",", keep_default_na=False)
    #cube.write_concept("struct", struct)
    #cube.serialize(f"4_data_integration/cube_101_{letter}.ttl")
    cube.serialize(f"C:/Users/Bot3/OneDrive - Berner Fachhochschule/Files BAFU/FS/data_105_3/cube_105_{letter}.ttl")