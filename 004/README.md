# Custom Ergonomic Sleep Earphone 3D CAD Library (Subject 004 Right Ear)

This repository contains the complete 3D CAD engineering models, watertight STL meshes, internal driver cavity designs, soft silicone sleeves, FreeCAD assembly simulations, and dimensional inspection reports for **Subject 004 Right Ear**, custom-engineered across three design generations (**v1**, **v2**, **v3**).

---

## 🎯 Initial Design Requirements & Engineering Constraints

The 3D models were designed based on the following three mandatory constraints and design criteria:

1. **Dedicated for Sleeping — Zero Protrusion (Flush In-Concha)**:
   - The earphone must not protrude beyond the ear's outer anatomical boundaries (Antihelix ridge / Tragus).
   - When the user sleeps on their side on a flat pillow, head weight must be distributed across the surrounding soft facial/auricular tissue without transferring concentrated vertical pressure onto the earphone chassis, eliminating side-sleeping cartilage pain.

2. **Miniaturized Acoustic Driver (Music Quality Not Critical)**:
   - Since the primary application is sleep aid (white noise, masking sounds, binaural beats, and alarms) rather than high-fidelity music reproduction, an ultra-compact **5.0 × 3.0 × 2.2 mm Micro Balanced Armature (Micro-BA)** or ultra-slim 5mm dynamic driver is used.
   - This releases internal volume constraints and allows compressing the overall shell thickness down to **2.8 ~ 3.2 mm**, enabling deep seating into the Cavum conchae.

3. **Anti-Drop Retention vs. Dynamic Auricular Deformation Relief**:
   - **Retention**: The earphone must anchor firmly inside the ear concha to prevent dislodging when the user rolls over or changes sleeping postures during the night.
   - **Anti-Pressure Pain**: When tossing and turning causes the flexible ear cartilage to compress and deform under head weight, the chassis boundaries must NOT dig into or pinch the auricular perichondrium.
   - **Engineering Solution**: Multi-point anatomical anchoring (Canal + Cavum + Cymba) combined with **0.35 ~ 0.45 mm dynamic deformation clearance** and **air-cushioned / soft-durometer silicone outer sleeves (Shore A 30)**.

---

## 📊 Three-Generation Evolution & Technical Comparison Matrix

| Technical Metric | 🎧 **v1 (Apple AirPods Pro Archetype)** | 🎧 **v2 (Sony LinkBuds S Archetype)** | 🌟 **v3 (Anker Soundcore Sleep A30 Archetype)** |
| :--- | :--- | :--- | :--- |
| **Design Archetype** | Apple AirPods Pro (1st/2nd Gen) | Sony LinkBuds S (WF-LS900N, 4.8g) | **Anker Soundcore Sleep A30 (3.1g)** |
| **Chassis Archetype Form** | Stemless Organic Head Bulb | Ultra-compact Organic Pebble/Bean | **Ultra-slim Disc + Crescent Cushion Wing** |
| **Solid Shell Volume** | 2,255.6 mm³ | 2,191.8 mm³ | **2,129.0 mm³ (Most Compact)** |
| **Faceplate Reference Plane** | $X = -0.5\text{ mm}$ (1.0 mm below antihelix) | $X = 0.0\text{ mm}$ (1.5 mm below antihelix) | **$X = +0.5\text{ mm}$ (2.0 mm deep recession)** |
| **Pillow Safety Clearance** | **2.0 mm** (Clear of pillow contact) | **2.5 mm** (+25% safety margin) | **3.0 mm (Maximum side-sleeping gap)** |
| **Anti-Drop Retention Mechanism** | Integrated Rigid Cymba Wing | Low-profile Organic Concha Wing | 🌟 **Patented Air-Wing Hollow Air-Cushion Wing** |
| **Deformation Relief Mechanism** | $R \ge 1.5\text{ mm}$ Filleted Outer Edges | Smooth Organic Pebble Contours | 🌟 **Passive Air-Chamber Compression upon Ear Deformation** |
| **Eartip Architecture** | Short-axis Oval Silicone Eartip | Hybrid Circular Silicone Tip | **Twin-Seal Dual-Layer Umbrella Silicone Eartip** |
| **Perimeter Dynamic Clearance** | 0.35 mm | 0.40 mm | **0.45 mm (Maximum Softness)** |
| **Driver Chamber Spec** | 5.0 × 3.0 × 2.2 mm Micro-BA | 5.0 × 3.0 × 2.2 mm Micro-BA | 5.0 × 3.0 × 2.2 mm Micro-BA |
| **Acoustic / Vent Dimensions** | $\phi 2.2\text{ mm}$ Nozzle, $\phi 0.8\text{ mm}$ Vent | $\phi 2.2\text{ mm}$ Nozzle, $\phi 0.8\text{ mm}$ Vent | $\phi 2.2\text{ mm}$ Nozzle, $\phi 0.8\text{ mm}$ Vent |

---

## 📁 Repository Directory Structure & File Index

