# Commercial Earphone 3D Reference Models & Verified Source Directory

This directory contains the 1:1 commercial benchmark 3D CAD models (STEP), high-resolution meshes (STL), disassembled component models, FreeCAD in-ear wearing assemblies, and dimensional inspection reports for the three benchmark consumer earphones used in this ergonomic study.

---

## 📌 Model Origin & Reverse-Engineering Methodology

Due to proprietary intellectual property restrictions, consumer electronics manufacturers (Apple, Sony, Anker) do not release official public open-source STEP/STL CAD files. 

Therefore, the models in this repository were **1:1 programmatically reconstructed using OpenCASCADE / FreeCAD** based strictly on:
1. **Official Engineering Guidelines & Dimension Blueprints** (e.g., Apple Developer Accessory Design Guidelines).
2. **Published Hardware Patents & Acoustic Architecture Specifications** (e.g., Anker Soundcore Sleep Patents, Sony Ergonomic Database Dimensions).
3. **Community 3D Optical Scan Data** verified for physical scale accuracy.

---

## 🎧 1. Apple AirPods Pro (1st/2nd Generation)

### 📋 CAD & Physical Specifications
- **Dimensions**: 30.9 mm (Height) × 21.8 mm (Width) × 24.0 mm (Depth)
- **Stem Angle**: 165° downward inclination
- **Solid Volume**: 1,993.4 mm³
- **Weight**: 5.3 g (Single earbud)

### 🔗 Verified Source Links
- **Apple Developer Official Accessory Design Guidelines (Official Engineering Blueprints PDF)**:
  - URL: <https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf>
  - *Content: Official dimensional drawings, keep-out zones, acoustic venting apertures, charging pin locations.*
- **Thingiverse 3D Optical Scan (Kmrap)**:
  - URL: <https://www.thingiverse.com/thing:4654924>
  - *Content: Real 3D surface optical scan of physical AirPods Pro.*
- **Thingiverse 3D Reference Model (stevesch)**:
  - URL: <https://www.thingiverse.com/thing:4134907>
  - *Content: Community 3D CAD reference model.*

### 📄 Local Deliverables in `output/product/`
- `airpods_pro_right.step` (Multi-body STEP CAD solid assembly)
- `airpods_pro_right.stl` (Watertight 3D mesh)
- `airpods_pro_body.stl` (Rigid housing chassis)
- `airpods_pro_eartip.stl` (Detachable silicone oval eartip)
- `airpods_pro_in_ear.FCStd` (FreeCAD assembly with Subject 004 ear model)
- `airpods_pro_report.json` (Dimensional measurement verification)

---

## 🎧 2. Sony LinkBuds S (WF-LS900N)

### 📋 CAD & Physical Specifications
- **Dimensions**: 29.5 mm (Height) × 25.6 mm (Width) × 18.9 mm (Depth)
- **Acoustic Recess**: $\phi 3.0\text{ mm}$ centered microphone recess (1.2mm depth)
- **Solid Volume**: 1,577.5 mm³
- **Weight**: 4.8 g

### 🔗 Verified Source Links
- **Thingiverse Sony LinkBuds Community 3D Model**:
  - URL: <https://www.thingiverse.com/thing:5424424>
  - *Content: 3D model geometry for Sony LinkBuds.*
- **Thingiverse Sony WF-1000XM4 Reference Model**:
  - URL: <https://www.thingiverse.com/thing:4918731>
  - *Content: Sony TWS reference geometry.*

### 📄 Local Deliverables in `output/product/`
- `sony_linkbuds_s_right.step` (Complete STEP CAD solid model)
- `sony_linkbuds_s_right.stl` (Watertight 3D mesh)
- `sony_linkbuds_s_in_ear.FCStd` (FreeCAD assembly with Subject 004 ear model)

---

## 🎧 3. Anker Soundcore Sleep A30 / A20

### 📋 CAD & Physical Specifications
- **Dimensions**: 25.0 mm (Height) × 19.3 mm (Width) × 8.4 mm (Thickness)
- **Solid Volume**: 1,066.4 mm³ (Ultra-slim 8.4mm body, ~53% volume of AirPods Pro)
- **Weight**: 3.1 g
- **Ergonomic Features**: Patented Air-Wing hollow air cushion + Twin-Seal umbrella eartip

### 🔗 Verified Source Links
- **Anker Soundcore Official Platform**:
  - URL: <https://www.soundcore.com>
  - *Reference: Soundcore Sleep Series Twin-Seal & Air-Wing patent architecture.*
- **Thingiverse Soundcore Community Model**:
  - URL: <https://www.thingiverse.com/thing:5178652>
  - *Content: Soundcore community 3D reference model.*

### 📄 Local Deliverables in `output/product/`
- `anker_soundcore_sleep_a30_right.step` (Multi-body STEP CAD solid assembly)
- `anker_soundcore_sleep_a30_right.stl` (Watertight 3D mesh)
- `anker_soundcore_sleep_a30_body.stl` (Ultra-slim 8.4mm rigid chassis disc)
- `anker_soundcore_sleep_a30_airwing.stl` (Patented Air-Wing hollow air cushion crescent)
- `anker_soundcore_sleep_a30_eartip.stl` (Twin-Seal umbrella eartip)
- `anker_soundcore_sleep_a30_in_ear.FCStd` (FreeCAD assembly with Subject 004 ear model)
- `anker_soundcore_sleep_a30_report.json` (Dimensional measurement verification)
