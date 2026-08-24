# ⚙️ Pillar 1: 5-Stage Learning Architecture & Creator Kit

**Pillar 1** is the curriculum and authoring layer of the Coding5s Framework.

It provides the spreadsheet-based **Creator Kit**, the curriculum-generation workflow, the five-stage learning architecture used to transform technical topics into structured practice sequences, and the automation infrastructure required to scale authoring operations globally.

The core lifecycle is:

```text
Practice
   ↓
Debug
   ↓
Complete
   ↓
Refactor
   ↓
Extend

```

The objective is not to make learning frictionless.

It is to apply **Controlled Cognitive Friction** so AI supports practice without replacing the reasoning, execution, debugging, and decisions the learner is expected to perform.

> **Low entry barrier does not mean low ceiling.**
> Creator Kits are designed to be usable through spreadsheets and prompts without requiring the educator to build or compile a software platform, while the resulting curricula can target skills from beginner fundamentals to advanced technical work.

For the operational workflow used to generate or adapt a curriculum, see `CURRICULUM_GENERATOR.md`.

---

## 🔬 The 5-Stage Learning Architecture

Each topic is transformed into five related forms of practice.

The exact prompt structure, mentor behavior, code shape, and difficulty may vary by language, library, domain, and learner level.

The stages define the **learning progression**, not one rigid exercise template.

### 🟥 Stage 1 — Practice

**Purpose:** Build initial familiarity with the syntax, tools, structures, or operational patterns of the topic.

Typical activities include:

* reading small reference examples,
* manually typing or reproducing them,
* executing them,
* observing results,
* making small changes,
* and connecting syntax with behavior.

AI may generate examples and explanations, but the learner should interact directly with the material instead of remaining a passive observer.

---

### 🟨 Stage 2 — Debug

**Purpose:** Develop corrective competence.

The learner receives intentionally broken, incomplete, misleading, or incorrect material related to what was practiced in Stage 1.

Possible failures include:

* syntax errors,
* logical mistakes,
* incorrect assumptions,
* configuration problems,
* malformed data,
* or domain-specific faults.

AI guidance should preserve the learner's diagnostic work. It may ask questions, interpret errors, provide hints, or explain relevant concepts without simply performing the entire correction when the exercise requires the learner to find it.

---

### 🟩 Stage 3 — Complete

**Purpose:** Move from recognition toward independent construction.

Part of a working artifact is intentionally missing.

Depending on the domain, the learner may need to complete:

* functions,
* transformations,
* configurations,
* queries,
* conditions,
* data structures,
* workflow steps,
* or another meaningful component.

The learner receives enough surrounding context to reason about what is missing and implement it.

---

### 🟦 Stage 4 — Refactor

**Purpose:** Improve something that already works.

The learner evaluates the Stage 3 result against constraints relevant to the technology or domain.

Possible improvements include:

* readability,
* maintainability,
* idiomatic design,
* performance,
* robustness,
* error handling,
* architecture,
* security,
* or simplification.

Refactoring rules must remain **ecosystem-specific**. A Python OOP lesson, an Elixir functional workflow, a SQL query, and a networking lab should not be forced through the same design principles.

---

### 🟪 Stage 5 — Extend

**Purpose:** Transfer existing understanding into a new requirement.

The learner expands the artifact by introducing an additional capability, constraint, scenario, integration, or architectural requirement.

Examples may include:

* supporting additional inputs,
* adding concurrency,
* extending a data model,
* introducing another service,
* adapting the solution to a new constraint,
* or scaling the original idea into a larger exercise.

The important transition is:

```text
Understand Existing Work
        ↓
Modify It Under New Requirements
        ↓
Explain / Defend the Decisions

```

Stage 5 tests whether the learner can move beyond reproducing the original lesson.

---

## 🧠 Controlled Cognitive Friction

Coding5s does **not** prohibit AI-generated code.

Instead, Pillar 1 controls **when and how AI assistance enters the learning task**.

Depending on the stage, AI may provide:

```text
reference examples
broken code
partial implementations
scaffolding
error explanations
diagnostic questions
analogies
review feedback
new requirements

```

The boundary is simpler:

> **AI can support the work, but it should not silently replace the cognitive task the learner is supposed to practice.**

This principle allows Coding5s to use modern generative AI extensively without turning the learning process into unrestricted answer generation.

---

## 🛠️ The Creator Kit Workspace (`coding5s_creator_kits/`)

The **Creator Kit** is the spreadsheet-based authoring environment used to construct Coding5s curricula.

It combines:

* curriculum topics,
* stage-specific prompt components,
* learner-level variables,
* ecosystem rules,
* output-language controls,
* reusable formulas,
* and optional contextual resources

into structured prompts that can be used with capable LLMs.

### ⚙️ Creator Kit Automation Infrastructure

To scale authoring operations and eliminate manual friction, the `coding5s_creator_kits/` subdirectory includes a dedicated automation suite powered by Python and background Windows COM Automation (`win32com`):

1. **Formula Auto-Injector (`copy_paster_Prompt_Formulas_for_CK.py`):** Extracts complex prompt-generation formulas from the modular generation sheets (`FGen_S1` through `FGen_S5`) and batch-injects them directly into the master `PromptGenerator` sheet across all stage ranges up to row 200. Features an 8,100-character safety guard to prevent Excel formula overflow.
2. **Creator Kit Updater (`creator_kit_updater.py`):** Performs mass batch updates across all Creator Kits in the directory tree by reading a central data source (`creator_kit_Base_File_for_CKs.xlsx`) and propagating rule changes without disrupting formatting or conditional styles.
3. **Sync Student Kit Generator (`student_kit_creator.py`):** Scans the directory recursively, opens each Creator Kit in background memory (`DispatchEx`), simulates target language localization (e.g., Spanish, English, German) in cell `B6`, recalculates prompts, extracts static values, and compiles clean, protected distribution files (`Student Kits`) using a global visual template (`Student Kit Template.xlsx`) while leaving master Creator Kits 100% untouched.

