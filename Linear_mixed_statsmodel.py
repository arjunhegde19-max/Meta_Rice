!pip install statsmodels
from google.colab import drive
import pandas as pd
import matplotlib.pyplot as plt

drive.mount('/content/drive')


df = pd.read_excel('/content/drive/MyDrive/Meta_Rice_RA.xlsx', sheet_name='lmef')
print(df)
import statsmodels.formula.api as smf

df['Vty_recoded'] = df['Vty'].map({'yes': 1, 'yesno': 0.5, 'no': 0})
df['Ad_recoded']  = df['Ad'].map({'yes': 1, 'no': 0})

model = smf.mixedlm("PCY ~ Tmax + Tmin + Precipitn + CO2 + Season + C(Ad) + Vty",
                   data=df, groups=df["Climatemodel"],
                   re_formula="~Cropmodel + Scenario")
result = model.fit()
print(result.summary())