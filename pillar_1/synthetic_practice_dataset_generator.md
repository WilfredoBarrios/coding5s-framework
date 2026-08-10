# 🧪 Synthetic Practice Dataset Generator

**Status: Active Tool / Practical Implementation**

Developed within the **Coding5s ecosystem** to improve hands-on technical learning by generating small, realistic, reproducible datasets designed specifically for practice.

---

## 📌 Overview

The **Synthetic Practice Dataset Generator** creates realistic synthetic files that can be used directly inside Coding5s lessons whenever the topic requires manipulating structured or semi-structured data.

Examples include:

- CSV files
- JSON files
- nested JSON
- Excel workbooks
- NumPy arrays
- logs
- text files
- Parquet files

The generator itself uses **Python as the generation engine**, while the resulting dataset is intended to remain usable from any programming language or technical environment capable of reading the selected format.

Its purpose is not to generate large benchmarking datasets.

Its purpose is to create **small, pedagogically engineered practice artifacts** that make technical lessons feel closer to real-world work.

---

## 🎯 The Problem It Solves

Many technical lessons become artificial when the learner is asked to practice concepts such as:

- file reading and writing,
- JSON parsing,
- CSV processing,
- data cleaning,
- filtering,
- grouping,
- joins,
- log analysis,
- regular expressions,
- spreadsheet operations,
- serialization,
- or data transformation

without having realistic data to work with.

A lesson about `json.load()`, for example, becomes much more meaningful when the learner receives an actual nested JSON file instead of copying a tiny dictionary directly from the lesson.

The same applies to CSV files, logs, spreadsheets, relational structures, and other common technical artifacts.

The Synthetic Practice Dataset Generator was created to close that gap.

Instead of teaching only the operation:

```text
Learn the syntax
      ↓
Read an example
      ↓
Imagine the data
````

the learner can work with:

```text
Learn the concept
      ↓
Receive a realistic synthetic file
      ↓
Load it
      ↓
Inspect it
      ↓
Transform it
      ↓
Debug it
      ↓
Use it inside the lesson
```

This makes the practice environment more concrete and helps Coding5s simulate more realistic technical work.

---

## 🧠 Why It Was Created for Coding5s

Coding5s is built around active practice rather than passive explanation.

As the framework expanded into topics involving data manipulation and external files, a recurring problem appeared:

> **How can a lesson remain realistic if every learner needs a useful practice file, but the course cannot depend on proprietary, private, or manually prepared datasets?**

Synthetic data offered a practical solution.

The generator can create a new practice artifact based on:

* the current topic,
* the learner's level,
* the target technology or library,
* the type of lesson,
* and the desired use case.

The dataset is therefore not generated independently from the lesson.

It is **engineered around the skill being practiced**.

Examples:

```text
groupby
→ meaningful categorical dimensions

nested JSON
→ nested objects and arrays

joins
→ related keys or tables

time series
→ dates and temporal variation

regex
→ structured text patterns

missing values
→ controlled null values

log parsing
→ realistic log lines
```

Every important field, structure, relationship, or intentional imperfection should exist for a pedagogical reason.

---

## 🤖 Designed for AI-Assisted Practice

A second design constraint is especially important inside Coding5s:

> **The dataset should normally remain small enough to be attached directly to an AI chat and analyzed as a complete file during a lesson.**

Large synthetic datasets may be useful for benchmarking or performance testing, but they can become counterproductive in an AI-assisted learning workflow.

A large CSV or deeply nested JSON file consumes more context, increases analysis complexity, and may make it harder for the model and learner to reason about the complete artifact at once.

For this reason, the generator defaults to **CHAT_OPTIMIZED** datasets.

Typical default ranges are intentionally small:

```text
CSV / Tabular
20–40 rows

Simple JSON
15–25 records

Nested JSON
10–20 records

LOG / TXT
10–20 lines

NumPy Arrays
20–40 elements
```

These are not universal technical limits.

They are pedagogical defaults intended to balance:

```text
Realism
+
Enough variation to practice
+
Human readability
+
AI context manageability
```

Larger datasets can still be generated when needed through the `EXTENDED` or `CUSTOM` size modes.

---

## ⚙️ Core Design Principles

### 1. Python Generates the Data

Python is used as the standard generation engine to keep the system simple and consistent.

The generated artifact remains independent from the generator whenever the file format allows it.

For example:

```text
Python Generator
      ↓