Each tool includes 1-click execution batch scripts (`.bat`) and comprehensive documentation guides inside its folder.

---

## 📦 Reference Creator Kits

This repository includes Creator Kits configured for several languages and technical ecosystems.

### Dart

* `Coding5s Dart Fundamentals Creator Kit v0.2.xlsx`

### Elixir

* `Coding5s Elixir Fundamentals Creator Kit v0.2.xlsx`
* `Coding5s Elixir OTP Creator Kit v0.2.xlsx`

### Python

* `Coding5s Python Core And Scripting Creator Kit v0.1.xlsx`
* `Coding5s Python HTTPX Creator Kit v0.1.xlsx`
* `Coding5s Python Numpy Creator Kit v0.1.xlsx`
* `Coding5s Python Pandas Creator Kit v0.1.xlsx`
* `Coding5s Python Requests Creator Kit v0.1.xlsx`

These are **reference implementations**, not the boundary of Pillar 1.

The same architecture can be adapted to additional programming languages, libraries, technical stacks, and other domains where the five-stage progression remains meaningful.

---

## 🧪 Supporting Practice Tools

Pillar 1 can also use complementary generators when a lesson requires realistic external artifacts.

One example is the **Synthetic Practice Dataset Generator**, which creates small reproducible CSV, JSON, XLSX, log, NumPy, or similar practice files engineered around the lesson topic.

This allows file-based exercises to use actual artifacts instead of requiring the learner to imagine the data being manipulated.

Supporting tools extend the practice environment; they do not replace the five-stage architecture.

---

## 📊 Cross-Model Reference Executions

The links below preserve examples of the same stage instructions executed across different LLMs.

They should be treated as **reference execution samples**, not formal benchmarks or proof of model-independent behavior.

### 💧 Elixir Fundamentals

* **Stage 1:** [suspicious link removed] | [Gemini](https://share.gemini.google/eznT27nS6B9v)
* **Stage 2:** [suspicious link removed] | [Gemini](https://share.gemini.google/tFvcGx1lLind)
* **Stage 3:** [suspicious link removed] | [Gemini](https://share.gemini.google/HkkaBKsKCxHh)
* **Stage 4:** [suspicious link removed] | [Grok](https://grok.com/share/c2hhcmQtMg_27517b30-0c23-44c4-b072-5c4b80b87b12)
* **Stage 5:** [suspicious link removed] | [Grok](https://grok.com/share/c2hhcmQtMg_dc7343bd-9559-4ece-8fa5-bf0f7649b942)

### 🐍 Python Core & Scripting

* **Stage 1:** [suspicious link removed] | [Grok](https://grok.com/share/c2hhcmQtMg_2397f881-723b-44b5-8803-c7d10a86494a) | [ChatGPT](https://chatgpt.com/share/6a5d4652-f8a4-83e8-9740-9607b5e948be)
* **Stage 2:** [suspicious link removed] | [Grok](https://grok.com/share/c2hhcmQtMg_96e5969c-7906-486f-873b-66b6458e2e83) | [ChatGPT](https://chatgpt.com/share/6a5d4a31-6564-83e8-9fe3-5dc236e8ff53)
* **Stage 3:** [suspicious link removed] | [Grok](https://grok.com/share/c2hhcmQtMg_9761e0fd-e5dc-4450-bf0f-905929a3ed02) | [ChatGPT](https://chatgpt.com/share/6a5d4cc2-c524-83e8-878f-c1cb36188bf1)
* **Stage 4:** [suspicious link removed] | [Grok](https://grok.com/share/c2hhcmQtMg_d79fd554-9c13-4c19-a866-d0834c18a122) | [ChatGPT](https://chatgpt.com/share/6a5d4ecb-b350-83e8-93c8-cd9cc10704cc)
* **Stage 5:** [suspicious link removed] | [Grok](https://grok.com/share/c2hhcmQtMg_003f4dd0-79d7-45f2-97da-cb1e5749fd50) | [ChatGPT](https://chatgpt.com/share/6a5d53dd-3370-83e8-a5f8-07f66f90582b)

Model behavior can change over time, and shared execution links may eventually become unavailable. These examples document historical behavior observed during framework development.

---

## 🚀 Getting Started

To create or adapt a Coding5s course:

1. Select an existing Creator Kit as a reference or start from the appropriate master template.
2. Define the target curriculum, technology, learner level, and output language.
3. Configure the technical and stage-specific rules.
4. Generate and inspect the resulting prompts.
5. Test representative topics before producing the complete Student Kit.
6. Iterate when model behavior exposes ambiguity, excessive assistance, or insufficient guidance.

See `CURRICULUM_GENERATOR.md` for the complete generation workflow.

---

## 🔗 Relationship to the Other Pillars

```text
PILLAR 1
What does the learner practice?
How is the curriculum structured?

        ↓

PILLAR 2
How should the AI mentor behave
during that practice?

        ↓

PILLAR 3
What useful context should persist
as the learner progresses?

```

The three pillars can work together, but Pillar 1 remains independently useful as the curriculum and practice architecture of Coding5s.

```

```