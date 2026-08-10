# 📘 METHODOLOGY.md: Coding5s Framework Architecture

Coding5s is an open-source technical-learning framework designed for an environment where generative AI can explain, generate, debug, and modify technical work on demand.

Its central design principle is:

> **Learn With AI. Don’t Outsource Your Thinking.**

The framework is organized around three complementary pillars:

```text
Pillar 1
5-Stage Learning Architecture
        ↓
Pillar 2
AI Mentor Behavioral Layer
        ↓
Pillar 3
Persistent Cumulative Context
````

Each pillar addresses a different part of the learning problem.

---

## 1. Core Principle: Controlled Cognitive Friction

AI can reduce the effort required to obtain a technically correct answer.

That can be useful, but during learning the effort being removed may sometimes be the exact reasoning, diagnosis, retrieval, construction, or decision-making that the learner needs to practice.

Coding5s uses **Controlled Cognitive Friction** to manage that boundary.

The objective is not to make learning unnecessarily difficult.

It is to introduce enough purposeful difficulty that the learner remains an active participant while still benefiting from AI assistance.

Conceptually:

```text
Too Little Friction
→ AI performs the learning task

Useful Friction
→ AI supports the learner performing the task

Too Much Friction
→ difficulty stops being educational
```

Coding5s attempts to operate in the middle.

A related design goal is **Epistemic Retention**: helping the learner retain enough understanding to inspect, explain, repair, modify, and extend technical work rather than only obtaining successful outputs.

---

## 2. Pillar 1: 5-Stage Learning Architecture

Pillar 1 defines **what the learner practices and how that practice progresses**.

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

### Practice

Build initial familiarity through direct interaction with small, understandable examples or technical artifacts.

### Debug

Diagnose and correct intentionally flawed or problematic work.

### Complete

Reconstruct a meaningful missing component from the surrounding context and requirements.

### Refactor

Improve something that already works according to criteria appropriate to the target technology or domain.

### Extend

Adapt existing work to a new requirement, capability, constraint, or environment.

The five stages are not intended as a literal copy of the Software Development Lifecycle.

They represent a **learning progression from initial interaction toward increasingly independent modification and transfer**.

Pillar 1 is implemented primarily through the spreadsheet-based **Creator Kit**, which combines curriculum information, technical rules, stage rules, configuration variables, and prompt components.

---

## 3. Pillar 2: AI Mentor Swarm & Behavioral Layer

Pillar 2 defines **how AI should behave while supporting the learner**.

General-purpose AI assistants may provide complete answers even when doing so removes the cognitive work an exercise was designed to develop.

Coding5s Mentors introduce task-specific behavioral boundaries.

Depending on the activity, a mentor may:

* request the learner's reasoning,
* provide progressive hints,
* ask diagnostic questions,
* critique an attempted solution,
* explain relevant concepts,
* challenge assumptions,
* provide examples or scaffolding,
* or require the learner to defend a technical decision.

Coding5s does **not** impose a universal rule that AI may never generate code.

The relevant boundary is:

> **Do not perform the cognitive task that the learner is currently expected to practice.**

The term **Mentor Swarm** refers primarily to a collection of specialized mentor behaviors.

Multiple agents do not need to operate simultaneously for Pillar 2 to be useful.

Future implementations may orchestrate several mentors together.

---

## 4. Pillar 3: Stateful5s

Pillar 3 addresses **what useful context should survive as the learner progresses**.

Some technical learning environments are cumulative.

A decision made in an early lesson may still matter many lessons later.

Stateful5s therefore separates:

```text
Conversation History
=
Everything that was said

