# 🤝 Contributing to Coding5s

Thank you for your interest in contributing to **Coding5s**.

Coding5s is an open-source framework for structured technical learning in the AI era. Contributions can range from documentation fixes and testing to Creator Kits, mentor behaviors, Stateful5s implementations, Seed Contexts, visual assets, research experiments, and entirely new methodology variants.

You do not need to be a senior software engineer to contribute.

By contributing to this project, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md) and the repository's [MIT License](LICENSE).

---

## 🧭 Ways to Contribute

Useful contributions may include:

- **Pillar 1** — Creator Kits, curricula, technical rules, learning-stage improvements
- **Pillar 2** — Mentor prompts, behavioral specifications, testing, and new mentor archetypes
- **Pillar 3** — Stateful5s ledgers, state models, persistence experiments, and automation
- **Seed Contexts** — Language Seed Contexts and General Seed Context experiments
- **Synthetic Practice Data** — dataset generators and realistic practice artifacts
- **Documentation** — READMEs, guides, examples, diagrams, and corrections
- **Visual Assets** — branding, diagrams, screenshots, and mascot-related work
- **Methodology Variants** — alternative or specialized Coding5s learning workflows
- **Research Lab** — experiments based on clearly identified research concepts
- **Testing & Bug Reports** — prompt failures, formula problems, inconsistent behavior, and usability issues

For larger community implementations, also review [`/contributions`](contributions/).

---

## 🧪 Core-Compatible vs. Experimental Work

Before contributing, identify what type of change you are making.

### Core-Compatible

A contribution that extends Coding5s while preserving the architecture or behavior it claims to implement.

Examples:

