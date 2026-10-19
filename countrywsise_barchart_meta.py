

# -*- coding: utf-8 -*-
"""
Country-wise Yield Plot

@author: Arjun
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'


overall = pd.read_excel(file, sheet_name='Overall_Statistics')
country = pd.read_excel(file, sheet_name='Countrywise_Statistics')

scenarios = ['baseline', '2030s', '2060s', '2090s']

countries = [
    'South Asia',
    'Bangladesh',
    'India',
    'Pakistan',
    'Sri Lanka',
    'Nepal'
]

colors = {
    'South Asia':'skyblue',
    'Bangladesh':'red',
    'India':'lightpink',
    'Pakistan':'goldenrod',
    'Sri Lanka':'plum',
    'Nepal':'lightgreen'
}

fig, ax = plt.subplots(figsize=(10,6), dpi=900)

bar_width = 0.13

x = np.arange(len(scenarios))

offsets = np.linspace(-2.5*bar_width,
                      2.5*bar_width,
                      len(countries))

means = []
sds = []

for s in scenarios:

    row = overall[overall['Scenario'] == s]

    if row.empty:
        means.append(np.nan)
        sds.append(np.nan)
    else:
        means.append(row['Mean'].iloc[0])
        sds.append(row['SD'].iloc[0])

ax.bar(
    x+offsets[0],
    means,
    width=bar_width,
    color=colors['South Asia'],
    edgecolor='black',
    linewidth=0.5,
    yerr=sds,
    capsize=4,
    error_kw={
        'elinewidth': 1.0,      # Thickness of error bars
        'capthick': 1.0          # Thickness of caps
    },
    label='South Asia'
)

for j, country_name in enumerate(countries[1:], start=1):

    means = []
    sds = []

    for s in scenarios:

        row = country[
            (country['Scenario'] == s) &
            (country['Country'] == country_name)
        ]

        if row.empty:
            means.append(np.nan)
            sds.append(np.nan)
        else:
            means.append(row['Mean'].iloc[0])
            sds.append(row['SD'].iloc[0])

    ax.bar(
        x+offsets[j],
        means,
        width=bar_width,
        color=colors[country_name],
        edgecolor='black',
        linewidth=0.5,
        yerr=sds,
        capsize=4,
        error_kw={
        'elinewidth': 1.0,      # Thickness of error bars
        'capthick': 1.0          # Thickness of caps
    },
        label=country_name
    )

ax.set_xticks(x)

ax.set_xticklabels(
    ['Baseline','2030s','2060s','2090s'],
    fontsize=14,
    fontweight='bold'
)

ax.set_ylabel(
    r'Yield (kg ha$^{-1}$)',
    fontsize=16,
    fontweight='bold'
)

ax.set_xlabel(
    'Time Periods',
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
    loc='upper center',
    bbox_to_anchor=(0.5, 1.18),
    ncol=3,
    fontsize=12,
    frameon=False,
    columnspacing=1.5,
    handletextpad=0.6
)

for text in legend.get_texts():
    text.set_fontname('Times New Roman')
    text.set_fontweight('bold')

for spine in ax.spines.values():
    spine.set_linewidth(2)

plt.grid(axis='y', linestyle='--', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92])

plt.savefig(
    r"E:\Ph.D. IARI\NS\Countrywise_Yield.png",
    dpi=900,
    bbox_inches='tight'
)

plt.show()