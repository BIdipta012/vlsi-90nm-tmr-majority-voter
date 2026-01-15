# 90nm TMR Majority Voter: Velocity Saturation Optimization

![VLSI](https://img.shields.io/badge/VLSI-Design-blue)
![Cadence](https://img.shields.io/badge/Tool-Cadence-brightgreen)
![90nm](https://img.shields.io/badge/Technology-90nm%20CMOS-orange)

## 📋 Overview

Full-custom design and characterization of a **14-transistor Triple Modular 
Redundancy (TMR) majority voter** in 90nm CMOS technology, demonstrating 
exceptional post-layout resilience through velocity saturation exploitation.

**Key Achievement**: 0.26% delay degradation post-parasitic extraction 
(5× superior to standard-cell designs)

---

## 🎯 Quick Results

| Metric | Value |
|--------|-------|
| **Delay** | 21.29 ns |
| **Power** | 2.052 μW |
| **RCX Resilience** | 0.26% degradation |
| **Layout Area** | 167.2 μm² |
| **FOM** | 0.91 fJ (26 × 10⁶) |

---

## 📁 Folder Guide

| Folder | Contents |
|--------|----------|
| `docs/` | Technical documentation |
| `design/` | Schematics, layouts, netlists |
| `simulations/` | Testbenches, configs, results |
| `results/` | Figures, tables, analysis |
| `paper/` | Research paper PDF |
| `python/` | Data processing scripts |

---

## 🚀 Getting Started

```bash
# View performance results
cat results/tables/table1_performance.csv

# Run analysis
python python/fom_calculator.py
