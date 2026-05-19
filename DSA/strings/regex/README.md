# Pattern: Regular Expressions

Use regex when string parsing involves **multiple delimiters, complex patterns, or character class matching** that would require chaining multiple string operations otherwise.

Think: *One expression instead of five `.replace()` calls.*

---

## When to Use Regex

- Splitting on **multiple delimiters** at once (`[.?!]`)
- Validating or extracting patterns (emails, numbers, words)
- Cleaning input with variable whitespace or punctuation
- When custom loop logic would be harder to read and maintain

Key insight: Regex trades readability of the pattern for simplicity of the surrounding code. Use it when the alternative is messier, not as a default.

---

## Core Template (Mental Model)

```python
import re

# Split on multiple delimiters
sentences = re.split(r'[.?!]', text)

# Find all matches
words = re.findall(r'[a-zA-Z]+', text)

# Check if token contains at least one letter
has_letter = bool(re.search(r'[a-zA-Z]', token))

# Substitute / clean
cleaned = re.sub(r'\s+', ' ', text).strip()
```

---

## Common Variations

### Split on multiple delimiters
```python
re.split(r'[.?!;]', text)   # extend by adding chars inside []
```

### Extract all words
```python
re.findall(r'\b[a-zA-Z]+\b', text)
```

### Validate format
```python
bool(re.fullmatch(r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}', email))
```

---

## Key Patterns

**Character class `[]`**: Match any one character in the set — easy to extend

**`re.split`**: Cleaner than chaining `.replace()` for multi-delimiter splits

**`re.findall`**: Returns all non-overlapping matches as a list

**`any(c.isalpha() for c in token)`**: Pythonic alternative for simple letter checks without importing re

---

## Pitfalls

- **Forgetting raw strings**: Always use `r'...'` — backslashes in regex need it
- **Greedy vs lazy**: `.*` is greedy, `.*?` is lazy — wrong choice causes over-matching
- **Overusing regex**: For single-character splits or simple checks, `.split()` and `.isalpha()` are cleaner

---

## Problems

| Problem | File | Key Twist |
|---------|------|-----------|
| Maximum Number of Words in a Sentence (LC 2114) | `max_words_in_sentence.py` | Split on `[.?!]`, filter tokens with at least one letter |