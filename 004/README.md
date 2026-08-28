# Custom Ergonomic Sleep Earphone 3D CAD Library (Subject 004 Right Ear)

This repository contains the complete 3D CAD engineering models, watertight STL meshes, internal driver cavity designs, soft silicone sleeves, FreeCAD assembly simulations, and dimensional inspection reports for **Subject 004 Right Ear**, custom-engineered across three distinct design generations (**v1**, **v2**, **v3**).

---

## 🎯 Initial Design Requirements & Engineering Constraints

The 3D models were designed based on the following three mandatory constraints and design criteria:

1. **Dedicated for Sleeping — Zero Protrusion (Flush In-Concha)**:
   - The earphone must not protrude beyond the ear's outer anatomical boundaries (Antihelix ridge / Tragus).
   - When the user sleeps on their side on a flat pillow, head weight is distributed across the surrounding soft facial and auricular tissue without transferring concentrated vertical pressure onto the earphone chassis, eliminating side-sleeping cartilage pain.

2. **Miniaturized Acoustic Driver (Music Quality Not Critical)**:
   - Since the primary application is sleep aid (white noise, masking sounds, binaural beats, and alarms) rather than high-fidelity music reproduction, an ultra-compact **5.0 × 3.0 × 2.2 mm Micro Balanced Armature (Micro-BA)** driver is used.
   - This releases internal volume constraints and allows compressing the overall shell thickness down to **2.8 ~ 3.2 mm**, enabling deep seating into the Cavum conchae.

3. **Anti-Drop Retention vs. Dynamic Auricular Deformation Relief**:
   - **Retention**: Multi-point anatomical anchoring (Canal + Cavum + Cymba) prevents dislodging when the user rolls over or changes sleeping postures during the night.
   - **Anti-Pressure Pain**: When tossing and turning causes the flexible ear cartilage to compress and deform under head weight, the chassis boundaries must NOT dig into or pinch the auricular perichondrium.
   - **Multi-Material Separation**: Rigid polymer housing is strictly separated from **soft liquid silicone rubber components (Shore A 30)** with **0.35 ~ 0.45 mm dynamic perimeter clearance** to cushion all dynamic cartilage deformations.

---

## 🎨 Strong Brand Prototype Styling & Multi-Material Architecture

To make each version visually distinct and instantly recognizable while maintaining 100% anatomical ear-concha fit on the inner side, the outer faceplates and soft components are deeply customized:

### 🎧 v1: Apple AirPods Pro Archetype
- **Outer Faceplate Styling**: Signature AirPods Pro **organic teardrop curvature** with a **lateral Force Sensor pinch flat notch** and top acoustic mesh recess.
- **Rigid Chassis**: `004_v1_rigid_chassis_solid.stl` & `004_v1_rigid_chassis_hollow.stl` (Recessed to $X = -0.5\text{ mm}$, 2.0mm pillow gap).
- **Soft Silicone Component**: `004_v1_soft_silicone_sleeve.stl` (AirPods-style elliptical umbrella flange + 0.6mm soft perimeter collar).

### 🎧 v2: Sony LinkBuds S Archetype
- **Outer Faceplate Styling**: Signature Sony **dual-curved organic pebble/bean profile** with a **centered circular acoustic microphone depression** ($\phi 3.0\text{ mm}$, depth 1.2mm).
- **Rigid Chassis**: `004_v2_rigid_chassis_solid.stl` & `004_v2_rigid_chassis_hollow.stl` (Recessed to $X = 0.0\text{ mm}$, 2.5mm pillow gap).
- **Soft Silicone Component**: `004_v2_soft_silicone_sleeve.stl` (Sony-style 0.5mm ultra-soft pebble silicone cushioning sleeve).

### 🌟 v3: Anker Soundcore Sleep A30 Archetype (Ultimate Sleep Architecture)
- **Outer Faceplate Styling**: Signature Anker **ultra-slim concentric metal disc faceplate** ($X = +0.5\text{ mm}$, 3.0mm pillow gap) with peripheral mounting rim.
- **Rigid Chassis**: `004_v3_rigid_chassis_solid.stl` & `004_v3_rigid_chassis_hollow.stl` (Most compact 2,129.0 mm³ solid volume).
- **Soft Silicone Component**: `004_v3_soft_silicone_sleeve.stl` (**Patented Air-Wing hollow air-cushioned crescent wing** extending into the Cymba conchae to passively compress under head weight, plus Twin-Seal umbrella tips).

---

## 📊 Three-Generation Evolution & Technical Comparison Matrix