customers.json
      ↓
Python
Elixir
Java
Dart
JavaScript
Rust
or another compatible environment
```

---

### 2. The Topic Defines the Dataset

The dataset must make the requested technical skill actionable.

The generator should not create generic datasets and then attempt to force the lesson onto them.

---

### 3. Reproducibility Matters

Random generation must use deterministic seeds so the same script can reproduce the same dataset.

This is especially useful in educational workflows where examples, expected structures, and exercises depend on stable data.

---

### 4. Data Quality Must Be Pedagogical

Realistic data does not automatically mean dirty data.

If the lesson is about basic file handling, the dataset should normally be clean.

If the lesson is about:

```text
data cleaning
missing values
outliers
regex
validation
error handling
log parsing
```

then controlled imperfections can be intentionally introduced.

Errors should exist because the learner needs to practice them—not simply because real-world data can be messy.

---

### 5. Small Does Not Mean Trivial

CHAT_OPTIMIZED datasets should remain small enough for AI-assisted analysis while still containing meaningful structure, variation, relationships, and realistic values.

The objective is:

> **Minimum useful size, not minimum possible size.**

---

## 📦 Generator Outputs

The generator produces more than the dataset-generation script.

A complete execution can provide:

1. **Dataset Description**
   Explains what the synthetic dataset represents and why it is useful for the lesson.

2. **Python Generator Code**
   Reproducible Python code that creates and exports the dataset.

3. **Student Exercise Ideas**
   Practical activities based specifically on the generated artifact.

4. **AI Practice Note**
   Indicates the dataset size, structural complexity, and whether it is suitable for full-file analysis inside an AI chat.

5. **Dataset Page Payload**
   A compact factual description of the generated artifact intended to be passed to a separate page-generation prompt.

The page payload keeps dataset generation and website generation as separate responsibilities:

```text
Synthetic Dataset Generator
          ↓
Dataset File
+
Dataset Page Payload
          ↓
Dataset Page Generator
          ↓
Coding5s Resource Page
```

This separation allows the dataset-generation engine to remain focused on educational data while the web-generation engine can evolve independently with the Coding5s website design system.

---

## 🧩 Role Inside Coding5s

The Synthetic Practice Dataset Generator does not decide what the learner should study.

It supports the curriculum by creating the **practice artifact required by the lesson**.

Conceptually:

```text
Curriculum Generator
        ↓
What should be practiced?

Synthetic Dataset Generator
        ↓
What realistic data does the learner need
to practice it?

Coding5s Lesson
        ↓
Learner manipulates the artifact
with AI-assisted guidance
```

This allows file-based lessons to move closer to actual technical work without requiring manually curated datasets for every topic.

---

## 🚀 Master Prompt

```markdown
[ROLE]: Senior Data Engineer / Software Architect

[TARGET PRACTICE TECHNOLOGY/LIBRARY]: (e.g., Python json, Pandas, NumPy, Elixir, Java, Dart, SQL)
[STUDENT LEVEL]: Beginner | Intermediate | Advanced
[USE CASE / INDUSTRY]: (Optional — AUTO if empty)
[LESSON TYPE]: Topic | PROJECT
[TOPIC OR PROJECT NAME]: [INSERT TOPIC OR PROJECT]
[PREVIOUS TOPICS INCLUDED]: (Only if PROJECT)
[OUTPUT LANGUAGE]: English


# DATASET CONFIGURATION

[FILE FORMAT]: AUTO | CSV | JSON | XLSX | PARQUET | NPY | LOG | TXT
[DATASET SIZE]: CHAT_OPTIMIZED | EXTENDED | CUSTOM
[CUSTOM RECORD LIMIT]: (Optional — only used if DATASET SIZE = CUSTOM)
[RANDOM SEED]: 42
[DATA QUALITY MODE]: AUTO | CLEAN | CHALLENGED


# OBJECTIVE

Generate a realistic, reproducible synthetic practice dataset specifically engineered to make the requested technical topic or project actionable.

The dataset-generation script MUST always be written in Python. The resulting dataset file should remain usable independently of Python whenever the selected format permits it.

By default, optimize the dataset for direct attachment to an AI chat and full-file analysis during an AI-assisted Coding5s lesson. Prioritize pedagogical usefulness, clarity, and manageable context size over unnecessary volume or complexity.


