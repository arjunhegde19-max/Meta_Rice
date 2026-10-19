
# -*- coding: utf-8 -*-
"""
@author: arjun
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titleweight'] = 'bold'
 

df = pd.read_excel(file, sheet_name='tmax')

x = df['Tmax change'].values
y = df['PCY'].values

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

x_pred = np.linspace(x.min(), x.max(), 300)
y_pred = intercept + slope * x_pred

n = len(x)

mean_x = np.mean(x)

t = stats.t.ppf(0.975, n-2)

s_err = np.sqrt(np.sum((y-(intercept+slope*x))**2)/(n-2))

conf = t*s_err*np.sqrt(
    1/n +
    ((x_pred-mean_x)**2) /
    np.sum((x-mean_x)**2)
)

upper = y_pred + conf
lower = y_pred - conf

fig, ax = plt.subplots(figsize=(8,6), dpi=900)

# Scatter

ax.scatter(
    x,
    y,
    s=35,
    color='steelblue',
    edgecolor='black',
    linewidth=0.4,
    alpha=0.75,
    label='Data'
)

bins = np.arange(
    np.floor(x.min()),
    np.ceil(x.max())+1,
    1
)

for i in range(len(bins)-1):

    mask = (x>=bins[i]) & (x<bins[i+1])

    xb = x[mask]
    yb = y[mask]

    if len(xb) > 2:

        m,b = np.polyfit(xb,yb,1)

        xx = np.linspace(
            xb.min(),
            xb.max(),
            10
        )

        yy = m*xx+b

        ax.plot(
            xx,
            yy,
            color='maroon',
            linewidth=1.5,
            alpha=0.6
        )

ax.plot(
    x_pred,
    y_pred,
    color='red',
    linewidth=3.5,
    
)

ax.fill_between(
    x_pred,
    lower,
    upper,
    color='red',
    alpha=0.15,
    label='95% CI'
)

ax.set_xlabel(
    'Maximum Temperature Change (°C)',
    fontsize=16,
    fontweight='bold'
)

ax.set_ylabel(
    'Percentage Change in Yield (PCY)',
    fontsize=16,
    fontweight='bold'
)

ax.tick_params(
    axis='both',
    labelsize=13,
    width=1.5
)

for tick in ax.get_xticklabels():
    tick.set_fontname('Times New Roman')
    tick.set_fontweight('bold')

for tick in ax.get_yticklabels():
    tick.set_fontname('Times New Roman')
    tick.set_fontweight('bold')

legend = ax.legend(
    frameon=False,
    fontsize=13
)

for text in legend.get_texts():
    text.set_fontname('Times New Roman')
    text.set_fontweight('bold')

for spine in ax.spines.values():
    spine.set_linewidth(2)

plt.grid(False)
plt.tight_layout()

plt.savefig(
    r"E:\Ph.D. IARI\Meta\Tmax_Linear_bins.png",
    dpi=900,
    bbox_inches='tight'
)

plt.show()