# 6-Key Programmable Macropad

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![License](https://img.shields.io/badge/license-MIT-green)
![CAD](https://img.shields.io/badge/CAD-Fusion%20360-orange)
![EDA](https://img.shields.io/badge/EDA-KiCad-blue)
![Firmware](https://img.shields.io/badge/Firmware-KMK%20%2F%20CircuitPython-purple)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)

A custom-designed 6-key programmable macropad, developed from scratch for productivity and competitive programming workflows.  
This project covers the full pipeline: electronics design, mechanical CAD, firmware, and documentation.

---

## Features

- 6 fully programmable mechanical keys  
- Custom PCB designed in KiCad  
- Custom 3D printed case and top plate designed in Fusion 360  
- Firmware based on KMK + CircuitPython  
- Optimized for programming & competitive programming shortcuts  
- Designed for easy manufacturing and assembly  

---

## Tools & Technologies

| Area              | Tool / Technology |
|-------------------|-------------------|
CAD (Case & Plate)   | Fusion 360        |
PCB Design           | KiCad             |
Firmware             | KMK (CircuitPython) |
Programming          | Python            |
Version Control      | Git & GitHub      |
Code Editor          | VS Code           |

---

## Project Preview

### Case Design (Fusion 360)
![Case Render](docs/images/case_assembled.png)
![Top Plate](docs/images/case_top.png)

### PCB & Schematic (KiCad)
![Schematic](docs/images/kicad_schematic.png)
![PCB](docs/images/kicad_pcb.png)
![PCB 3D View](docs/images/pcb_3d.png)

---

## Repository Structure
```
├── README.md
├── diary.md
├── firmware/
│ └── main.py
├── pcb/
│ ├── macropadmaluu.kicad_pcb
│ ├── macropadmaluu.kicad_pro
│ └── macropadmaluu.kicad_sch
├── case/
│ ├── topmacropad.f3d
│ ├── casemalumacropad.f3d
└── docs/
│ ├── images/
```

---

## Firmware Overview

The firmware is written using KMK, a Python-based keyboard firmware for CircuitPython.
Example functionality:
- Launch VS Code
- Insert common code templates
- Execute build/run commands
- Useful macros for competitive programming
Located at: ``` firmware/main.py ```
---

## Manufacturing
### PCB
- Gerber files located in: ```pcb/gerbers/```
- Compatible with JLCPCB, PCBWay, etc.
### Case
- Exported files for 3D printing:```case/exports/```
Formats:
- STL (for printing)
- STEP (for editing)

---

## Development Log
A detailed development log is available in: ``` diary.md ```


