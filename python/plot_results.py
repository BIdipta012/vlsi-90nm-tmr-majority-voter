#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd

# Load data
data = pd.read_csv('../results/tables/table2_width_sweep.csv')

# Plot width sweep
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Power vs. Width
ax1.plot(data['W_eff (nm)'], data['Power (μW)'], 'o-', linewidth=2)
ax1.set_xlabel('W_eff (nm)')
ax1.set_ylabel('Power (μW)')
ax1.set_title('Power Scaling with Transistor Width')
ax1.grid(True)

# FOM vs. Width
ax2.plot(data['W_eff (nm)'], data['FOM (×10^6)'], 's-', linewidth=2, color='green')
ax2.axvline(x=190, color='red', linestyle='--', label='Optimal (190 nm)')
ax2.set_xlabel('W_eff (nm)')
ax2.set_ylabel('FOM (×10⁶)')
ax2.set_title('FOM vs. Transistor Width')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig('../results/figures/fig5_width_sweep.png', dpi=300)
print("Plot saved: fig5_width_sweep.png")
