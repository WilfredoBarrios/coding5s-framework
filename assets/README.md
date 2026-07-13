# 🎨 Coding5s Visual Assets & Branding Hub

This directory hosts the official visual assets, interface screenshots, illustrations, and branding elements for the Coding5s ecosystem. 

For the history, emotional origin, and active community design challenge for our official mascot, please read **[CODI.md](CODI.md)**.

---

## 📂 Asset Inventory & Specifications

To maintain a cohesive presentation across our main repository and any community forks, please adhere to the following directory layout:

```text
assets/
├── README.md                 # This file
├── CODI.md                   # Codi's story and community design challenge
├── logo.png                  # Official Coding5s logo banner
├── codi-base-photo.jpg       # The original photo of David's stuffed bear
├── codi-mascot.png           # [WIP] The official digital mascot design (Pending community merge)
├── diagram.png               # High-fidelity 5-Stage Lifecycle infographic (SDLC)
└── screenshots/              # Real-world interface captures
    ├── creator-kit-excel.png # Master Authoring Environment preview
    ├── student-kit-grid.png  # Self-assessment matrix tracking (1, 0, -1)
    └── mentor-socratic-chat.png # AI Mentors executing the "No Keyboard" rule
```

🛠️ Contribution & Optimization Gate

If you are uploading new screenshots for your custom technology stack or localized language variants inside contributions/:

    Dark Mode Compliance: Ensure background templates, charts, and diagrams use clean transparency masks so they render flawlessly across both GitHub Light and Dark modes.

    Compression Guardrail: All binary images must be processed through compression tools (e.g., TinyPNG, OptiPNG) before a Pull Request is submitted. Keep file sizes under 500 KB to guarantee fast repository cloning in low-resource environments.

    Anonymization: Please blur or omit any private API keys, local paths, or personal grading details inside your screenshots/ submissions.