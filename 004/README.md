# 004 右耳專屬客製化睡眠耳機 3D 模型庫 (Sleep Earphones v1, v2, v3)

本目錄包含針對 **004 受試者右耳 3D 掃描解剖結構** 進行客製化人因工程設計的三代睡眠耳機（Sleep Earbuds）完整 3D 模型（包含 STEP CAD 實體、高精 STL 網格、抽殼腔體、矽膠外套、FreeCAD 佩戴模擬專案與尺寸量測報告）。

---

## 📊 三代睡眠耳機演進全方位對比 (v1 vs v2 vs v3)

| 比較項目 | 🎧 v1 版（Apple AirPods Pro 原型） | 🎧 v2 版（Sony LinkBuds S 原型） | 🌟 **v3 版（Anker Soundcore Sleep A30 原型）** |
| :--- | :--- | :--- | :--- |
| **設計原型** | Apple AirPods Pro (1st/2nd Gen) | Sony LinkBuds S (WF-LS900N, 4.8g) | **Anker Soundcore Sleep A30 (3.1g)** |
| **全機實體體積** | 2,255.6 mm³ | 2,191.8 mm³ | **2,129.0 mm³（三代最緊湊）** |
| **外背蓋沉降深度** | $X = -0.5\text{ mm}$（深進 1.0mm） | $X = 0.0\text{ mm}$（深進 1.5mm） | **$X = +0.5\text{ mm}$（深進 2.0mm，極致深嵌）** |
| **側睡枕頭安全間隙** | 2.0 mm | 2.5 mm | **3.0 mm（三代最大安全間隙，枕頭完全不碰耳機）** |
| **防掉耳翼技術** | 一體化硬質倒圓角 Cymba 耳翼 | 鵝卵石低凸流線耳翼 | 🌟 **Air-Wing 專利中空柔性緩衝氣囊耳翼** |
| **側睡防壓痛機制** | 幾何邊界倒圓角避讓 | 鵝卵石有機平滑過渡 | 🌟 **中空氣囊被動受壓形變緩衝（徹底消除軟骨壓痛）** |
| **耳塞套結構** | 單層短軸橢圓矽膠套 | 複合圓形矽膠套 | **Twin-Seal 雙層傘狀柔性隔音套** |
| **周邊退讓公差** | 0.35 mm | 0.40 mm | **0.45 mm（最高彈性形變容許度）** |
| **內部單體規格** | 5.0 × 3.0 × 2.2 mm 微型動鐵 | 5.0 × 3.0 × 2.2 mm 微型動鐵 | 5.0 × 3.0 × 2.2 mm 微型動鐵 |
| **聲學導管與洩壓** | $\phi 2.2\text{ mm}$ 導音管 + $\phi 0.8\text{ mm}$ 洩壓孔 | $\phi 2.2\text{ mm}$ 導音管 + $\phi 0.8\text{ mm}$ 洩壓孔 | $\phi 2.2\text{ mm}$ 導音管 + $\phi 0.8\text{ mm}$ 洩壓孔 |

---

## 📁 目錄結構與檔案清單

```text
004/
├── v1_AirPodsPro/                                  # v1 版：基於 Apple AirPods Pro 原型
│   ├── 004_v1_sleep_earphone_assembly.step        # 工程級 STEP CAD 實體
│   ├── 004_v1_sleep_earphone_solid.stl           # 100% Watertight 實體模型
│   ├── 004_v1_sleep_earphone_hollow.stl          # 內部微型單體抽殼安裝腔體
│   ├── 004_v1_sleep_earphone_silicone_sleeve.stl # 0.6mm 超軟矽膠外套
│   ├── 004_v1_sleep_earphone_colored.ply         # 4 色解剖分區網格
│   ├── 004_v1_sleep_earphone_in_ear_simulation.FCStd # FreeCAD 佩戴與枕頭切面模擬
│   ├── 004_v1_sleep_earphone_design_report.json  # v1 尺寸度量報告
│   ├── 004_v1_airpods_pro_reference_1to1.step    # AirPods Pro 1:1 STEP 參考模型
│   ├── 004_v1_airpods_pro_reference_1to1.stl     # AirPods Pro 1:1 STL 參考模型
│   └── 004_v1_airpods_pro_in_ear.FCStd           # AirPods Pro 佩戴模擬
│
├── v2_SonyLinkBudsS/                               # v2 版：基於 Sony LinkBuds S 原型
│   ├── 004_v2_sleep_earphone_assembly.step        # 工程級 STEP CAD 實體
│   ├── 004_v2_sleep_earphone_solid.stl           # 100% Watertight 實體模型
│   ├── 004_v2_sleep_earphone_hollow.stl          # 內部微型單體抽殼安裝腔體
│   ├── 004_v2_sleep_earphone_silicone_sleeve.stl # 0.5mm 超軟矽膠外套
│   ├── 004_v2_sleep_earphone_colored.ply         # 4 色解剖分區網格
│   ├── 004_v2_sleep_earphone_in_ear_simulation.FCStd # FreeCAD 佩戴與枕頭切面模擬
│   ├── 004_v2_sleep_earphone_design_report.json  # v2 尺寸度量報告
│   ├── 004_v2_sony_linkbuds_s_reference_1to1.step# Sony LinkBuds S 1:1 STEP 模型
│   ├── 004_v2_sony_linkbuds_s_reference_1to1.stl # Sony LinkBuds S 1:1 STL 模型
│   └── 004_v2_sony_linkbuds_s_in_ear.FCStd       # Sony LinkBuds S 佩戴模擬
│
├── v3_AnkerSleepA30/                              # 🌟 v3 版：基於 Anker Soundcore Sleep A30 氣囊原型
│   ├── 004_v3_sleep_earphone_assembly.step        # 工程級 STEP CAD 實體
│   ├── 004_v3_sleep_earphone_solid.stl           # 100% Watertight 實體模型
│   ├── 004_v3_sleep_earphone_hollow.stl          # 內部微型單體抽殼安裝腔體
│   ├── 004_v3_sleep_earphone_airwing_silicone_sleeve.stl # Air-Wing 專利氣囊矽膠外套
│   ├── 004_v3_sleep_earphone_colored.ply         # 4 色解剖分區網格
│   ├── 004_v3_sleep_earphone_in_ear_simulation.FCStd # FreeCAD 佩戴與 3.0mm 枕頭間隙模擬
│   ├── 004_v3_sleep_earphone_design_report.json  # 三代演進完整度量報告
│   ├── 004_v3_anker_sleep_a30_reference_1to1.step# Anker Sleep A30 1:1 STEP 模型
│   ├── 004_v3_anker_sleep_a30_reference_1to1.stl # Anker Sleep A30 1:1 STL 模型
│   └── 004_v3_anker_sleep_a30_in_ear.FCStd       # Anker Sleep A30 佩戴模擬
│
└── reference_ear/                                  # 004 右耳原始解剖基準模型
    ├── 004_human_ear_right_solid.stl              # 100% Watertight 人耳封閉實體
    ├── 004_concha_basin.stl                       # 耳甲腔盆地（Cavum + Cymba + Meatus）
    └── 004_canal_entrance.stl                     # 耳道口漏斗幾何
```
