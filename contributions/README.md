# 🤝 Coding5s Contributions Hub

Welcome to the Coding5s Contributions Hub. This directory is being built as a collaborative space for community-contributed educational assets, custom technology stacks, and framework expansions.

If you have built a **Creator Kit** and a specialized **Student Kit**, adapted the methodology to a new domain, or created new Seed Contexts, this is where it will live.

**Note:** Coding5s is in its early stages and we are actively looking for the first contributors to help shape this ecosystem. Your contribution will be foundational.

---

## 📂 Directory Structure

All contributions must follow this specific hierarchy inside the `/contributions` folder to maintain parity with the core ecosystem:

### For Pillar 1 Coding5s Contributions (5-Stage Methodology)

```text
contributions/
├── coding5s-[technology]/           # e.g., coding5s-react-js, coding5s-docker-fundamentals
│   ├── README.md                    # Overview, target audience, and setup instructions
│   ├── creator_kit/                 # The authoring files (Excel templates, source data)
│   │   └── [Tech]_Creator_Kit.xlsx
│   └── student_kit/                 # The runtime files (Clean prompts, student grids)
│       ├── [Tech]_Student_Kit.xlsx
│       └── localized/               # Optional: Regional or low-resource language variants
```

### For Pillar 2 Mentor Contributions (AI Swarm Mentors)

```text
contributions/
├── mentors/
│   ├── [mentor-archetype]/          # e.g., security-auditor, performance-optimizer, ux-specialist
│   │   ├── README.md                # Mentor profile, use cases, and activation scenarios
│   │   ├── mentor_prompt.md         # The Level 1 Meta-Prompt that generates this mentor's Seed
│   │   ├── examples/                # Sample interactions and prompt outputs
│   │   │   ├── stage_1_example.md
│   │   │   ├── stage_3_example.md
│   │   └── test_results.md          # Validation across different LLMs
│   └── README.md                    # How to create and test new mentor archetypes
```

### For Pillar 3 Stateful5s Contributions (Cumulative State Methodology)

```text
contributions/
├── stateful5s-[technology]/         # e.g., stateful5s-django, stateful5s-aws-arch
│   ├── README.md                    # Overview, state architecture, and prerequisites
│   ├── creator_kit/                 # The authoring files with state management
│   │   └── [Domain]_Stateful5s_Creator_Kit.xlsx
│   ├── student_kit/                 # The runtime files with cumulative prompts
│   │   └── [Domain]_Stateful5s_Student_Kit.xlsx
│   └── topology/                    # Optional: State diagrams, architecture maps
│       └── state_diagram.md
```

### For Seed Context Contributions

```text
contributions/
├── seed-contexts/
│   ├── language/                    # New language Seed Contexts
│   │   └── [language-name].md
│   ├── pedagogy/                    # New pedagogical approaches
│   │   └── [approach-name].md
│   ├── role/                        # New mentor archetypes
│   │   └── [archetype-name].md
│   └── README.md                    # How to create and test Seed Contexts
```

---

## 🛠️ Contribution Guidelines

To ensure that community kits maintain the same pedagogical rigor as the core repository, all pull requests (PRs) must meet the following Quality Gates:

### 1. The Pedagogy Checklist

- **The 5-Stage Alignment**: Your curriculum must strictly adhere to the 5 stages (Practice, Debug, Complete, Refactor, Extend). Skipping stages breaks the learning continuity.
- **The "No Keyboard" Rule**: The generated prompts for your AI Mentors must explicitly forbid the LLM from writing direct code for the student.
- **Controlled Friction**: The Socratic prompts must be validated to ensure they provide guidance through analogies and diagnostic questions, not shortcut solutions.
- **Stage 1 Priority**: The Practice stage must emphasize manual copying of code to build muscle memory before any AI interaction.

### 2. Technical Requirements