# 1. DATASET DESIGN LOGIC

## Domain Inference

If [USE CASE / INDUSTRY] is empty, infer a realistic domain that best exposes the requested skill. Examples include e-commerce, inventory, IoT, system logs, finance, user activity, marketing, and technical support.

Do not select a domain merely for decoration; it must help make the topic actionable.


## Topic / Project Engineering

Design the dataset around [TOPIC OR PROJECT NAME].

Every important field, structure, relationship, or intentional imperfection MUST have a pedagogical purpose connected to the requested topic or project.

Examples:

- groupby → useful categorical dimensions
- joins → related keys or relational structures
- nested JSON → meaningful nested objects and lists
- time series → dates and temporal variation
- outliers → controlled extreme values
- regex → relevant textual patterns
- missing values → strategic null values
- sorting → varied sortable values

If [LESSON TYPE] is PROJECT, also incorporate [PREVIOUS TOPICS INCLUDED] without making the dataset unnecessarily complex.


## Difficulty Scaling

Beginner:
- 5–8 meaningful fields
- simple structures and relationships

Intermediate:
- 8–15 meaningful fields
- richer but understandable relationships

Advanced:
- richer structures, correlations, temporal relationships, or domain complexity when useful

Data imperfections are controlled exclusively by [DATA QUALITY MODE].


# 2. CHAT-OPTIMIZED SIZE RULES

When [DATASET SIZE] = CHAT_OPTIMIZED, keep the dataset deliberately small enough for a learner to attach the complete file to an AI conversation and work with it during a lesson.

Recommended limits:

- CSV / tabular data: 20–40 rows
- Simple JSON: 15–25 records
- Nested JSON: 10–20 records
- LOG / TXT: 10–20 lines
- NumPy arrays: 20–40 elements
- XLSX: normally 20–40 rows per primary table; additional sheets only when the topic genuinely requires them

Choose toward the lower end when individual records are structurally dense.

When [DATASET SIZE] = EXTENDED:
Generate a larger but still pedagogically reasonable dataset. Clearly warn in the final AI Practice Note that complete-file analysis inside one AI chat may be less convenient.

When [DATASET SIZE] = CUSTOM:
Use [CUSTOM RECORD LIMIT]. If the requested size is likely excessive for full-file AI analysis, generate it as requested but explicitly warn the user in the AI Practice Note.


# 3. DATA QUALITY LOGIC

Evaluate [DATA QUALITY MODE].

AUTO:
- If the topic involves cleaning, error handling, regex, log parsing, missing values, outliers, malformed input, validation, or similar skills, inject controlled and realistic challenges.
- Otherwise generate clean, correctly formatted, standard data.

CLEAN:
- Do not inject intentional nulls, duplicates, malformed values, formatting inconsistencies, or unrelated errors.

CHALLENGED:
- Inject controlled imperfections appropriate to the topic and student level.

Never inject problems unrelated to the skill being practiced.

Beginner challenges should be few and obvious enough to understand.
Intermediate challenges may be more varied.
Advanced challenges may involve multiple interacting issues when pedagogically justified.


# 4. DATA REALISM

Use realistic values, categorical cardinality, statistical distributions, and simple relationships only when they improve the exercise.

Examples of useful relationships:

- revenue = price × quantity
- demand influences stock
- category influences discount
- timestamps produce temporal patterns

Avoid unnecessary statistical sophistication.

Categorical fields used for grouping or aggregation should normally contain roughly 3–10 useful unique values.

Do not use real personal data.


# 5. STRICT GENERATION RULES

- Generator code MUST be Python.
- Use Faker, NumPy, pandas, or other Python libraries only when useful.
- Set deterministic seeds for every random generator used.
- Use [RANDOM SEED] consistently.
- Keep generated values internally consistent.
- Keep the dataset reproducible.
- Do not generate trivial datasets.
- Do not add decorative or pedagogically useless fields.
- Generate exactly ONE primary dataset file whenever possible.
- Multiple files are allowed ONLY when the requested topic inherently requires multi-file processing and cannot be represented appropriately in one file.
- XLSX may contain multiple sheets when relational practice requires them.
- The selected format must directly support the requested topic.
- Save generated files in the current directory.


# 6. FILE FORMAT & NOMENCLATURE

If [FILE FORMAT] = AUTO, choose the format that best supports the topic.

