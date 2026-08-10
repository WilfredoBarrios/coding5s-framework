# 🐝 Pillar 2: AI Mentor Swarm & Behavioral Layer

**Pillar 2** is the behavioral layer of the Coding5s Framework.

While **Pillar 1** defines what the learner practices and how the five-stage progression is structured, Pillar 2 defines **how the AI should behave while supporting that practice**.

This directory contains specialized **Mentor Prompts** and behavioral specifications designed to apply **Controlled Cognitive Friction**, adapt guidance to the task, and reduce the risk that AI assistance replaces the reasoning the learner is expected to perform.

> **Learn With AI. Don’t Outsource Your Thinking.**

---

## 🧠 What a Coding5s Mentor Does

General-purpose AI assistants are optimized to be helpful and may provide complete solutions even when doing so weakens the intended learning task.

Coding5s Mentors introduce behavioral constraints that change **how assistance is delivered**.

A mentor may:

- ask the learner to explain their current reasoning,
- request missing context before proceeding,
- provide diagnostic questions instead of immediate fixes,
- reveal hints progressively,
- critique an attempted solution,
- surface relevant constraints,
- adapt explanation depth,
- challenge design decisions,
- or require the learner to defend a conclusion.

The objective is not to make the AI unhelpful.

It is to provide **the right amount of help for the cognitive task being practiced**.

---

## ⚙️ Common Mentor Components

Individual mentors may use different structures, but several patterns recur across Pillar 2.

### 1. Role & Communication Style

A mentor can adopt a specialized professional role or recognizable conversational style to make interactions easier to understand and more engaging.

Personality is optional.

The behavioral objective matters more than theatrical presentation.

---

### 2. Context Adaptation

Mentors may adapt to available information such as:

- programming language or technical domain,
- learner level,
- current stage,
- submitted code or artifact,
- learner explanation,
- and selected output language.

Adaptation should be based on supplied or reasonably inferable context rather than invented assumptions about the learner.

---

### 3. Input Gates

When an exercise requires learner reasoning, a mentor may request the learner's interpretation before providing deeper assistance.

For example:

```text
Artifact Submitted
       ↓
Learner Explanation Missing
       ↓
Ask What They Think
       ↓
Continue With Guided Analysis
````

The purpose is to preserve active participation, not to block the learner unnecessarily.

---

### 4. Assistance Boundaries

Coding5s does **not** impose a universal rule that AI can never generate code.

Depending on the learning task, a mentor may provide:

```text
examples
scaffolding
broken code
partial implementations
diagnostic hints
documentation guidance
review feedback
```

The important boundary is:

> **Do not perform the cognitive task that the learner is currently expected to practice.**

A Debug mentor may avoid supplying the final correction.

A Practice mentor may freely provide reference examples.

A Refactor mentor may critique a solution while requiring the learner to implement the changes.

The boundary changes with the task.

---

### 5. Structured Interaction

Mentors may use consistent response structures when those structures improve learning.

Examples include:

* diagnostic checkpoints,
* progressive hints,
* comparison tables,
* reasoning prompts,
* review scorecards,
* reflection questions,
* or compact state summaries.

Formatting is a tool, not an invariant.

A mentor should not force complex output structures when a simpler interaction works better.

---

## 🛠️ Included Mentor Archetypes

This directory contains early reference implementations demonstrating different behavioral patterns.

### 🏗️ Legacy Architect (`legacy_architect.md`)

**Target:** Reverse engineering and brownfield reasoning.

The mentor helps learners understand unfamiliar existing code before modifying it.

Typical behaviors include:

* mapping structural relationships,
* identifying risky areas,
* discussing code smells,
* exploring likely consequences of changes,
* and encouraging a mental test plan before editing.

---

### 🔄 Paradigm Bridge

A two-part mentor pattern designed to help learners move between programming paradigms.

#### Part 1 — Concept Illuminator (`bridge_mentor_s1.md`)

Introduces the conceptual differences between the source and target paradigms.

It may provide:

* conceptual mappings,
* analogies,
* partial scaffolding,
* and a structured first attempt.

#### Part 2 — Sparring Partner (`bridge_mentor_s2.md`)

Reviews the learner's attempted translation and challenges assumptions inherited from the previous paradigm.

Its purpose is not simply to mark an answer wrong, but to help the learner recognize **why an old mental model does not map cleanly to the new paradigm**.

---

### 📐 Abstraction Architect (`math_calculus_architect.md`)

**Target:** Mathematics, calculus, and geometric reasoning.

This mentor emphasizes conceptual and visual understanding before mechanical manipulation.

Depending on the problem, it may use:

* diagrams,
* computational experiments,
* Python visualization,
* numerical examples,
* or guided conceptual questions.

The objective is to connect symbolic operations with the mathematical relationships they represent.

---

## 🧩 Mentors Are Behavioral Components

A Coding5s Mentor is not necessarily a complete curriculum.

Conceptually:

```text
PILLAR 1
Learning Task
     +
