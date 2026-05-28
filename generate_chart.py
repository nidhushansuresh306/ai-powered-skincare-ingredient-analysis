"""
Generate a clean, academic-style line chart for the PureSkin AI research paper.
Chart: Ingredient Risk Assessment Across Skin Types
Based on actual ingredient database from the project.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# ── Data from the project's ingredient database (seed_db.py) ──
# Counting Safe / Caution / Avoid ingredients per skin type from the 22 seeded ingredients

skin_types = ['Oily', 'Dry', 'Sensitive', 'Acne-Prone']

# Actual counts from the ingredient database:
# For each skin type, count how many ingredients fall into each risk category
safe_counts     = [15, 14, 8,  14]   # Safe
caution_counts  = [4,  4,  6,  5]    # Caution
avoid_counts    = [3,  4,  8,  3]    # Avoid

x = np.arange(len(skin_types))

# ── Create the figure ──
fig, ax = plt.subplots(figsize=(8, 5))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# Plot three lines
ax.plot(x, safe_counts, color='#2ecc71', marker='o', linewidth=2.2, markersize=8,
        label='Safe', zorder=3)
ax.plot(x, caution_counts, color='#f39c12', marker='s', linewidth=2.2, markersize=8,
        label='Caution', zorder=3)
ax.plot(x, avoid_counts, color='#e74c3c', marker='^', linewidth=2.2, markersize=8,
        label='Avoid', zorder=3)

# ── Add data labels on each point ──
for i in range(len(skin_types)):
    ax.annotate(str(safe_counts[i]),    (x[i], safe_counts[i]),    textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, color='#2ecc71', fontweight='bold')
    ax.annotate(str(caution_counts[i]), (x[i], caution_counts[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, color='#f39c12', fontweight='bold')
    ax.annotate(str(avoid_counts[i]),   (x[i], avoid_counts[i]),   textcoords="offset points", xytext=(0, -15), ha='center', fontsize=9, color='#e74c3c', fontweight='bold')

# ── Axis formatting ──
ax.set_xticks(x)
ax.set_xticklabels(skin_types, fontsize=11)
ax.set_xlabel('Skin Type', fontsize=12, fontweight='bold', labelpad=10)
ax.set_ylabel('Number of Ingredients', fontsize=12, fontweight='bold', labelpad=10)
ax.set_title('Ingredient Risk Classification Across Skin Types', fontsize=14, fontweight='bold', pad=15)

ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
ax.set_ylim(0, max(safe_counts) + 3)

# ── Grid and legend ──
ax.grid(True, linestyle='--', alpha=0.3, zorder=0)
ax.legend(loc='upper right', fontsize=10, framealpha=0.9, edgecolor='#cccccc')

# ── Clean spines ──
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#cccccc')
ax.spines['bottom'].set_color('#cccccc')
ax.tick_params(colors='#333333')

plt.tight_layout()
plt.savefig('line_chart_research.png', dpi=300, bbox_inches='tight', facecolor='white')
print("Chart saved as: line_chart_research.png")
plt.close()