| Technical Metric | 🎧 **v1 (Apple AirPods Pro Archetype)** | 🎧 **v2 (Sony LinkBuds S Archetype)** | 🌟 **v3 (Anker Soundcore Sleep A30 Archetype)** |
| :--- | :--- | :--- | :--- |
| **Design Archetype** | Apple AirPods Pro (1st/2nd Gen) | Sony LinkBuds S (WF-LS900N, 4.8g) | **Anker Soundcore Sleep A30 (3.1g)** |
| **Outer Chassis Styling** | Teardrop Dome + Force Sensor Notch | Organic Pebble + Recessed Mic Chamber | **Ultra-slim Disc + Peripheral Air-Wing Rim** |
| **Solid Chassis Volume** | 2,255.6 mm³ | 2,191.8 mm³ | **2,129.0 mm³ (Most Compact)** |
| **Faceplate Reference Plane** | $X = -0.5\text{ mm}$ (1.0 mm below antihelix) | $X = 0.0\text{ mm}$ (1.5 mm below antihelix) | **$X = +0.5\text{ mm}$ (2.0 mm deep recession)** |
| **Pillow Safety Clearance** | **2.0 mm** (Clear of pillow contact) | **2.5 mm** (+25% safety margin) | **3.0 mm (Maximum side-sleeping gap)** |
| **Rigid Housing Component** | `004_v1_rigid_chassis_*.stl` | `004_v2_rigid_chassis_*.stl` | `004_v3_rigid_chassis_*.stl` |
| **Soft Silicone Component** | `004_v1_soft_silicone_sleeve.stl` | `004_v2_soft_silicone_sleeve.stl` | `004_v3_soft_silicone_sleeve.stl` (Air-Wing) |
| **Deformation Relief Mechanism** | $R \ge 1.5\text{ mm}$ Filleted Outer Edges | Smooth Organic Pebble Contours | 🌟 **Passive Air-Chamber Compression upon Ear Deformation** |
| **Perimeter Dynamic Clearance** | 0.35 mm | 0.40 mm | **0.45 mm (Maximum Softness)** |
| **Driver Chamber Spec** | 5.0 × 3.0 × 2.2 mm Micro-BA | 5.0 × 3.0 × 2.2 mm Micro-BA | 5.0 × 3.0 × 2.2 mm Micro-BA |
| **Acoustic / Vent Dimensions** | $\phi 2.2\text{ mm}$ Nozzle, $\phi 0.8\text{ mm}$ Vent | $\phi 2.2\text{ mm}$ Nozzle, $\phi 0.8\text{ mm}$ Vent | $\phi 2.2\text{ mm}$ Nozzle, $\phi 0.8\text{ mm}$ Vent |

---

## 📁 Repository Directory Structure & File Index