Stage Context
     ↓

PILLAR 2
Mentor Behavior
     ↓

AI-Assisted Interaction
     ↓

Learner Reasoning + Action
```

The same mentor behavior may potentially support multiple languages, libraries, or domains when its constraints remain relevant.

Likewise, the same lesson can use different mentor behaviors depending on the learning objective.

---

## 🧪 Building New Mentors

New mentor archetypes can target specific forms of reasoning.

Possible examples include:

* code review,
* debugging,
* architecture,
* performance,
* security,
* accessibility,
* data analysis,
* technical communication,
* troubleshooting,
* or paradigm transition.

A useful mentor specification should clearly document:

1. **Target Task** — What kind of reasoning does it support?
2. **Expected Inputs** — What should the learner provide?
3. **Behavioral Rules** — How should the AI respond?
4. **Assistance Boundary** — What should the mentor avoid doing for the learner?
5. **Adaptation Rules** — What context can change its behavior?
6. **Known Limitations** — Where does the prompt behave inconsistently?
7. **Example Interactions** — What does successful use look like?

---

## 🔬 Testing Mentor Behavior

Mentor prompts should be tested through realistic interactions rather than judged only by reading the prompt.

Useful observations include:

* whether the mentor preserves the intended assistance boundary,
* whether it asks unnecessary questions,
* whether hints become too revealing,
* whether instructions degrade during long interactions,
* whether formatting remains useful,
* and whether behavior changes significantly across models.

Cross-model testing is encouraged, especially when claiming that a mentor is model-agnostic.

Model behavior can change over time, so mentor prompts should be treated as **behavioral specifications that may require iteration**, not permanent guarantees.

---

## 🚀 How to Use a Mentor

Typical workflow:

1. Open the desired mentor `.md` file.
2. Copy the mentor specification.
3. Provide it through the most appropriate instruction mechanism available in the selected AI platform.
4. Supply the requested learner input.
5. Interact with the mentor while performing the actual learning task.

Exact system-prompt, custom-instruction, project, or conversation setup will depend on the AI platform being used.

---

## 🔗 Relationship to the Other Pillars

```text
PILLAR 1
What should the learner practice?
How does the difficulty progress?

        ↓

PILLAR 2
How should AI behave
while supporting that practice?

        ↓

PILLAR 3
What useful context should persist
as the learner progresses?
```

Pillar 2 can also be used independently wherever an AI interaction benefits from explicit behavioral boundaries and learner-centered guidance.

---

## 🐝 The Swarm Idea

The term **Mentor Swarm** does not require many AI agents to run simultaneously.

It describes a collection of specialized mentor behaviors that can be selected according to the learning task.

```text
One Learner
    ↓
Different Cognitive Problems
    ↓
Different Mentor Behaviors
```

Future implementations may orchestrate multiple mentors together, but the core value of Pillar 2 already exists when a single specialized mentor changes how AI assistance is delivered.

> **The mentor should help the learner think better—not simply think for them.**