- **Formula-Free Student Kits**: The files inside the `student_kit/` folder must be completely stripped of the original Excel generation formulas. They should only contain the clean, final prompt text payloads ready for copy-pasting.
- **Model Agnosticism**: Your prompts must be tested across at least two different LLM families (e.g., GPT-4o and Claude 3.5 Sonnet) to ensure they do not suffer from severe Latent Drift.
- **Data Validation**: Ensure all strings inside your Creator Kit sheets are sanitized and do not contain unescaped characters that could break string interpolation when loaded into an LLM payload.
- **Stateful5s Specific**: If contributing to Stateful5s, ensure your state management logic is clearly documented and that each lesson builds on the previous state.

### 3. Licensing

- All contributions must be released under the **MIT License**, consistent with the main repository.
- You retain copyright of your original work, but grant the community the right to use, modify, and distribute it.

---

## 🚀 How to Submit Your Kit

1. **Fork the Repository**: Create a personal fork of the `coding5s-framework` repository.
2. **Create your Branch**: Use a descriptive naming convention: `feature/contrib-[tech-name]`.
3. **Build and Test**: Place your files in the structured folder layout. Run a "Dry Run" test interaction with an AI to confirm the constraints hold under pressure.
4. **Document**: Include a comprehensive `README.md` explaining:
   - Target technology and student profile
   - Prerequisites (if any)
   - How to use the Creator Kit and Student Kit
   - Any linguistic localizations included
   - Testing results across different LLMs
5. **Submit a PR**: Open a Pull Request against our main branch. Be prepared to iterate based on feedback.

---

## 💡 Ideas to Innovate (Open Challenges)

Looking to contribute but don't know where to start? Here are priority areas where the framework needs expansion:

### Technology Stacks
- **Frontend Frameworks**: React, Vue, Svelte, Angular
- **Cloud & DevOps**: Docker, Kubernetes, AWS/GCP/Azure Architectures
- **Data Science & ML**: Pandas, Scikit-Learn, PyTorch foundations
- **Advanced Systems**: Rust (memory management), Go (concurrency patterns), Elixir (distributed systems)
- **Mobile Development**: React Native, Flutter, Swift/Kotlin

### Non-Programming Domains
- **Medical Triage**: Diagnostic protocols, patient care workflows
- **Aviation Procedures**: ICAO standards, emergency protocols (see HRPML demo)
- **Legal Analysis**: Case research, contract drafting, precedent integration
- **Corporate Networking**: Beyond CCNA (enterprise architectures, security)

### Seed Contexts
- **New Languages**: French, German, Mandarin, Arabic, Portuguese (and more indigenous languages)
- **New Pedagogies**: Problem-Based Learning, Flipped Classroom adaptations
- **New Mentor Archetypes**: Security Auditor, Performance Optimizer, UX Specialist
- **Domain-Specific Contexts**: Fintech, Healthcare, Gaming, Education

### Framework Extensions
- **ECP Optimizations**: Improvements to the Ephemeral Context Protocol
- **Context Composition**: New ways to combine multiple Seed Contexts
- **Tool Integrations**: VS Code extensions, Jupyter notebooks, IDE plugins
- **Assessment Tools**: Automated evaluation systems for Explanation Gates

---

## 🚫 What NOT to Contribute

To maintain quality and focus, please do **not** submit:

- ❌ Kits that skip any of the 5 stages
- ❌ Prompts that allow the AI to write complete code for the student
- ❌ Untested prompts that haven't been validated across multiple LLMs
- ❌ Student Kits that still contain Excel formulas
- ❌ Content that violates the Code of Conduct or promotes harmful practices
- ❌ Duplicate contributions (check existing PRs first)

---

## 🏆 Recognition

We believe in recognizing our contributors. When your contribution is merged:

- Your name and GitHub profile will be listed in the contribution's `README.md`
- Significant contributions may be featured in announcements and documentation
- You retain full copyright of your original work under the MIT License

---

## 💬 Questions?

If you have questions about contributing, want to discuss an idea before building it, or need help with the process:

1. **Open a Discussion**: Use GitHub Discussions to ask questions and get feedback from the community
2. **Check Existing Issues**: Someone might already be working on something similar
3. **Contact the Creator**: For specific questions about the methodology or architecture, reach out directly

We are building this together, and every contribution—no matter how small—helps shape the future of technical education in the Post-AI era.

Thank you for being part of the foundational team! 🚀
