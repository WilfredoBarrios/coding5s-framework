# 📖 Coding5s Glossary

This glossary defines technical, pedagogical, and architectural terminology used throughout the **Coding5s Framework** and its Research Lab.

Terms marked with **(*)** are project-specific names or labels used within Coding5s. This notation does **not** imply that the underlying idea is necessarily unique, novel, or exclusive to the framework.

---

## A

### **Accumulated Context (*)**

The selected cumulative state preserved by Stateful5s because later learning interactions still depend on it.

Accumulated Context should contain relevant persistent information rather than a complete transcript of previous conversations.

Examples may include:

- project structure,
- topology state,
- previous technical decisions,
- completed requirements,
- constraints,
- or other domain-specific state.

---

### **Architectural Ledger (*)**

A structured external record used by a Stateful5s implementation to preserve and propagate relevant cumulative state across dependent lessons.

The current reference implementation uses a spreadsheet ledger, but Stateful5s does not require spreadsheets or any specific storage technology.

---

### **Architecture-as-Code (*)**

A Coding5s design idea in which curriculum structures, technical rules, prompts, and configuration variables are represented as structured and reusable artifacts rather than being manually rewritten for every lesson.

The term is used conceptually and should not be confused with Infrastructure as Code.

---

### **Audit-First Approach (*)**

A learning orientation that emphasizes inspecting, understanding, debugging, and improving existing technical artifacts rather than focusing exclusively on creating new ones from scratch.

It is a useful pattern within Coding5s, not a requirement that all learning begin with auditing.

---

## B

### **Brownfield Triage (*)**

Practice centered on understanding and repairing an existing imperfect technical artifact.

Depending on the domain, this may involve:

- broken code,
- configuration errors,
- architectural weaknesses,
- malformed data,
- legacy structures,
- or other existing systems that require diagnosis.

---

## C

### **Coding5s Framework (*)**

An open-source technical-learning framework organized around three architectural pillars:

```text
Pillar 1
5-Stage Learning Architecture & Creator Kit

Pillar 2
AI Mentor Swarm & Behavioral Layer

Pillar 3
Stateful5s & Persistent Cumulative Context
````

Its core five-stage learning progression is:

```text
Practice → Debug → Complete → Refactor → Extend
```

---

### **Cognitive Outsourcing**

The transfer of reasoning, decision-making, diagnosis, or construction to an external tool when those activities are themselves the skills the learner is expected to practice.

Within Coding5s, the concern is not AI assistance itself, but **uncontrolled outsourcing of the relevant cognitive task**.

---

### **Complete (*)**

Stage 3 of the Coding5s learning lifecycle.

The learner receives an incomplete but meaningful technical artifact and must supply a missing component using the surrounding context, requirements, and expected behavior.

The missing work may involve code, configuration, queries, transformations, workflow steps, or other domain-specific components.

---

### **Controlled Cognitive Friction (*)**

The deliberate introduction of useful difficulty into a learning task so the learner must actively reason, inspect, decide, debug, retrieve, or construct instead of receiving every answer immediately.

The objective is not frustration.

Friction should be sufficient to preserve meaningful learner participation while still allowing appropriate guidance.

---

### **Creator Kit (*)**

The spreadsheet-based authoring environment used in Pillar 1 to generate structured Coding5s learning prompts and curricula.

A Creator Kit can combine:

* curriculum topics,
* technical rules,
* stage rules,
* learner-level variables,
* output-language configuration,
* prompt components,
* and optional contextual resources.

It is designed to lower the technical barrier to creating or adapting Coding5s courses without requiring a custom software platform.

---

## D

### **Debug (*)**

Stage 2 of the Coding5s learning lifecycle.

The learner diagnoses and corrects an intentionally flawed or problematic technical artifact.

The objective is to develop **corrective competence** rather than simply obtain a fixed answer.

---

## E

### **ECP — Ephemeral Context Protocol (*)**

A **Crazy Idea** explored inside the Coding5s Research Lab.

ECP investigates whether useful state can be preserved across otherwise ephemeral AI executions by externalizing selected context, terminating the session, and reinjecting that state into a later execution.

Conceptually:

```text
State
  ↓
