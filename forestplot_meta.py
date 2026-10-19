
# -*- coding: utf-8 -*-
"""
Forest Plot of Climate Variables on PCY

@author: Arjun
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titleweight'] = 'bold'

df = pd.read_excel(r"E:\Ph.D. IARI\Meta\Forest_new.xlsx")

variables = {
    'Tmax change': 'pcy-tmax',
    'Tmin change': 'pcy-tmin',
    'Precipitation change': 'pcy-preciptn',
    'CO$_2$ change': 'pcy-co2'
}

summary = []

for var_name, pcy_col in variables.items():

    values = df[pcy_col].replace([np.inf, -np.inf], np.nan).dropna()

    mean = values.mean()
    std = values.std()

    n = len(values)

    ci_lower = mean - 1.96 * std / np.sqrt(n)
    ci_upper = mean + 1.96 * std / np.sqrt(n)

    summary.append([
        var_name,
        mean,
        ci_lower,
        ci_upper
    ])

summary_df = pd.DataFrame(
    summary,
    columns=['Variable','Mean','Lower','Upper']
)

summary_df = summary_df.iloc[::-1]

fig, ax = plt.subplots(figsize=(8,6), dpi=900)

ax.errorbar(
    summary_df['Mean'],
    summary_df['Variable'],

    xerr=[
        summary_df['Mean']-summary_df['Lower'],
        summary_df['Upper']-summary_df['Mean']
    ],

    fmt='o',

    markersize=8,

    color='darkblue',

    markerfacecolor='darkblue',

    markeredgecolor='darkblue',

    ecolor='black',

    elinewidth=2,

    capsize=6,

    capthick=2
)

ax.axvline(
    x=0,
    color='gray',
    linestyle='--',
    linewidth=2
)

ax.set_xlabel(
    'Average Percentage Change in Yield (%)',
    fontsize=16,
    fontweight='bold'
)

ax.set_ylabel(
    'Climate Variables',
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

ax.grid(
    True,
    axis='x',
    linestyle='--',
    linewidth=1,
    alpha=0.5
)

for spine in ax.spines.values():
    spine.set_linewidth(2)

plt.tight_layout()

plt.savefig(
    r"E:\Ph.D. IARI\Meta\Forest_Plot_PCY.png",
    dpi=900,
    bbox_inches='tight'
)

plt.show()