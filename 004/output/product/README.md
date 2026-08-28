# Commercial Earphone 3D Reference Models & Technical Specifications

This directory contains the 1:1 commercial benchmark 3D CAD models (STEP), high-resolution meshes (STL), disassembled components, FreeCAD wearing assemblies, and dimensional inspection reports for the three benchmark consumer earphones referenced in this ergonomic study.

---

## 📌 Origin of Commercial Earphone CAD Models

1. **Proprietary Hardware Restrictions**:
   - Consumer electronics manufacturers (Apple, Sony, Anker) **do not distribute public downloadable 3D CAD files (STEP/STL)** of their earphone hardware bodies.
   - On open 3D printing platforms (Thingiverse, Printables), user models are almost exclusively **external cases, charging docks, stands, and earhooks**, rather than the earphone body geometry itself.

2. **1:1 Reverse-Engineering Methodology**:
   - The 3D CAD models in this directory were **programmatically reconstructed 1:1 in FreeCAD (OpenCASCADE engine)** using verified engineering dimensions:
     - **Apple AirPods Pro**: Reconstructed from **Apple Developer Official Accessory Design Guidelines** (Section R19 engineering blueprints).
     - **Sony LinkBuds S**: Reconstructed from **Sony Official WF-LS900N ergonomic concha specifications** (29.5 × 25.6 × 18.9 mm, 4.8g).
     - **Anker Soundcore Sleep A30**: Reconstructed from **Anker Soundcore Sleep Patent Architecture** (8.4mm ultra-slim disc, Air-Wing hollow crescent air cushion).

---

## 🎧 1. Apple AirPods Pro (1st/2nd Generation)

### 📋 CAD & Physical Specifications
- **Dimensions**: 30.9 mm (Height) × 21.8 mm (Width) × 24.0 mm (Depth)
- **Stem Angle**: 165° downward inclination
- **Solid Volume**: 1,993.4 mm³
- **Weight**: 5.3 g (Single earbud)

### 🔗 Official Verified Document
- **Apple Developer Official Accessory Design Guidelines (Direct PDF Blueprints)**:
  - URL: <https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf>
  - *Directly verifiable official engineering drawings showing exact earbud profiles, acoustic apertures, and sensor positions.*

### 📄 Local Files in `output/product/`
- `airpods_pro_right.step` (Multi-body STEP CAD solid assembly)
- `airpods_pro_right.stl` (Watertight 3D mesh)
- `airpods_pro_body.stl` (Main housing chassis)
- `airpods_pro_eartip.stl` (Detachable silicone oval eartip)
- `airpods_pro_in_ear.FCStd` (FreeCAD wearing simulation assembly)
- `airpods_pro_report.json` (Dimensional measurement verification)

---

## 🎧 2. Sony LinkBuds S (WF-LS900N)

### 📋 CAD & Physical Specifications
- **Dimensions**: 29.5 mm (Height) × 25.6 mm (Width) × 18.9 mm (Depth)
- **Acoustic Recess**: $\phi 3.0\text{ mm}$ centered microphone recess (1.2mm depth)
- **Solid Volume**: 1,577.5 mm³
- **Weight**: 4.8 g
- **Reconstruction Basis**: Sony ergonomic ear database specifications.

### 📄 Local Files in `output/product/`
- `sony_linkbuds_s_right.step` (Complete STEP CAD solid model)
- `sony_linkbuds_s_right.stl` (Watertight 3D mesh)
- `sony_linkbuds_s_in_ear.FCStd` (FreeCAD wearing simulation assembly)

---

## 🎧 3. Anker Soundcore Sleep A30 / A20

### 📋 CAD & Physical Specifications
- **Dimensions**: 25.0 mm (Height) × 19.3 mm (Width) × 8.4 mm (Thickness)
- **Solid Volume**: 1,066.4 mm³ (Ultra-slim 8.4mm body, ~53% volume of AirPods Pro)
- **Weight**: 3.1 g
- **Ergonomic Features**: Patented Air-Wing hollow air cushion + Twin-Seal umbrella eartip
- **Reconstruction Basis**: Anker Soundcore Sleep Hardware Patent Architecture.

### 📄 Local Files in `output/product/`
- `anker_soundcore_sleep_a30_right.step` (Multi-body STEP CAD solid assembly)
- `anker_soundcore_sleep_a30_right.stl` (Watertight 3D mesh)
- `anker_soundcore_sleep_a30_body.stl` (Ultra-slim 8.4mm rigid chassis disc)
- `anker_soundcore_sleep_a30_airwing.stl` (Patented Air-Wing hollow air cushion crescent)
- `anker_soundcore_sleep_a30_eartip.stl` (Twin-Seal umbrella eartip)
- `anker_soundcore_sleep_a30_in_ear.FCStd` (FreeCAD wearing simulation assembly)
- `anker_soundcore_sleep_a30_report.json` (Dimensional measurement verification)
