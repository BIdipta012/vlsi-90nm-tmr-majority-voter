# Research Paper Summary

## Title
90nm TMR Majority Voter with 0.26% RCX Delay Resilience 
and Minimum-Width FOM Optimality

## Abstract

This paper presents a full-custom 90 nm GPDK 14-transistor (14T) 
Triple Modular Redundancy (TMR) majority voter exploiting velocity 
saturation for minimum-width power optimization...

[Copy your 189-word abstract here from paper]

## Key Contributions

1. **First comprehensive 90nm custom TMR voter** with post-layout 
   DRC/LVS/RCX verification
2. **38% power reduction** through velocity saturation optimization 
   (W_eff = 190 nm)
3. **Exceptional 0.26% RCX resilience** (5× better than standard cells)
4. **7.4× FOM improvement** over low-end 28nm voters despite 3.2× larger tech
5. **Reproducible methodology** using open NCSU GPDK090

## Key Results

| Metric | Pre-RCX | Post-RCX | Status |
|--------|---------|----------|--------|
| Delay | 21.29 ns | 21.34 ns | ✅ 0.26% |
| Power | 2.052 μW | 2.167 μW | ✅ 5.6% |
| FOM | 0.91 fJ | 0.86 fJ | ✅ Optimal |

## Applications

- **Legacy Avionics**: DO-254 certification (15–30 year lifecycle)
- **Radiation-Hardened Design**: Inherent SEU immunity
- **Academic Education**: Open-source GPDK090 accessibility