Persistent State
=
What future work still depends on
```

The relevant state is preserved outside the LLM and supplied again when later work requires it.

This selected persistent information is called **Accumulated Context**.

A networking implementation might preserve:

```text
Topology
Device Roles
Interfaces
VLANs
IP Addressing
Routing
Security Decisions
Current Constraints
```

A programming project might preserve an entirely different state.

The current reference implementation uses a spreadsheet **Architectural Ledger**, but Stateful5s does not require:

* spreadsheets,
* a Finite State Machine,
* a database,
* RAG,
* ECP,
* or any specific persistence technology.

The architectural principle is simply:

> **Persist what future work depends on.**

---

## 5. How the Three Pillars Work Together

The pillars answer three different questions:

```text
PILLAR 1
What should the learner do?

        ↓

PILLAR 2
How should the AI help?

        ↓

PILLAR 3
What must remain known later?
```

For example:

```text
Curriculum Topic
      ↓
5-Stage Practice Structure
      ↓
Appropriate Mentor Behavior
      ↓
Learner Action
      ↓
Relevant State Preserved
      ↓
Next Dependent Lesson
```

The pillars can work together, but each can also be explored or implemented independently.

---

## 6. Framework Characteristics

### Spreadsheet-Based Authoring

The primary Creator Kit workflow uses spreadsheets so educators and technical authors can configure curricula and prompt-generation rules without first building a custom software platform.

This lowers the entry barrier to authoring while still allowing technically advanced curricula.

> **Low entry barrier does not mean low ceiling.**

---

### Technical Ecosystem Adaptation

Coding5s is not tied to one programming language or stack.

Technical rules allow the same learning architecture to behave differently for environments such as:

```text
Python
Elixir
Dart
SQL
Networking
Data Analysis
Cloud Infrastructure
```

The framework should adapt to the conventions of the target ecosystem rather than force every subject through identical rules.

---

### AI Provider Independence

Coding5s is not architecturally dependent on one specific LLM provider.

However, this does not mean every model will behave identically.

Instruction-following, context limits, reasoning capability, formatting, and output quality may vary across models and model versions.

---

### Human-Language Adaptation

Course-generation workflows can target different human output languages.

For languages where ordinary model performance requires stronger grounding, **Language Seed Contexts** can provide additional linguistic information and constraints.

These contexts may reduce linguistic drift or dominant-language interference, but they do not guarantee correctness.

Authoritative linguistic resources and fluent or native-speaker review remain important for production-quality material.

---

### Architecture as Structured Data

Coding5s represents substantial parts of curriculum generation through structured:

* variables,
* rules,
* tables,
* formulas,
* prompts,
* and reusable context.

This allows changes to be propagated systematically instead of manually rewriting every lesson.

The exact workflow depends on the Creator Kit implementation.

---

## 7. Framework vs. Research Lab

The core Coding5s architecture should remain distinct from experimental ideas explored in the **Research Lab**.

Examples include:

* General Seed Context,
* Knowledge Domain Protocol,
* Reverse Pitch Marketing,
* Ephemeral Context Protocol,
* M2M Semantic Notation,
* and other experimental architectures.

Some Research Lab concepts may eventually become useful implementations.

Others may remain experiments or be discarded.

Their presence in the repository does not make them requirements of the three core pillars.

---

## 8. Methodology Boundary

Coding5s is a developing open-source methodology and implementation framework.

It should not currently be interpreted as proof that:

* the five stages universally improve learning,
* Controlled Cognitive Friction guarantees retention,
* AI dependence is eliminated,
* Seed Contexts guarantee linguistic accuracy,
* Stateful5s guarantees correct model recall,
* or the framework outperforms other educational approaches.

Those are questions for testing and research.

The architecture makes a more modest claim:

> **When AI can provide answers almost instantly, learning activities should be deliberately structured so the learner still has meaningful work to understand, diagnose, build, improve, and extend.**

Este archivo ahora ocupa un lugar bastante claro en la raíz:

```text
README.md
→ What is Coding5s?

METHODOLOGY.md
→ How does the architecture work?

GLOSSARY.md
→ What do the terms mean?

FAQ.md
→ What does it mean for different users?

CONTRIBUTING.md
→ How can I participate?

LICENSE
→ What am I legally allowed to do?
```