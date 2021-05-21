import pandas as pd
import sys
import os

dataPath = os.getcwd()+'\\Data\\gapminder.tsv'

data = pd.read_csv(dataPath, sep='\t')

print(data)