```text
New Creator Kit
New Language Seed Context
New Mentor
Stateful5s Domain Adaptation
Documentation Improvement
````

### Experimental

A contribution that intentionally changes, challenges, or tests part of the framework.

Examples:

```text
Alternative Stage Architecture
New Persistence Strategy
Research Lab Prototype
Methodology Variant
Experimental Prompt System
```

Experimental work is welcome.

It should simply be labeled clearly so users do not confuse an early experiment with established framework behavior.

---

## 🚀 Contribution Workflow

### 1. Fork the Repository

Create a personal fork of Coding5s.

### 2. Create a Branch

Use a descriptive branch name.

Examples:

```text
feature/python-oop-creator-kit
fix/stage-3-prompt-rule
docs/stateful5s-readme
experiment/context-ledger
```

Useful prefixes include:

```text
feature/
fix/
docs/
experiment/
```

### 3. Make and Test Your Changes

Perform testing appropriate to the contribution.

A documentation correction may require only careful review.

A Creator Kit, mentor, prompt engine, dataset generator, or Stateful5s implementation should be executed through at least one realistic workflow.

### 4. Commit and Push

Example:

```bash
git add .
git commit -m 'Add Python OOP Creator Kit'
git push origin feature/python-oop-creator-kit
```

### 5. Open a Pull Request

Clearly explain:

* what problem the contribution addresses,
* what was changed,
* which part of Coding5s it affects,
* how it was tested,
* known limitations,
* and whether it is core-compatible or experimental.

Link related Issues, Discussions, Research Lab documents, or Ideas to Innovate entries when relevant.

---

## ✅ Quality Expectations

### Documentation

Use Markdown for repository documentation whenever practical.

Keep documentation:

* clear,
* concise,
* technically specific,
* consistent with the surrounding architecture,
* and honest about limitations.

Use code blocks for prompts, formulas, schemas, commands, and technical examples when they improve readability.

---

### Testing Proportional to Claims

Do not make testing requirements larger than the contribution requires.

At minimum, test the behavior you are changing.

Cross-model testing is encouraged for AI-dependent components.

If a contribution claims to be **model-agnostic**, that claim should be supported by testing across multiple model families.

Document important failures such as:

* instruction loss,
* excessive assistance,
* insufficient guidance,
* formatting instability,
* model-specific behavior,
* or inconsistent outputs.

---

### Preserve Architecture When Claiming Compatibility

If a contribution is described as a standard Coding5s implementation, it should preserve the relevant principles of the framework.

For example:

* Pillar 1 should preserve meaningful learner participation and Controlled Cognitive Friction.
* Pillar 2 should define clear behavioral boundaries for AI assistance.
* Pillar 3 should clearly document what cumulative state is preserved and how later work receives it.

Experimental variants may intentionally change these behaviors if the deviation is documented.

---

## ⚙️ Creator Kit Contributions

When modifying or creating Creator Kits:

* verify spreadsheet formulas and references,
* preserve expected row and column alignment,
* avoid unnecessary formula complexity,
* test generated prompts,
* document important configuration variables,
* and inspect representative outputs before submitting.

Student-facing artifacts should avoid exposing Creator Kit generation machinery unless that machinery is intentionally part of the learning experience.

---

## 🐝 Mentor Contributions

A mentor should clearly define:

```text
Target Task
Expected Input
Behavioral Rules
Assistance Boundary
Adaptation Rules
Known Limitations
Example Interaction
```

Coding5s does **not** impose a universal rule that AI must never generate code.

A mentor fails when it violates the assistance boundary of the learning task—not simply because code appears in its response.

---

## 🌐 Stateful5s Contributions

Stateful5s implementations should document:

```text
What state is preserved?
Where is it stored?
How is it updated?
How is it validated?
How does later work consume it?
What happens when the state is incomplete or incorrect?
```

No specific persistence technology is required.

Spreadsheet ledgers, structured files, databases, application state, or experimental persistence strategies may all be explored.

---

## 🌍 Language Seed Context Contributions

Language Seed Contexts should aim to provide stronger linguistic grounding for the target language.

When contributing one:

* preserve technical meaning,
* avoid blindly translating from a dominant language,
* use authoritative linguistic resources where possible,
* document the sources used,
* distinguish established linguistic information from experimental prompt behavior,
* and seek review from fluent or native speakers when practical.

For low-resource or indigenous languages, expert or community review is especially valuable.

---

## 🔬 Research Lab Contributions

Research Lab concepts may be speculative.

Contributors are welcome to:

* test them,
* challenge them,
* implement prototypes,
* measure failures,
* compare alternatives,
* or show that an idea does not work.

Do not present an experimental hypothesis as a validated framework capability.

A negative result can still be a useful contribution.

---

## 🎨 Visual Contributions

Before submitting screenshots, diagrams, branding, or other visual assets:

* verify that you have the rights to contribute them,
* remove private or confidential information,
* avoid exposing API keys or credentials,
* optimize unnecessarily large images,
* and clearly distinguish official, reference, experimental, and community assets.

See [`/assets`](assets/) for visual asset guidance.

---

## 🐛 Reporting Bugs & Prompt Failures

If you discover a framework, formula, prompt, or mentor failure, include enough information to reproduce it.

Useful details include:

1. Target technology or domain
2. Relevant Coding5s stage or component
3. AI model and provider, when applicable
4. Exact prompt or configuration that triggered the problem
5. Actual behavior
6. Expected behavior
7. Relevant screenshots, logs, or generated output

For AI-related failures, remember that behavior can vary across models and can change over time.

---

## ⚖️ Licensing & Content Rights

Contributions must be compatible with the repository license.

Do not submit:

* confidential information,
* proprietary datasets without permission,
* copyrighted material you cannot redistribute,
* credentials or private customer data,
* or third-party assets with incompatible licensing.

Contributors retain authorship of their original work while granting the rights required by the repository's MIT License.

---

## 💬 Discussions Before Large Contributions

For substantial changes, opening a GitHub Discussion or Issue before investing heavily in implementation is encouraged.

This is especially useful for:

* new methodology variants,
* major Creator Kit architectures,
* new research directions,
* changes affecting multiple pillars,
* or proposals that alter core framework behavior.

Small fixes do not need unnecessary process.

---

## 🔗 Related Areas

```text
/contributions
Community implementations and extensions

/ideas_to_innovate
Open implementation and experimentation ideas

/research_lab
Experimental research concepts

/assets
Visual identity and asset guidelines

/pillar_1
5-Stage Learning Architecture & Creator Kit

/pillar_2
AI Mentor Swarm & Behavioral Layer

/pillar_3
Stateful5s & Persistent Cumulative Context
```

---

## 🌱 Contribution Principle

A contribution does not need to be large to be valuable.

Fix a confusing sentence. Test a prompt. Improve a formula. Build a new Creator Kit. Challenge an experimental idea. Document a failure.

What matters is that the contribution solves or exposes a clear problem, makes its behavior inspectable, and distinguishes what has been tested from what is still being explored.
