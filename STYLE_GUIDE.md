# Notebook Style Guide

This training uses a consistent visual and teaching pattern in every notebook.

The style uses local SVG icons instead of emoji characters so notebooks render correctly on all student machines.

## Signature Learning Loop

```text
QUESTION -> DATA -> CODE -> EVIDENCE -> DECISION
```

Meaning:

- QUESTION: What are we trying to understand?
- DATA: What information do we have?
- CODE: What Python step will we run?
- EVIDENCE: What does the output show?
- DECISION: What can we say or do based on the evidence?

## Notebook Block Types

Each concept should use these blocks.

### Concept Card

Explains the idea in simple language.

Use it for:

- Definitions
- Why the concept matters
- Real-life examples
- Common confusion

### Code Lab

One focused code block for one concept.

Use it for:

- A small runnable example
- Clear variable names
- Output that students can inspect

### Read the Output

Guides students to interpret what they see.

Use it for:

- What changed?
- What is the most important value?
- What pattern is visible?
- What question should we ask next?

### Practice Task

A short student task after a concept.

Use it for:

- Change one value
- Add one row
- Try one extra column
- Write one observation

## Color Language

Markdown callout cards use a simple color system:

- Blue: concept or key idea
- Green: code goal
- Yellow: read the output
- Red: common mistake or caution

## Icon Language

Use local SVG icons consistently:

- `assets/icons/goal.svg`: learning goal
- `assets/icons/concept.svg`: concept explanation
- `assets/icons/code.svg`: code lab
- `assets/icons/read-output.svg`: output interpretation
- `assets/icons/practice.svg`: practice task
- `assets/icons/caution.svg`: common mistake or caution
- `assets/icons/recap.svg`: recap or decision
- `assets/icons/map.svg`: learning map
- `assets/icons/loop.svg`: learning loop

## Writing Rules

- Use simple language first.
- Use technical terms only after the simple explanation.
- Keep one concept tied to one code block.
- Avoid advanced modeling terms in Day 1 unless the topic requires them.
- Prefer practical examples over abstract theory.

## Rendered Examples

The raw markdown below produces each block type. Copy these exactly when authoring new notebooks.

### Concept Card

```html
<div style="background:#EAF3FF; border-left:6px solid #2F80ED; padding:14px; border-radius:6px;">
<img src="../../../assets/icons/concept.svg" width="22" style="vertical-align:middle; margin-right:6px;"><b>Concept</b><br>
A variable is a name that stores a value.
</div>
```

### Code Lab

```html
<div style="background:#E9F8EF; border-left:6px solid #27AE60; padding:14px; border-radius:6px;">
<img src="../../../assets/icons/code.svg" width="22" style="vertical-align:middle; margin-right:6px;"><b>Code Lab</b><br>
Create a few variables for a customer purchase example.
</div>
```

### Read the Output

```html
<div style="background:#FFF8E1; border-left:6px solid #F2C94C; padding:14px; border-radius:6px;">
<img src="../../../assets/icons/read-output.svg" width="22" style="vertical-align:middle; margin-right:6px;"><b>Read the Output</b><br>
Check how each variable name makes the stored value understandable.
</div>
```

### Practice Task

```html
<div style="background:#F7FBFF; border-left:6px solid #56CCF2; padding:14px; border-radius:6px;">
<img src="../../../assets/icons/practice.svg" width="22" style="vertical-align:middle; margin-right:6px;"><b>Try It</b><br>
Change one value in the list and predict how the total will change before running the cell again.
</div>
```

## Complete Concept Cycle Example

This shows the full block sequence from Notebook 02 Concept 1 (Python Variables).

**Step 1: Concept Card** -- introduces the idea.

**Step 2: Code Lab** -- states the goal before the student runs code.

**Step 3: Read the Output** -- directs interpretation of the result.

**Step 4: Try It** -- gives one small student action.

| Block | Color | Border | Purpose |
|---|---|---|---|
| Concept Card | Blue (`#EAF3FF`) | `#2F80ED` | Define the idea in simple language |
| Code Lab | Green (`#E9F8EF`) | `#27AE60` | State the goal before the student runs code |
| Read the Output | Yellow (`#FFF8E1`) | `#F2C94C` | Guide interpretation of the result |
| Try It | Light blue (`#F7FBFF`) | `#56CCF2` | Give one small student action |
