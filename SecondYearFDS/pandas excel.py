import numpy as np
import pandas as pd

vaccinationfile= pd.read_csv('vaccination-data.csv')
print(vaccinationfile.index)