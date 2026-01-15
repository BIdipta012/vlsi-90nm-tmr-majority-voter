#!/usr/bin/env python3
"""
FOM Calculator: Power-Delay-Area Efficiency Metric
"""

def calculate_fom(power_uw, delay_ns, area_um2):
    """
    Calculate Figure of Merit (FOM) using Balasubramanian formula
    
    FOM = (100 × P × D) / A
    
    Lower FOM = Better efficiency
    """
    fom = (100 * power_uw * delay_ns) / area_um2
    return fom

# Your data
power_preRCX = 2.052  # μW
delay_preRCX = 21.29  # ns
area = 167.2  # μm²

# Calculate
fom_preRCX = calculate_fom(power_preRCX, delay_preRCX, area)
print(f"Pre-RCX FOM: {fom_preRCX:.2f} × 10⁶")
print(f"Pre-RCX FOM (fJ): {fom_preRCX * 1e-6 * 1e15:.2f} fJ")

# Post-RCX
power_postRCX = 2.167  # μW
delay_postRCX = 21.34  # ns
fom_postRCX = calculate_fom(power_postRCX, delay_postRCX, area)
print(f"Post-RCX FOM: {fom_postRCX:.2f} × 10⁶")