Typical choices:

- tabular analysis → CSV
- nested structures → JSON
- NumPy arrays → NPY
- spreadsheet practice → XLSX
- log parsing → LOG or TXT
- columnar analytical workflows → PARQUET

Name the file using a short version of [TOPIC OR PROJECT NAME]:

- snake_case
- maximum 4 words
- lowercase letters, numbers, and underscores only
- no parentheses or special characters

Never use generic names such as:

dataset.csv
data.json
datos.csv


# 7. OUTPUT FORMAT

Generate the following sections in [OUTPUT LANGUAGE].


## 1. Dataset Description

Briefly explain:

- what the dataset represents
- the scenario it simulates
- the technical skill it enables
- why its structure is useful for the requested topic


## 2. Complete Python Generator Code

Provide clean, commented, executable Python code.

The code must include:

- required imports
- deterministic random seeds
- synthetic data generation
- appropriate data structure creation
- file export
- a small preview appropriate to the selected format

If third-party packages are required, include a first-line comment containing only the necessary installation command.

The generated file must match the Dataset Description and Dataset Page Payload exactly.


## 3. Student Exercise Ideas

Generate 5–8 practical exercises aligned with:

- [TOPIC OR PROJECT NAME]
- [STUDENT LEVEL]
- the actual generated schema
- the actual data-quality characteristics

Do not propose exercises that require information or structures absent from the generated file.


## 4. AI Practice Note

Output a compact block using exactly this structure:

[AI PRACTICE NOTE]

Dataset Size Mode:
Actual Records / Lines / Elements:
Structure Complexity:
AI Chat Suitability:
Recommendation:

For CHAT_OPTIMIZED datasets, explicitly state that the dataset was intentionally kept small for complete-file attachment and AI-assisted lesson analysis.

For EXTENDED or large CUSTOM datasets, mention when a smaller CHAT_OPTIMIZED version may be preferable for full-file AI analysis.


## 5. Dataset Page Payload

Generate a structured factual block using exactly this heading:

[DATASET PAGE PAYLOAD]

Include:

TITLE:
FILE_NAME:
FILE_FORMAT:
FILE_SIZE_MODE:
RECORD_COUNT:
STUDENT_LEVEL:
TARGET_TOPIC:
TARGET_TECHNOLOGY_LIBRARY:
USE_CASE:
DESCRIPTION:
SCHEMA:
STRUCTURE:
DATA_QUALITY:
INJECTED_CHALLENGES:
RELATIONSHIPS:
PEDAGOGICAL_PURPOSE:
EXERCISES:
GENERATOR:
REPRODUCIBILITY:
AI_PRACTICE_RECOMMENDATION:

The Dataset Page Payload will be passed to a separate web-page generator.

Therefore:

- Include every factual detail needed to accurately describe the generated dataset.
- Reuse the actual exercises generated above.
- Describe nested structures when applicable.
- Clearly state when the dataset is clean.
- Clearly state every intentional challenge when present.
- Do not include HTML, CSS, design instructions, marketing copy, greetings, or requests.
- Do not invent information that is not supported by the generated dataset.
- Keep the payload technical, compact, and self-contained.


# 8. FINAL SILENT VALIDATION

Before producing the final response, silently verify that:

1. The selected file format is appropriate for the requested topic.
2. The generated size follows [DATASET SIZE].
3. The dataset remains reasonably manageable for AI-assisted practice when CHAT_OPTIMIZED is selected.
4. The filename follows the required naming convention.
5. Data quality follows [DATA QUALITY MODE].
6. Every important field or structure has a pedagogical purpose.
7. Random generation is reproducible.
8. The generated code actually exports the intended file.
9. Exercises are possible using the generated dataset.
10. The AI Practice Note accurately reflects the actual dataset size and complexity.
11. The Dataset Page Payload matches the generated artifact exactly.
12. No unsupported or fabricated dataset information appears in the final response.

```

---

## ⚖️ License

Released as part of the **Coding5s Framework** under the applicable repository license.

```

Así queda documentado como una **herramienta real de Coding5s**, no como Crazy Idea: tiene un problema claro, una función concreta y un workflow que ya has usado con buenos resultados. También deja preparada la separación entre **dataset generation** y el futuro **Dataset Page Generator**, sin meter todavía ese segundo prompt dentro del mismo MD. 
```
