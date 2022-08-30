import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

# #-----------------------------------Data Extraction----------------------------------------#
df= pd.read_csv('data/mandarin_words.csv')
# df.drop(df.columns[-1], axis=1, inplace=True)
df = df.to_dict(orient="records")
print (df)