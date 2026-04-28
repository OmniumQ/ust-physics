# 🌌 UST-Physics v5.0

**Professional Physics Library: GR + QFT + UST + Quantum Gravity**

---

## 📦 Installation

```bash
pip install ust-physics
```

## 🚀 Quick Start

```python
import ust_physics as ust

# Display constants
ust.constants.info()

# Verify theorems
ust.theorems.verify_all()

# Quantum Gravity
from ust_physics.quantum_gravity import BlackHoleQuantum
from ust_physics.constants import M_SUN

bh = BlackHoleQuantum(mass=M_SUN)
T_H = bh.hawking_temperature_ust()
print(f"Hawking Temperature (UST): {T_H:.3e} K")
```

## 📚 Modules

- **constants** - Physical constants with UST values
- **theorems** - UST theorems T1-T28
- **utils** - Helper functions
- **gr** - General Relativity
- **qft** - Quantum Field Theory
- **models** - Physics models 
- **quantum_gravity** - Quantum gravity with UST corrections ⭐NEW

### Quantum Gravity Features:
- Planck scale corrections
- Black hole quantum thermodynamics
- Loop quantum gravity (17D structure)
- Graviton properties
- Holographic principle & AdS/CFT

---

## 📄 License

Copyright (c) 2026 Niyazi ÖCAL
Patent: TR 2026/003258
