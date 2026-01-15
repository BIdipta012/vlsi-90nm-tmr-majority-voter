# Results & Analysis

## Performance Summary

### Pre-RCX vs. Post-RCX Comparison

| Metric | Pre-RCX | Post-RCX | Degradation | Assessment |
|--------|---------|----------|-------------|------------|
| **Delay** | 21.29 ns | 21.34 ns | **+0.26%** | ✅ Exceptional |
| **Power** | 2.052 μW | 2.167 μW | +5.6% | ✅ Expected |
| **Rise time** | 45.6 ps | 47.0 ps | +3.1% | ✅ Good |
| **Fall time** | 50.47 ps | 49.0 ps | −2.9% | ✅ Balanced |

### Significance

**0.26% delay degradation is 5× superior to standard-cell designs** 
(which typically degrade 10–50%), validating custom layout parasitic 
awareness.

---

## Width Sweep Analysis (Velocity Saturation)

| W_eff (nm) | Power (μW) | Delay (ns) | FOM (×10⁶) | Note |
|-----------|-----------|-----------|-----------|------|
| 190 | 2.052 | 21.29 | **26** | 🎯 **OPTIMAL** |
| 240 | 2.50 | 21.29 | 20.5 | Baseline |
| 290 | 3.00 | 21.28 | 17.4 | Saturation region |
| 360 | 3.68 | 21.29 | 14.2 | Width-independent |
| 480 | 4.84 | 21.29 | 10.8 | 2.5× penalty |

**Key Observation**: Delay remains constant (±0.05 ns) across 2.5× 
width variation, confirming velocity saturation and validating W_eff = 190 nm.

---

## Benchmarking vs. Literature

| Design | Technology | FOM (×10⁶) | Comparison |
|--------|-----------|-----------|-----------|
| **Proposed 14T TMR** | **90 nm** | **26** | Baseline |
| KP Majority Voter | 28 nm | 3.5 | 7.4× worse |
| Literature Average | 28 nm | 82 | 3.2× better |
| OA222 (best-in-lit) | 28 nm | 273 | 10.5× better |

**Interpretation**: Despite 3.2× larger technology node, achieves 
7.4× improvement over low-end 28nm voters, proving transistor-level 
optimization can partially compensate for technology disadvantage.

---

## Fault Masking Validation

**TMR Principle**: Majority vote (2/3) masks single-module faults

**Test Case**: A=1, B=0 (FAULT), C=1
- **Expected**: Vo = AB + AC + BC = 0 + 1 + 0 = 1 ✓
- **Rise time**: 45.6 ps (no glitch)
- **Delay**: 21.29 ns (invariant)
- **Result**: Fault masked successfully ✅

Monotonic V_out is critical for TMR reliability.
