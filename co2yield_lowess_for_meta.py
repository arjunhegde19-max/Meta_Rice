# -*- coding: utf-8 -*-
"""

@author: arjun
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titleweight'] = 'bold'
file = r"E:\Ph.D. IARI\Meta\co2 and yield.xlsx"

df = pd.read_excel(file, sheet_name='CO2')

x = df['CO2'].values
y = df['PCY'].values
order = np.argsort(x)
x = x[order]
y = y[order]

frac = 0.60

fit = lowess(y, x, frac=frac, return_sorted=True)

x_fit = fit[:,0]
y_fit = fit[:,1]

n_boot = 1000

predictions = np.zeros((n_boot, len(x_fit)))

np.random.seed(42)

for i in range(n_boot):

    idx = np.random.choice(len(x), len(x), replace=True)

    xb = x[idx]
    yb = y[idx]

    order = np.argsort(xb)

    xb = xb[order]
    yb = yb[order]

    fit_boot = lowess(yb, xb, frac=frac, return_sorted=True)

    predictions[i] = np.interp(
        x_fit,
        fit_boot[:,0],
        fit_boot[:,1]
    )

lower = np.percentile(predictions,2.5,axis=0)
upper = np.percentile(predictions,97.5,axis=0)

fig, ax = plt.subplots(figsize=(8,6), dpi=900)

ax.scatter(
    x,
    y,
    s=28,
    color='steelblue',
    edgecolor='black',
    linewidth=0.4,
    alpha=0.75,
    label='Data'
)

ax.plot(
    x_fit,
    y_fit,
    color='red',
    linewidth=3,
    label='LOWESS'
)


ax.fill_between(
    x_fit,
    lower,
    upper,
    color='red',
    alpha=0.12,
    label='95% CI'
)



ax.axhline(
    0,
    color='black',
    linestyle='--',
    linewidth=1.5
)

ax.set_xlabel(
    'Change in CO$_2$ concentration (ppm)',
    fontsize=16,
    fontweight='bold'
)

ax.set_ylabel(
    'Percentage Change in Yield (PCY)',
    fontsize=16,
    fontweight='bold'
)

ax.tick_params(axis='both', labelsize=13, width=1.5)

for tick in ax.get_xticklabels():
    tick.set_fontweight('bold')
    tick.set_fontname('Times New Roman')

for tick in ax.get_yticklabels():
    tick.set_fontweight('bold')
    tick.set_fontname('Times New Roman')

legend = ax.legend(
    frameon=False,
    fontsize=13
)

for text in legend.get_texts():
    text.set_fontweight('bold')
    text.set_fontname('Times New Roman')

for spine in ax.spines.values():
    spine.set_linewidth(1.5)

plt.grid(False)

plt.tight_layout()

plt.savefig(
    r"E:\Ph.D. IARI\Meta\Figure_CO2_LOWESS_900dpi.tif",
    dpi=900,
    bbox_inches='tight'
)

plt.savefig(
    r"E:\Ph.D. IARI\Meta\Figure_CO2_LOWESS_900dpi.png",
    dpi=900,
    bbox_inches='tight'
)

plt.show()