```text
004/
├── v1_AirPodsPro/                                  # Generation 1: Derived from Apple AirPods Pro Prototype
│   ├── 004_v1_sleep_earphone_assembly.step        # Multi-Body STEP Solid CAD Model (Rigid Shell + Soft Sleeve)
│   ├── 004_v1_rigid_chassis_solid.stl            # Rigid Polymer Housing Solid Mesh (Watertight)
│   ├── 004_v1_rigid_chassis_hollow.stl           # Rigid Polymer Housing with Micro-BA Cavity
│   ├── 004_v1_soft_silicone_sleeve.stl           # Soft Silicone Outer Sleeve (Shore A 30)
│   ├── 004_v1_sleep_earphone_colored.ply         # 4-Color Anatomically Segmented Inspection Mesh
│   ├── 004_v1_sleep_earphone_in_ear_simulation.FCStd # FreeCAD Multi-Body Wearing & Pillow Simulation
│   ├── 004_v1_sleep_earphone_design_report.json  # Quantitative Dimensional Report
│   ├── 004_v1_airpods_pro_reference_1to1.step    # 1:1 Apple AirPods Pro Reference STEP Model
│   ├── 004_v1_airpods_pro_reference_1to1.stl     # 1:1 Apple AirPods Pro Reference STL Mesh
│   ├── 004_v1_airpods_pro_body.stl               # AirPods Pro Main Chassis Component STL
│   ├── 004_v1_airpods_pro_eartip.stl             # AirPods Pro Silicone Eartip Component STL
│   └── 004_v1_airpods_pro_in_ear.FCStd           # FreeCAD Project: 1:1 AirPods Pro Wearing Simulation
│
├── v2_SonyLinkBudsS/                               # Generation 2: Derived from Sony LinkBuds S (WF-LS900N) Prototype
│   ├── 004_v2_sleep_earphone_assembly.step        # Multi-Body STEP Solid CAD Model (Rigid Shell + Soft Sleeve)
│   ├── 004_v2_rigid_chassis_solid.stl            # Rigid Polymer Housing Solid Mesh (Watertight, 2,191.8 mm³)
│   ├── 004_v2_rigid_chassis_hollow.stl           # Rigid Polymer Housing with Micro-BA Cavity
│   ├── 004_v2_soft_silicone_sleeve.stl           # Soft Pebble Silicone Cushioning Sleeve (Shore A 30)
│   ├── 004_v2_sleep_earphone_colored.ply         # 4-Color Anatomically Segmented Inspection Mesh
│   ├── 004_v2_sleep_earphone_in_ear_simulation.FCStd # FreeCAD Multi-Body Wearing & 2.5mm Pillow Simulation
│   ├── 004_v2_sleep_earphone_design_report.json  # Quantitative Dimensional Report
│   ├── 004_v2_sony_linkbuds_s_reference_1to1.step# 1:1 Sony LinkBuds S Reference STEP Model
│   ├── 004_v2_sony_linkbuds_s_reference_1to1.stl # 1:1 Sony LinkBuds S Reference STL Mesh
│   └── 004_v2_sony_linkbuds_s_in_ear.FCStd       # FreeCAD Project: 1:1 Sony LinkBuds S Wearing Simulation
│
├── v3_AnkerSleepA30/                              # 🌟 Generation 3: Derived from Anker Soundcore Sleep A30 Prototype
│   ├── 004_v3_sleep_earphone_assembly.step        # Multi-Body STEP Solid CAD Model (Rigid Shell + Soft Sleeve)
│   ├── 004_v3_rigid_chassis_solid.stl            # Rigid Polymer Housing Solid Mesh (Watertight, 2,129.0 mm³)
│   ├── 004_v3_rigid_chassis_hollow.stl           # Rigid Polymer Housing with Micro-BA Cavity
│   ├── 004_v3_soft_silicone_sleeve.stl           # Patented Air-Wing Hollow Air-Cushioned Silicone Sleeve
│   ├── 004_v3_sleep_earphone_colored.ply         # 4-Color Anatomically Segmented Inspection Mesh
│   ├── 004_v3_sleep_earphone_in_ear_simulation.FCStd # FreeCAD Multi-Body Wearing & 3.0mm Pillow Simulation
│   ├── 004_v3_sleep_earphone_design_report.json  # 3-Generation Comparative Verification Report
│   ├── 004_v3_anker_sleep_a30_reference_1to1.step# 1:1 Anker Soundcore Sleep A30 Reference STEP Model
│   ├── 004_v3_anker_sleep_a30_reference_1to1.stl # 1:1 Anker Soundcore Sleep A30 Reference STL Mesh
│   ├── 004_v3_anker_sleep_a30_airwing.stl        # Anker A30 Air-Wing Component STL
│   ├── 004_v3_anker_sleep_a30_eartip.stl         # Anker A30 Twin-Seal Umbrella Eartip Component STL
│   └── 004_v3_anker_sleep_a30_in_ear.FCStd       # FreeCAD Project: 1:1 Anker Sleep A30 Wearing Simulation
│
└── reference_ear/                                  # Subject 004 Anatomical Benchmark Data
    ├── 004_human_ear_right_solid.stl              # 100% Watertight 3D Human Ear Solid (Poisson Reconstruction)
    ├── 004_concha_basin.stl                       # Segmented Concha Basin (Cavum + Cymba + Acoustic Meatus)
    └── 004_canal_entrance.stl                     # Segmented Ear Canal Entrance Funnel
```

---

## 🔬 Viewing & Simulation Guide in FreeCAD

1. **Opening Simulation Projects**:
   - Open `004_v3_sleep_earphone_in_ear_simulation.FCStd` directly in FreeCAD (v0.21 or v1.1+).
2. **Multi-Material Object Inspection**:
   - `Rigid_Polymer_Chassis_004_v3`: Represents the internal structural core housing the electronics.
   - `Soft_Silicone_Sleeve_004_v3_ShoreA30`: Represents the flexible silicone skin with the crescent Air-Wing air cushion.
   - `Human_Ear_004_Scan`: Human ear anatomy. Set transparency to 70% (`Ctrl + D`) for internal interference inspection.
   - `Simulated_Pillow_Plane_Gap_3_0mm`: Tangent contact plane at $X = -2.5\text{ mm}$ proving complete zero-contact side-sleeping clearance.
