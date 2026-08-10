# 📑 Reverse Pitch Marketing (RPM) Protocol Specification

> **Technical Specification: System Mechanics, Evaluation Constraints, and Evidence-Bounded Architecture for AI-Assisted Buyer Enablement.**

---

## 1. Executive Abstract

Traditional B2B outbound processes can suffer from trust asymmetries, promotional overstatement, and cognitive fatigue on the part of technical and business evaluators. The **Reverse Pitch Marketing (RPM)** technique explores an alternative architecture by transitioning part of discovery from a provider-driven presentation into a buyer-controlled, AI-assisted evaluation workflow.

By separating the outreach layer from an evidence-bounded evaluation instrument, RPM allows the recipient to perform a structured gap analysis inside an organization-approved Large Language Model (LLM) environment. This specification defines the architectural patterns, semantic constraints, evaluation guardrails, and interaction states used by the technique.

The objective is not to make the LLM a neutral source of truth. It is to give the buyer a structured mechanism for interrogating the provider's evidence from their own operational perspective.

---

## 2. Theoretical Foundations: Interpretation Localization & Evaluation Transfer

RPM operates as an experimental distribution counterpart to ideas used elsewhere in the **Coding5s** ecosystem.

While Coding5s uses *Controlled Cognitive Friction* to preserve learner reasoning during AI-assisted learning, RPM applies a different structural inversion to technology evaluation: instead of asking the provider to perform all interpretation for the buyer, part of that interpretation is transferred into the buyer's own AI-assisted workflow.

### Traditional Outreach Architecture

```text
[Provider]
     │
     └── Promotional Interpretation
                  ↓
             [Evaluator]
```

### RPM Architectural Inversion

```text
[Provider]
     │
     └── Evidence Package + Evaluation Instrument
                          ↓
                 [Buyer's Selected LLM]
                          ↓
                Evidence-Bounded Review
                          ↓
                     [Evaluator]
```

This architecture introduces three mechanisms:

1. **Evaluation Transfer:** The assessment is executed inside an AI environment selected or approved by the receiving organization, reducing the need for the provider to receive the buyer's internal evaluation context.

2. **Interpretation Localization:** The model helps map technical evidence—such as architecture, implementation artifacts, Seed Contexts, or Stateful5s components—against the terminology, responsibilities, risks, KPIs, or operational priorities relevant to the evaluator.

3. **Evidence-Bounded Review:** The evaluation instrument instructs the model to distinguish conclusions supported by the supplied material from reasonable inference and information that remains unestablished.

RPM transfers part of the interpretation process.

It does not guarantee neutral interpretation, correct conclusions, privacy, or factual truth.

---

## 3. The 5 RPM Design Guardrails

Buyer-side evaluation occurs in environments the provider does not control. RPM therefore uses five practical guardrails intended to reduce friction and improve evaluation quality.

These guardrails are design patterns rather than security guarantees.

### A. Low-Friction Entry

* **Failure Risk:** Executive inertia or immediate cognitive overload prevents the evaluation instrument from being tested.
* **Mitigation:** Keep the introductory communication deliberately short and focused on one clear reason to inspect the evidence. A practical RPM implementation may target approximately 100 words or fewer for the initial outreach.

### B. Governance Boundary

* **Failure Risk:** Enterprise governance, data-handling policies, or compliance requirements prevent the recipient from processing supplied material.
* **Mitigation:** Clearly identify the nature, source, and licensing of the evidence package and instruct recipients to use only organization-approved AI environments. When applicable, describe Coding5s material as publicly accessible and released under the **MIT License**. MIT-licensed material is not equivalent to public-domain material.

### C. Evidence Priority

* **Failure Risk:** Large technical packages make it difficult for either the human evaluator or the LLM to identify the most important architectural information.
* **Mitigation:** Place a concise Executive Evidence Summary at the beginning of the package containing the technology's purpose, existing implementation, available evidence, experimental components, known limitations, and verification paths.

### D. Portable Evaluation Instrument

* **Failure Risk:** Complex JSON schemas, scripts, custom interfaces, or specialized execution requirements create unnecessary adoption friction.
* **Mitigation:** Keep the primary evaluation instrument as a **single continuous paragraph of natural-language prose** that can be selected, copied, and pasted into common LLM interfaces without additional tooling.

### E. Document / Instruction Separation

* **Failure Risk:** Text contained inside supplied or retrieved documentation may conflict with the evaluation instructions or contain embedded prompt-like directives.
* **Mitigation:** Explicitly instruct the evaluating model to treat documentation as evidence to analyze rather than instructions to execute.

This separation can reduce instruction confusion but **does not constitute complete protection against prompt injection or malicious documents**.

---

## 4. Semantic Constraints of the Evaluation Payload

The RPM evaluation instrument uses five semantic boundaries intended to reduce promotional bias and keep the assessment tied to inspectable evidence.

1. **Evaluator Framing:** Instruct the model to operate as a critical technical or business evaluation assistant rather than as a salesperson or advocate.

2. **Evidence Grounding:** Require conclusions to remain anchored to the supplied specifications and explicitly distinguish:
   - **SUPPORTED** — demonstrated directly by evidence.
   - **INFERRED** — reasonable interpretation derived from evidence.
   - **NOT ESTABLISHED** — unsupported by the supplied material.

3. **Context / KPI Mapping:** Evaluate documented technical components against the responsibilities, operational requirements, KPIs, risks, or priorities supplied by the recipient.

4. **Adversarial Counterweight:** Require the model to actively search for meaningful deployment risks, dependencies, architectural limitations, missing evidence, and reasons against adoption instead of producing only positive conclusions.

5. **Fault-Tolerant Conversational Branching:** The initial assessment may close with three relevant follow-up paths, while accepting subsequent responses in either natural language or numerical form rather than requiring a rigid command syntax.

The central semantic rule is:

> **Absence of evidence must remain absence of evidence.**

---

## 5. System Execution States & Resilience Patterns

Once executed inside the buyer's selected environment, a typical RPM interaction can follow this functional loop:

```text
[State: Evidence Ingestion]
            │
            ▼
[Evidence-Bounded Assessment]
            │
            ▼
[State: Follow-Up Exploration]
            │
            ├── Methodology / Conceptual Model
            ├── Technical Architecture
            └── Implementation / Deployment
```

The exact follow-up categories may change according to the technology and evaluator.

RPM should favor natural conversation over rigid menu enforcement.

---

### 🚨 Operational Failures & Mitigation

#### Inertia State

If the recipient does not execute the evaluation instrument, the provider may optionally send a pre-generated **Evidence-Bounded Assessment** as a demonstration of the intended workflow.

The recipient should still be encouraged to perform their own evaluation using their preferred or organization-approved AI environment.

#### Generic Evaluation State

If the model produces vague or excessively positive conclusions, strengthen the evaluation contract by explicitly requiring:

```text
Limitations
Missing Evidence
Dependencies
Reasons Against Adoption
Claims Requiring Verification
```

#### Insufficient Evidence State

If the supplied documentation cannot support a requested conclusion, the model should return:

```text
NOT ESTABLISHED
```

and identify what additional evidence would be required.

#### Valuable Negative Finding

If the evaluation exposes a genuine architectural weakness, operational dependency, security concern, or unhandled edge case, the finding should be verified rather than treated as a failure of the technique.

If valid, the provider can:

- acknowledge the limitation,
- document it,
- correct it,
- create a roadmap issue,
- or explain why it represents an accepted design trade-off.

A successful Reverse Pitch does not require a positive conclusion.

It requires a more inspectable one.