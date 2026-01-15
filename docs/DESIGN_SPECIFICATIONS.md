# Design Specifications

## Circuit Overview

**14-Transistor TMR Majority Voter**

A ──┐
├─→ 6T NAND Core ─→ Vo = AB + AC + BC
B ──┤
└─→ 6T Complementary
+ 2T Output Buffer
C ──┐
└─→ Common-centroid layout


## Device Sizing

| Device | W/L (nm) | Type | Purpose |
|--------|----------|------|---------|
| NAND pull-up | 240/90 | HVT | Low power |
| NAND pull-down | 190/90 | HVT | Minimum-width (saturation) |
| Comp. stage | 240/90 | HVT | Symmetry |
| Output inverter | 360/90 | LVT | Drive strength |

## Layout Specifications

Dimensions: 14.8 μm × 25.0 μm
Area: 167.2 μm²
Matching: Common-centroid (HVT core)
Metal layers: M1–M3 (routing), M4 (power)
VDD rail: Top (M4)
GND rail: Bottom (M4)


## Process Parameters

- **Technology**: NCSU GPDK090 v4.6
- **Feature size**: 90 nm (nominal)
- **Supply voltage**: 1.2V
- **Temperature**: 27°C (nominal)
- **Vth model**: BSIM4 (level 54)

## Performance

| Parameter | Value | Unit |
|-----------|-------|------|
| **Propagation Delay** | 21.29 | ns |
| **Rise Time** | 45.6 | ps |
| **Fall Time** | 50.47 | ps |
| **Dynamic Power** | 2.052 | μW |
| **Leakage Power** | ~40 | pA/tr. |
| **FOM (fJ)** | 0.91 | — |
| **FOM (normalized)** | 26 | ×10⁶ |
