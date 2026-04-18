# Example Transcripts

These are real lecture transcripts from MIT OpenCourseWare, used here to demonstrate t2md's transformation pipeline.

## Lectures

### Lecture 1 — Introduction to Deep Learning
**Folder:** `mit6_7960_lec01_intro_deep_learning/`
**Source:** MIT 6.S191 / 6.7960 Fall 2024 — Lecture 1
**Instructor:** Sara Beery
**License:** CC BY-NC-SA 4.0
**OCW page:** https://ocw.mit.edu/courses/6-s191-introduction-to-deep-learning-january-iap-2023/

### Lecture 2 — Training Neural Networks
**Folder:** `mit6_7960_lec02_training_neural_networks/`
**Source:** MIT 6.S191 / 6.7960 Fall 2024 — Lecture 2
**Instructor:** Sara Beery
**License:** CC BY-NC-SA 4.0
**OCW page:** https://ocw.mit.edu/courses/6-s191-introduction-to-deep-learning-january-iap-2023/

## Try it

```bash
# Short run — Lecture 1 only (auto-selects gpt-4o-mini or claude-haiku)
t2md run examples/mit6_7960_lec01_intro_deep_learning

# Longer run — both lectures together (auto-selects gpt-4o or claude-sonnet)
t2md run examples/mit6_7960_lec02_training_neural_networks --format docx

# Use Claude instead of OpenAI
t2md run examples/mit6_7960_lec01_intro_deep_learning --provider anthropic
```

These transcripts are intentionally raw and conversational — exactly the kind of content t2md is designed to clean up.