Inject
  ↓
Execute
  ↓
Extract Updated State
  ↓
Persist Externally
  ↓
Terminate
  ↓
Rehydrate
```

ECP is experimental and is **not required by Stateful5s or the Coding5s core architecture**.

---

### **Epistemic Debt**

The accumulated gap between obtaining a technically acceptable result and actually possessing enough understanding to inspect, explain, repair, modify, or extend that result independently.

Coding5s uses Controlled Cognitive Friction as one possible response to this problem.

The framework does not claim that Epistemic Debt is automatically eliminated by using Coding5s.

---

### **Epistemic Sovereignty (*)**

A Coding5s principle describing the learner's ability and responsibility to inspect, question, validate, and challenge AI-generated outputs rather than automatically accepting them as authoritative.

---

### **Extend (*)**

Stage 5 of the Coding5s learning lifecycle.

The learner takes existing work and adapts it to a new requirement, constraint, capability, integration, or environment.

The objective is transfer:

```text
Understand Existing Work
        ↓
Respond to New Requirements
        ↓
Implement the Change
        ↓
Explain the Decisions
```

---

## G

### **General Seed Context (*)**

An experimental context architecture from the Coding5s Research Lab used to provide persistent or high-priority contextual rules to an LLM.

A General Seed Context may contain information related to:

* communication,
* pedagogy,
* domain behavior,
* terminology,
* cultural context,
* or other persistent constraints.

It is intended to reduce context drift and repeated instruction overhead.

It does **not** literally control or reshape an LLM's latent space, and its effectiveness depends on the model and implementation.

---

### **Greenfield Creation**

Building a new technical artifact from an empty or minimal starting point.

Coding5s supports greenfield creation, but also deliberately includes debugging, completion, refactoring, and extension so learning is not limited to creating new artifacts from scratch.

---

## L

### **Language Seed Context (*)**

A structured context resource intended to provide stronger linguistic grounding when an LLM must communicate in a target human language, particularly when ordinary model performance is inconsistent or affected by dominant-language interference.

It may contain:

* grammatical information,
* terminology,
* morphological patterns,
* communication conventions,
* examples,
* and relevant cultural context.

Language Seed Contexts do not guarantee linguistic correctness. Production-quality contexts should use authoritative sources and, where practical, review by fluent or native speakers.

---

### **Latent Drift**

An informal Coding5s term for observable behavioral drift in which an LLM gradually stops following specialized instructions, constraints, tone, role, or interaction rules during an extended task.

Because internal model representations are not directly observable through ordinary prompting, the term describes **behavioral symptoms**, not a measured movement through latent space.

---

### **Low-Resource Language**

A language for which comparatively fewer high-quality digital, linguistic, educational, or model-training resources are available.

Coding5s explores Language Seed Contexts as one possible way to improve AI-assisted technical education in such languages.

---

## M

### **M2M Semantic Notation (*)**

A highly speculative **Crazy Idea** from the Coding5s Research Lab exploring whether AI systems could exchange structured meaning through a machine-oriented semantic notation that is more compact than conventional human prose.

Its long-term design goals include being:

* human-translatable,
* AI-native,
* linear in representation,
* multidimensional in meaning,
* and potentially usable across different machine-to-machine workflows.

The current notation is experimental and does not establish universal semantics, token savings, or native model support.

---

### **Mentor Swarm (*)**

The collection of specialized AI mentor behaviors that form Pillar 2.

A swarm does not require multiple agents to operate simultaneously.

Different mentors can be selected for different cognitive tasks such as:

* debugging,
* conceptual explanation,
* code review,
* architecture,
* troubleshooting,
* paradigm transition,
* or technical critique.

Future implementations may orchestrate multiple mentors together.

---

## P

### **Post-AI Technical Learning (*)**

Coding5s terminology for technical learning in an environment where generative AI is readily available and learners can obtain explanations, code, configurations, and solutions on demand.

The framework focuses on designing learning activities that use this capability without allowing it to replace the skills being practiced.

---

### **Practice (*)**

Stage 1 of the Coding5s learning lifecycle.

The learner develops initial familiarity by interacting directly with small, understandable examples or technical artifacts.

Activities may include:

* reading,
* reproducing,
* executing,
* observing,
* modifying,
* and comparing results.

AI may participate in generating or explaining the examples.

---

## R

### **Refactor (*)**

Stage 4 of the Coding5s learning lifecycle.

The learner improves something that already works according to criteria appropriate to the technology or domain.

Possible targets include:

* readability,
* maintainability,
* performance,
* robustness,
* security,
* idiomatic design,
* architecture,
* or simplification.

Refactoring criteria should remain ecosystem-specific.

---

### **Research Lab (*)**

The experimental area of the Coding5s repository where concepts can be proposed, tested, criticized, improved, or discarded without being treated as established core framework capabilities.

Research Lab concepts have different maturity levels.

Some are practical experiments, while others—such as ECP and M2M Semantic Notation—are intentionally presented as **Crazy Ideas**.

---

## S

### **Seed Context (*)**

A structured contextual resource designed to provide selected high-priority information or constraints to an LLM.

Seed Contexts may address areas such as:

* language,
* domain knowledge,
* pedagogy,
* communication,
* terminology,
* or behavioral context.

A Seed Context is not defined by a fixed word count and should not be assumed to permanently control model behavior.

---

### **Semantic Isolation (*)**

A Coding5s exercise pattern in which part of the internal logic or transformation is withheld while enough surrounding information remains for the learner to reason about and reconstruct the missing component.

It is commonly associated with **Stage 3: Complete**, but Stage 3 is broader than this single exercise pattern.

---

### **Socratic Guidance**

An assistance strategy based on questions, progressive hints, analogies, reflection, and guided reasoning rather than immediately supplying the entire solution.

Coding5s Mentors may use Socratic guidance when it supports the intended cognitive task.

It is not mandatory for every mentor or every stage.

---

### **State Validation Gate (*)**

A checkpoint used to inspect whether persistent state or learner work satisfies defined conditions before it is propagated or used by later dependent tasks.

Validation may involve:

* automated tests,
* schema checks,
* manual review,
* technical verification,
* or domain-specific criteria.

A validation gate reduces propagation errors but does not guarantee deterministic correctness.

---

### **Stateful5s (*)**

Pillar 3 of the Coding5s Framework.

Stateful5s addresses cumulative learning environments by preserving selected useful state outside the LLM and making that state available to later dependent interactions.

Its defining principle is:

> **Persist what future work depends on.**

Stateful5s does not require:

* a specific spreadsheet schema,
* a Finite State Machine,
* ECP,
* RAG,
* a database,
* or a continuously running AI session.

The current spreadsheet Architectural Ledger is one reference implementation.

---

### **Student Kit (*)**

A learner-facing Coding5s artifact containing the generated material required to perform a course or learning sequence.

Student Kits are intended to expose the learning workflow without unnecessarily exposing the Creator Kit's authoring machinery.

---

### **Synthetic Practice Dataset Generator (*)**

A Coding5s supporting tool that generates deliberately small, reproducible synthetic datasets for technical practice.

It uses Python as the generation engine and can create artifacts such as:

* CSV,
* JSON,
* XLSX,
* Parquet,
* NumPy arrays,
* logs,
* and text files.

Its default dataset sizes are designed to remain practical for human inspection and AI-assisted lesson workflows.

---

## T

### **Technical Rule (*)**

A structured constraint used by the Creator Kit to keep generated lessons aligned with the conventions, tools, paradigms, and practices of the target technical ecosystem.

Technical rules allow the same five-stage architecture to behave differently for environments such as:

```text
Python
Elixir
Dart
SQL
Networking
Data Analysis
```

rather than forcing all subjects through identical programming conventions.

---

## Core Principle

Many Coding5s terms describe **design goals, architectural patterns, or experimental ideas**, not scientifically established laws.

The glossary should therefore be read as:

> **A vocabulary for understanding the Coding5s ecosystem—not a claim that every named concept is unique, universally validated, or applicable to every learning environment.**
