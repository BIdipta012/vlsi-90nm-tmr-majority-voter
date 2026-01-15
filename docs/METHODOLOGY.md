# Design Flow & Methodology

## Complete VLSI Flow

┌─────────────────┐
│ 1. SCHEMATIC │ Cadence Virtuoso
│ Design │ 14T voter netlist
└────────┬────────┘
↓
┌─────────────────┐
│ 2. PRE-RCX │ Spectre APS simulator
│ SIMULATION │ Transient analysis
└────────┬────────┘
↓
┌─────────────────┐
│ 3. LAYOUT │ Hierarchical design
│ Design │ Common-centroid matching
└────────┬────────┘
↓
┌─────────────────┐
│ 4. VERIFICATION │ Calibre PVS
│ (DRC/LVS) │ Zero violations
└────────┬────────┘
↓
┌─────────────────┐
│ 5. PARASITIC │ RCX extraction
│ EXTRACTION │ (av_extracted_view)
└────────┬────────┘
↓
┌─────────────────┐
│ 6. POST-RCX │ Identical testbench
│ SIMULATION │ Measure resilience
└────────┬────────┘
↓
┌─────────────────┐
│ 7. ANALYSIS │ FOM, comparisons
│ & REPORTING │ Benchmarking
└─────────────────┘


## Simulation Settings

- **Simulator**: Spectre APS (accurate-moderate setting)
- **reltol**: 1e-3 (relative tolerance)
- **abstol**: 1e-12 (absolute current tolerance)
- **Load**: 1kΩ resistor || 100 fF capacitor
- **Frequency**: 100 MHz
- **Supply**: 1.2V nominal

## Verification Checklist

✅ **DRC**: Design Rule Check (0 violations)
✅ **LVS**: Layout vs. Schematic (100% match)
✅ **RCX**: Parasitic extraction completed
✅ **Pre-RCX**: Delay & power measured
✅ **Post-RCX**: Resilience validated