```text
004/
├── v1_AirPodsPro/                                  # Generation 1: Derived from Apple AirPods Pro Prototype
│   ├── 004_v1_sleep_earphone_assembly.step        # Engineering STEP Solid CAD Model
│   ├── 004_v1_sleep_earphone_solid.stl           # 100% Watertight Solid Shell Mesh
│   ├── 004_v1_sleep_earphone_hollow.stl          # Internal Micro-BA Driver Chamber Hollow Mesh
│   ├── 004_v1_sleep_earphone_silicone_sleeve.stl # 0.6mm Soft Protective Silicone Outer Sleeve
│   ├── 004_v1_sleep_earphone_colored.ply         # 4-Color Anatomically Segmented Inspection Mesh
│   ├── 004_v1_sleep_earphone_in_ear_simulation.FCStd # FreeCAD In-Ear Wearing & Pillow Clearance Simulation
│   ├── 004_v1_sleep_earphone_design_report.json  # Quantitative Dimensional & Verification Report
│   ├── 004_v1_airpods_pro_reference_1to1.step    # 1:1 Apple AirPods Pro Reference STEP Model
│   ├── 004_v1_airpods_pro_reference_1to1.stl     # 1:1 Apple AirPods Pro Reference STL Mesh
│   ├── 004_v1_airpods_pro_body.stl               # AirPods Pro Main Chassis Component STL
│   ├── 004_v1_airpods_pro_eartip.stl             # AirPods Pro Silicone Eartip Component STL
│   └── 004_v1_airpods_pro_in_ear.FCStd           # FreeCAD Project: 1:1 AirPods Pro Wearing Simulation
│
├── v2_SonyLinkBudsS/                               # Generation 2: Derived from Sony LinkBuds S (WF-LS900N) Prototype
│   ├── 004_v2_sleep_earphone_assembly.step        # Engineering STEP Solid CAD Model
│   ├── 004_v2_sleep_earphone_solid.stl           # 100% Watertight Solid Shell Mesh (2,191.8 mm³)
│   ├── 004_v2_sleep_earphone_hollow.stl          # Internal Micro-BA Driver Chamber Hollow Mesh
│   ├── 004_v2_sleep_earphone_silicone_sleeve.stl # 0.5mm Soft Protective Silicone Outer Sleeve
│   ├── 004_v2_sleep_earphone_colored.ply         # 4-Color Anatomically Segmented Inspection Mesh
│   ├── 004_v2_sleep_earphone_in_ear_simulation.FCStd # FreeCAD In-Ear Wearing & 2.5mm Pillow Clearance Simulation
│   ├── 004_v2_sleep_earphone_design_report.json  # Quantitative Dimensional & Verification Report
│   ├── 004_v2_sony_linkbuds_s_reference_1to1.step# 1:1 Sony LinkBuds S Reference STEP Model
│   ├── 004_v2_sony_linkbuds_s_reference_1to1.stl # 1:1 Sony LinkBuds S Reference STL Mesh
│   └── 004_v2_sony_linkbuds_s_in_ear.FCStd       # FreeCAD Project: 1:1 Sony LinkBuds S Wearing Simulation
│
├── v3_AnkerSleepA30/                              # 🌟 Generation 3: Derived from Anker Soundcore Sleep A30 Prototype
│   ├── 004_v3_sleep_earphone_assembly.step        # Engineering STEP Solid CAD Model
│   ├── 004_v3_sleep_earphone_solid.stl           # 100% Watertight Solid Shell Mesh (2,129.0 mm³)
│   ├── 004_v3_sleep_earphone_hollow.stl          # Internal Micro-BA Driver Chamber Hollow Mesh
│   ├── 004_v3_sleep_earphone_airwing_silicone_sleeve.stl # Patented Air-Wing Hollow Air-Cushion Sleeve (Shore A 30)
│   ├── 004_v3_sleep_earphone_colored.ply         # 4-Color Anatomically Segmented Inspection Mesh
│   ├── 004_v3_sleep_earphone_in_ear_simulation.FCStd # FreeCAD In-Ear Wearing & 3.0mm Pillow Clearance Simulation
│   ├── 004_v3_sleep_earphone_design_report.json  # 3-Generation Comparative Verification Report
│   ├── 004_v3_anker_sleep_a30_reference_1to1.step# 1:1 Anker Soundcore Sleep A30 Reference STEP Model
│   ├── 004_v3_anker_sleep_a30_reference_1to1.stl # 1:1 Anker Soundcore Sleep A30 Reference STL Mesh
│   ├── 004_v3_anker_sleep_a30_airwing.stl        # Anker A30 Air-Wing Hollow Cushion Component STL
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
2. **Object Visibility & Color Setup**:
   - Select `Human_Ear_004_Scan` in the left Model tree, press `Ctrl + D` and set **Transparency to 70%** (Light Gray) to inspect the internal in-ear fit.
   - Toggle visibility of `Sleep_Earphone_v3_AnkerAirWing_Solid` and `AirWing_Silicone_Cushion_Sleeve_ShoreA30` using the **Spacebar**.
   - Inspect `Simulated_Pillow_Plane_Clearance_3_0mm` (Plane at $X = -2.5\text{ mm}$) to verify the **3.0 mm non-contact safety clearance** between the pillow plane and the recessed faceplate ($X = +0.5\text{ mm}$).
